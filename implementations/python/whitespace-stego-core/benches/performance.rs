//! Performance benchmarks for whitespace steganography core library.
//!
//! These benchmarks measure the performance of encoding and decoding operations
//! with various input sizes and configurations.

use criterion::{black_box, criterion_group, criterion_main, Criterion};
use whitespace_stego_core::*;

fn bench_encode_small(c: &mut Criterion) {
    let message = "Hello, World!";
    let carrier = "This is a short carrier text.";

    c.bench_function("encode_small", |b| {
        b.iter(|| encode(black_box(message), black_box(carrier), black_box(None)))
    });
}

fn bench_decode_small(c: &mut Criterion) {
    let message = "Hello, World!";
    let carrier = "This is a short carrier text.";
    let encoded = encode(message, carrier, None).unwrap();

    c.bench_function("decode_small", |b| {
        b.iter(|| decode(black_box(&encoded), black_box(None)))
    });
}

fn bench_encode_medium(c: &mut Criterion) {
    let message = "This is a medium-sized message that contains more text to encode. It should provide a good benchmark for typical usage patterns.";
    let carrier = "This is a medium-sized carrier text that will contain the encoded message. It provides a realistic scenario for benchmarking.";

    c.bench_function("encode_medium", |b| {
        b.iter(|| encode(black_box(message), black_box(carrier), black_box(None)))
    });
}

fn bench_decode_medium(c: &mut Criterion) {
    let message = "This is a medium-sized message that contains more text to encode. It should provide a good benchmark for typical usage patterns.";
    let carrier = "This is a medium-sized carrier text that will contain the encoded message. It provides a realistic scenario for benchmarking.";
    let encoded = encode(message, carrier, None).unwrap();

    c.bench_function("decode_medium", |b| {
        b.iter(|| decode(black_box(&encoded), black_box(None)))
    });
}

fn bench_encode_large(c: &mut Criterion) {
    let message = "A".repeat(1000);
    let carrier = "This is a large carrier text. ".repeat(50);

    c.bench_function("encode_large", |b| {
        b.iter(|| encode(black_box(&message), black_box(&carrier), black_box(None)))
    });
}

fn bench_decode_large(c: &mut Criterion) {
    let message = "A".repeat(1000);
    let carrier = "This is a large carrier text. ".repeat(50);
    let encoded = encode(&message, &carrier, None).unwrap();

    c.bench_function("decode_large", |b| {
        b.iter(|| decode(black_box(&encoded), black_box(None)))
    });
}

fn bench_encode_with_password(c: &mut Criterion) {
    let message = "Secret message";
    let carrier = "Public carrier text";
    let password = "my_secret_password";

    c.bench_function("encode_with_password", |b| {
        b.iter(|| {
            encode(
                black_box(message),
                black_box(carrier),
                black_box(Some(password)),
            )
        })
    });
}

fn bench_decode_with_password(c: &mut Criterion) {
    let message = "Secret message";
    let carrier = "Public carrier text";
    let password = "my_secret_password";
    let encoded = encode(message, carrier, Some(password)).unwrap();

    c.bench_function("decode_with_password", |b| {
        b.iter(|| decode(black_box(&encoded), black_box(Some(password))))
    });
}

fn bench_encode_binary(c: &mut Criterion) {
    let data = b"This is binary data for benchmarking the encode_binary function.";

    c.bench_function("encode_binary", |b| {
        b.iter(|| encode_binary(black_box(data)))
    });
}

fn bench_decode_binary(c: &mut Criterion) {
    let data = b"This is binary data for benchmarking the decode_binary function.";
    let encoded = encode_binary(data);

    c.bench_function("decode_binary", |b| {
        b.iter(|| decode_binary(black_box(&encoded)))
    });
}

fn bench_has_encoded_message(c: &mut Criterion) {
    let message = "Test message";
    let carrier = "Carrier text";
    let encoded = encode(message, carrier, None).unwrap();
    let plain_text = "Plain text without any encoded message";

    c.bench_function("has_encoded_message_true", |b| {
        b.iter(|| has_encoded_message(black_box(&encoded)))
    });

    c.bench_function("has_encoded_message_false", |b| {
        b.iter(|| has_encoded_message(black_box(plain_text)))
    });
}

fn bench_extract_encoded(c: &mut Criterion) {
    let message = "Test message";
    let carrier = "Carrier text";
    let encoded = encode(message, carrier, None).unwrap();

    c.bench_function("extract_encoded", |b| {
        b.iter(|| extract_encoded(black_box(&encoded)))
    });
}

fn bench_get_encoded_message_position(c: &mut Criterion) {
    let message = "Test message";
    let carrier = "Carrier text";
    let encoded = encode(message, carrier, None).unwrap();

    c.bench_function("get_encoded_message_position", |b| {
        b.iter(|| get_encoded_message_position(black_box(&encoded)))
    });
}

fn bench_get_encoded_message_size(c: &mut Criterion) {
    let message = "Test message";
    let carrier = "Carrier text";
    let encoded = encode(message, carrier, None).unwrap();

    c.bench_function("get_encoded_message_size", |b| {
        b.iter(|| get_encoded_message_size(black_box(&encoded)))
    });
}

fn bench_encrypt_data(c: &mut Criterion) {
    let data = b"This is test data for encryption benchmarking.";
    let password = "test_password";

    c.bench_function("encrypt_data", |b| {
        b.iter(|| encrypt_data(black_box(data), black_box(password)))
    });
}

fn bench_decrypt_data(c: &mut Criterion) {
    let data = b"This is test data for decryption benchmarking.";
    let password = "test_password";
    let encrypted = encrypt_data(data, password).unwrap();

    c.bench_function("decrypt_data", |b| {
        b.iter(|| decrypt_data(black_box(&encrypted), black_box(password)))
    });
}

fn bench_derive_fernet_key(c: &mut Criterion) {
    let password = "test_password_for_key_derivation";

    c.bench_function("derive_fernet_key", |b| {
        b.iter(|| derive_fernet_key(black_box(password)))
    });
}

criterion_group!(
    benches,
    bench_encode_small,
    bench_decode_small,
    bench_encode_medium,
    bench_decode_medium,
    bench_encode_large,
    bench_decode_large,
    bench_encode_with_password,
    bench_decode_with_password,
    bench_encode_binary,
    bench_decode_binary,
    bench_has_encoded_message,
    bench_extract_encoded,
    bench_get_encoded_message_position,
    bench_get_encoded_message_size,
    bench_encrypt_data,
    bench_decrypt_data,
    bench_derive_fernet_key,
);
criterion_main!(benches);
