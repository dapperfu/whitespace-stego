use aes_gcm::{
    aead::{Aead, KeyInit},
    Aes256Gcm, Key, Nonce,
};
use base64::{engine::general_purpose::STANDARD as BASE64, Engine};
use clap::{Parser, Subcommand};
use pbkdf2::{
    password_hash::{PasswordHash, PasswordHasher, SaltString},
    Pbkdf2,
};
use std::{
    fs::File,
    io::{self, Read, Write},
    path::PathBuf,
};
use thiserror::Error;

const ZERO_WIDTH_SPACE: char = '\u{200B}';
const ZERO_WIDTH_NON_JOINER: char = '\u{200C}';
const WORD_JOINER: char = '\u{2060}';
const FUNCTION_APPLICATION: char = '\u{2061}';

#[derive(Error, Debug)]
pub enum StegoError {
    #[error("Encryption error: {0}")]
    Encryption(String),
    #[error("Decryption error: {0}")]
    Decryption(String),
    #[error("Invalid carrier: {0}")]
    InvalidCarrier(String),
    #[error("IO error: {0}")]
    Io(#[from] io::Error),
}

impl From<aes_gcm::Error> for StegoError {
    fn from(err: aes_gcm::Error) -> Self {
        StegoError::Encryption(err.to_string())
    }
}

fn derive_key(password: &str) -> Result<Key<Aes256Gcm>, StegoError> {
    let salt = SaltString::generate(&mut rand::thread_rng());
    let hash = Pbkdf2::hash_password(password.as_bytes(), &salt)
        .map_err(|e| StegoError::Encryption(e.to_string()))?;
    let key_bytes = hash.hash.unwrap().as_bytes();
    Key::<Aes256Gcm>::from_slice(key_bytes)
        .try_clone()
        .map_err(|e| StegoError::Encryption(e.to_string()))
}

fn encrypt_message(message: &str, password: Option<&str>) -> Result<String, StegoError> {
    if let Some(pwd) = password {
        let key = derive_key(pwd)?;
        let cipher = Aes256Gcm::new(&key);
        let nonce = Nonce::from_slice(b"whitespace_stego_nonce");
        let ciphertext = cipher
            .encrypt(nonce, message.as_bytes())
            .map_err(|e| StegoError::Encryption(e.to_string()))?;
        Ok(BASE64.encode(ciphertext))
    } else {
        Ok(BASE64.encode(message.as_bytes()))
    }
}

fn decrypt_message(encrypted: &str, password: Option<&str>) -> Result<String, StegoError> {
    if let Some(pwd) = password {
        let key = derive_key(pwd)?;
        let cipher = Aes256Gcm::new(&key);
        let nonce = Nonce::from_slice(b"whitespace_stego_nonce");
        let ciphertext = BASE64
            .decode(encrypted)
            .map_err(|e| StegoError::Decryption(e.to_string()))?;
        let plaintext = cipher
            .decrypt(nonce, ciphertext.as_slice())
            .map_err(|e| StegoError::Decryption(e.to_string()))?;
        String::from_utf8(plaintext).map_err(|e| StegoError::Decryption(e.to_string()))
    } else {
        let decoded = BASE64
            .decode(encrypted)
            .map_err(|e| StegoError::Decryption(e.to_string()))?;
        String::from_utf8(decoded).map_err(|e| StegoError::Decryption(e.to_string()))
    }
}

fn binary_to_zero_width(binary: &str) -> String {
    binary
        .chars()
        .map(|c| match c {
            '0' => ZERO_WIDTH_SPACE,
            '1' => ZERO_WIDTH_NON_JOINER,
            _ => c,
        })
        .collect()
}

fn zero_width_to_binary(zero_width: &str) -> String {
    zero_width
        .chars()
        .map(|c| match c {
            c if c == ZERO_WIDTH_SPACE => '0',
            c if c == ZERO_WIDTH_NON_JOINER => '1',
            _ => c,
        })
        .collect()
}

fn encode(message: &str, carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    let encrypted = encrypt_message(message, password)?;
    
    let binary: String = encrypted
        .bytes()
        .map(|b| format!("{:08b}", b))
        .collect();
    
    let zero_width = binary_to_zero_width(&binary);
    let framed = format!("{}{}{}", WORD_JOINER, zero_width, FUNCTION_APPLICATION);
    
    if carrier.is_empty() {
        Ok(framed)
    } else {
        Ok(format!("{}{}{}", &carrier[0..1], framed, &carrier[1..]))
    }
}

fn decode(carrier: &str, password: Option<&str>) -> Result<String, StegoError> {
    let start = carrier
        .find(WORD_JOINER)
        .ok_or_else(|| StegoError::InvalidCarrier("No start delimiter found".into()))?;
    let end = carrier
        .find(FUNCTION_APPLICATION)
        .ok_or_else(|| StegoError::InvalidCarrier("No end delimiter found".into()))?;
    
    if start >= end {
        return Err(StegoError::InvalidCarrier("Invalid message format".into()));
    }
    
    let zero_width = &carrier[start + 1..end];
    let binary = zero_width_to_binary(zero_width);
    
    let mut encrypted = String::new();
    for chunk in binary.as_bytes().chunks(8) {
        let byte = u8::from_str_radix(&String::from_utf8_lossy(chunk), 2)
            .map_err(|e| StegoError::Decryption(e.to_string()))?;
        encrypted.push(byte as char);
    }
    
    decrypt_message(&encrypted, password)
}

fn read_file(path: &PathBuf) -> Result<String, StegoError> {
    let mut file = File::open(path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents.trim().to_string())
}

fn write_file(path: &PathBuf, contents: &str) -> Result<(), StegoError> {
    let mut file = File::create(path)?;
    file.write_all(contents.as_bytes())?;
    Ok(())
}

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    Encode {
        #[arg(short, long)]
        message: Option<String>,
        #[arg(short = 'f', long)]
        message_file: Option<PathBuf>,
        #[arg(short, long)]
        carrier: Option<String>,
        #[arg(short = 'f', long)]
        carrier_file: Option<PathBuf>,
        #[arg(short, long)]
        password: Option<String>,
        #[arg(short = 'f', long)]
        password_file: Option<PathBuf>,
        #[arg(short, long)]
        output: Option<PathBuf>,
    },
    Decode {
        #[arg(short, long)]
        carrier: Option<String>,
        #[arg(short = 'f', long)]
        carrier_file: Option<PathBuf>,
        #[arg(short, long)]
        password: Option<String>,
        #[arg(short = 'f', long)]
        password_file: Option<PathBuf>,
        #[arg(short, long)]
        output: Option<PathBuf>,
    },
}

fn main() -> Result<(), StegoError> {
    let cli = Cli::parse();

    match cli.command {
        Commands::Encode {
            message,
            message_file,
            carrier,
            carrier_file,
            password,
            password_file,
            output,
        } => {
            let message = if let Some(msg) = message {
                msg
            } else if let Some(path) = message_file {
                read_file(&path)?
            } else {
                return Err(StegoError::InvalidCarrier("Message is required".into()));
            };

            let carrier = if let Some(car) = carrier {
                car
            } else if let Some(path) = carrier_file {
                read_file(&path)?
            } else {
                String::new()
            };

            let password = if let Some(pwd) = password {
                Some(pwd)
            } else if let Some(path) = password_file {
                Some(read_file(&path)?)
            } else {
                None
            };

            let result = encode(&message, &carrier, password.as_deref())?;

            if let Some(path) = output {
                write_file(&path, &result)?;
            } else {
                println!("{}", result);
            }
        }
        Commands::Decode {
            carrier,
            carrier_file,
            password,
            password_file,
            output,
        } => {
            let carrier = if let Some(car) = carrier {
                car
            } else if let Some(path) = carrier_file {
                read_file(&path)?
            } else {
                return Err(StegoError::InvalidCarrier("Carrier is required".into()));
            };

            let password = if let Some(pwd) = password {
                Some(pwd)
            } else if let Some(path) = password_file {
                Some(read_file(&path)?)
            } else {
                None
            };

            let result = decode(&carrier, password.as_deref())?;

            if let Some(path) = output {
                write_file(&path, &result)?;
            } else {
                println!("{}", result);
            }
        }
    }

    Ok(())
} 