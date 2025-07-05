# Benchmark Results

## Test Configuration
- **Test Messages**: Various sizes from 1 byte to Unicode strings
- **Test Passwords**: Empty, simple, complex, and Unicode
- **Carrier Text**: Standard test carrier
- **Runs**: Automatically adjusted based on coefficient of variation (CV < 10%)

## Results Summary

| Implementation | Message Size | Password | Runs | Encode (ms) | Decode (ms) | Total (ms) | CV (%) |
|----------------|--------------|----------|------|-------------|-------------|------------|--------|
| python-c        | J            | 🚀🌟🎉 |    0 |             |             |            |        |
| rust            | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | Hello, World! | simple_password |    0 |             |             |            |      0 |
| rust            | Hello, World! | simple_password |    0 |             |             |            |      0 |
| rust            | Hello, World! | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | Hello, World! | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | This is a longer tes... | simple_password |    0 |             |             |            |      0 |
| rust            | This is a longer tes... | simple_password |    0 |             |             |            |      0 |
| rust            | This is a longer tes... | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | This is a longer tes... | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | Unicode: 🚀🌟� | simple_password |    0 |             |             |            |      0 |
| rust            | Unicode: 🚀🌟� | simple_password |    0 |             |             |            |      0 |
| rust            | Unicode: 🚀🌟� | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | Unicode: 🚀🌟� | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | A            | simple_password |    0 |             |             |            |      0 |
| rust            | A            | simple_password |    0 |             |             |            |      0 |
| rust            | A            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | A            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | B            | simple_password |    0 |             |             |            |      0 |
| rust            | B            | simple_password |    0 |             |             |            |      0 |
| rust            | B            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | B            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | C            | simple_password |    0 |             |             |            |      0 |
| rust            | C            | simple_password |    0 |             |             |            |      0 |
| rust            | C            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | C            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | D            | simple_password |    0 |             |             |            |      0 |
| rust            | D            | simple_password |    0 |             |             |            |      0 |
| rust            | D            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | D            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | E            | simple_password |    0 |             |             |            |      0 |
| rust            | E            | simple_password |    0 |             |             |            |      0 |
| rust            | E            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | E            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | F            | simple_password |    0 |             |             |            |      0 |
| rust            | F            | simple_password |    0 |             |             |            |      0 |
| rust            | F            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | F            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | G            | simple_password |    0 |             |             |            |      0 |
| rust            | G            | simple_password |    0 |             |             |            |      0 |
| rust            | G            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | G            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | H            | simple_password |    0 |             |             |            |      0 |
| rust            | H            | simple_password |    0 |             |             |            |      0 |
| rust            | H            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | H            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | I            | simple_password |    0 |             |             |            |      0 |
| rust            | I            | simple_password |    0 |             |             |            |      0 |
| rust            | I            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | I            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | J            | simple_password |    0 |             |             |            |      0 |
| rust            | J            | simple_password |    0 |             |             |            |      0 |
| rust            | J            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | J            | complex_password_123!@# |    0 |             |             |            |      0 |
| rust            | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| rust            | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | Hello, World! | simple_password |    0 |             |             |            |      0 |
| go              | Hello, World! | simple_password |    0 |             |             |            |      0 |
| go              | Hello, World! | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | Hello, World! | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | This is a longer tes... | simple_password |    0 |             |             |            |      0 |
| go              | This is a longer tes... | simple_password |    0 |             |             |            |      0 |
| go              | This is a longer tes... | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | This is a longer tes... | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | Unicode: 🚀🌟� | simple_password |    0 |             |             |            |      0 |
| go              | Unicode: 🚀🌟� | simple_password |    0 |             |             |            |      0 |
| go              | Unicode: 🚀🌟� | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | Unicode: 🚀🌟� | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | A            | simple_password |    0 |             |             |            |      0 |
| go              | A            | simple_password |    0 |             |             |            |      0 |
| go              | A            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | A            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | B            | simple_password |    0 |             |             |            |      0 |
| go              | B            | simple_password |    0 |             |             |            |      0 |
| go              | B            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | B            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | C            | simple_password |    0 |             |             |            |      0 |
| go              | C            | simple_password |    0 |             |             |            |      0 |
| go              | C            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | C            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | D            | simple_password |    0 |             |             |            |      0 |
| go              | D            | simple_password |    0 |             |             |            |      0 |
| go              | D            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | D            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | E            | simple_password |    0 |             |             |            |      0 |
| go              | E            | simple_password |    0 |             |             |            |      0 |
| go              | E            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | E            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | F            | simple_password |    0 |             |             |            |      0 |
| go              | F            | simple_password |    0 |             |             |            |      0 |
| go              | F            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | F            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | G            | simple_password |    0 |             |             |            |      0 |
| go              | G            | simple_password |    0 |             |             |            |      0 |
| go              | G            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | G            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | H            | simple_password |    0 |             |             |            |      0 |
| go              | H            | simple_password |    0 |             |             |            |      0 |
| go              | H            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | H            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | I            | simple_password |    0 |             |             |            |      0 |
| go              | I            | simple_password |    0 |             |             |            |      0 |
| go              | I            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | I            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | J            | simple_password |    0 |             |             |            |      0 |
| go              | J            | simple_password |    0 |             |             |            |      0 |
| go              | J            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | J            | complex_password_123!@# |    0 |             |             |            |      0 |
| go              | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| go              | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | Hello, World! | simple_password |    0 |             |             |            |      0 |
| python-pure     | Hello, World! | simple_password |    0 |             |             |            |      0 |
| python-pure     | Hello, World! | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | Hello, World! | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | This is a longer tes... | simple_password |    0 |             |             |            |      0 |
| python-pure     | This is a longer tes... | simple_password |    0 |             |             |            |      0 |
| python-pure     | This is a longer tes... | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | This is a longer tes... | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | Unicode: 🚀🌟� | simple_password |    0 |             |             |            |      0 |
| python-pure     | Unicode: 🚀🌟� | simple_password |    0 |             |             |            |      0 |
| python-pure     | Unicode: 🚀🌟� | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | Unicode: 🚀🌟� | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | A            | simple_password |    0 |             |             |            |      0 |
| python-pure     | A            | simple_password |    0 |             |             |            |      0 |
| python-pure     | A            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | A            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | B            | simple_password |    0 |             |             |            |      0 |
| python-pure     | B            | simple_password |    0 |             |             |            |      0 |
| python-pure     | B            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | B            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | C            | simple_password |    0 |             |             |            |      0 |
| python-pure     | C            | simple_password |    0 |             |             |            |      0 |
| python-pure     | C            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | C            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | D            | simple_password |    0 |             |             |            |      0 |
| python-pure     | D            | simple_password |    0 |             |             |            |      0 |
| python-pure     | D            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | D            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | E            | simple_password |    0 |             |             |            |      0 |
| python-pure     | E            | simple_password |    0 |             |             |            |      0 |
| python-pure     | E            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | E            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | F            | simple_password |    0 |             |             |            |      0 |
| python-pure     | F            | simple_password |    0 |             |             |            |      0 |
| python-pure     | F            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | F            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | G            | simple_password |    0 |             |             |            |      0 |
| python-pure     | G            | simple_password |    0 |             |             |            |      0 |
| python-pure     | G            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | G            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | H            | simple_password |    0 |             |             |            |      0 |
| python-pure     | H            | simple_password |    0 |             |             |            |      0 |
| python-pure     | H            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | H            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | I            | simple_password |    0 |             |             |            |      0 |
| python-pure     | I            | simple_password |    0 |             |             |            |      0 |
| python-pure     | I            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | I            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | J            | simple_password |    0 |             |             |            |      0 |
| python-pure     | J            | simple_password |    0 |             |             |            |      0 |
| python-pure     | J            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | J            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-pure     | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-pure     | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | Hello, World! | simple_password |    0 |             |             |            |      0 |
| python-rust     | Hello, World! | simple_password |    0 |             |             |            |      0 |
| python-rust     | Hello, World! | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | Hello, World! | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | This is a longer tes... | simple_password |    0 |             |             |            |      0 |
| python-rust     | This is a longer tes... | simple_password |    0 |             |             |            |      0 |
| python-rust     | This is a longer tes... | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | This is a longer tes... | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | Unicode: 🚀🌟� | simple_password |    0 |             |             |            |      0 |
| python-rust     | Unicode: 🚀🌟� | simple_password |    0 |             |             |            |      0 |
| python-rust     | Unicode: 🚀🌟� | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | Unicode: 🚀🌟� | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | A            | simple_password |    0 |             |             |            |      0 |
| python-rust     | A            | simple_password |    0 |             |             |            |      0 |
| python-rust     | A            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | A            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | B            | simple_password |    0 |             |             |            |      0 |
| python-rust     | B            | simple_password |    0 |             |             |            |      0 |
| python-rust     | B            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | B            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | C            | simple_password |    0 |             |             |            |      0 |
| python-rust     | C            | simple_password |    0 |             |             |            |      0 |
| python-rust     | C            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | C            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | D            | simple_password |    0 |             |             |            |      0 |
| python-rust     | D            | simple_password |    0 |             |             |            |      0 |
| python-rust     | D            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | D            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | E            | simple_password |    0 |             |             |            |      0 |
| python-rust     | E            | simple_password |    0 |             |             |            |      0 |
| python-rust     | E            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | E            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | F            | simple_password |    0 |             |             |            |      0 |
| python-rust     | F            | simple_password |    0 |             |             |            |      0 |
| python-rust     | F            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | F            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | G            | simple_password |    0 |             |             |            |      0 |
| python-rust     | G            | simple_password |    0 |             |             |            |      0 |
| python-rust     | G            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | G            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | H            | simple_password |    0 |             |             |            |      0 |
| python-rust     | H            | simple_password |    0 |             |             |            |      0 |
| python-rust     | H            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | H            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | I            | simple_password |    0 |             |             |            |      0 |
| python-rust     | I            | simple_password |    0 |             |             |            |      0 |
| python-rust     | I            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | I            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | J            | simple_password |    0 |             |             |            |      0 |
| python-rust     | J            | simple_password |    0 |             |             |            |      0 |
| python-rust     | J            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | J            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-rust     | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-rust     | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | Hello, World! | simple_password |    0 |             |             |            |      0 |
| python-c        | Hello, World! | simple_password |    0 |             |             |            |      0 |
| python-c        | Hello, World! | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | Hello, World! | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | Hello, World! | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | This is a longer tes... | simple_password |    0 |             |             |            |      0 |
| python-c        | This is a longer tes... | simple_password |    0 |             |             |            |      0 |
| python-c        | This is a longer tes... | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | This is a longer tes... | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | This is a longer tes... | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | Unicode: 🚀🌟� | simple_password |    0 |             |             |            |      0 |
| python-c        | Unicode: 🚀🌟� | simple_password |    0 |             |             |            |      0 |
| python-c        | Unicode: 🚀🌟� | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | Unicode: 🚀🌟� | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | Unicode: 🚀🌟� | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | A            | simple_password |    0 |             |             |            |      0 |
| python-c        | A            | simple_password |    0 |             |             |            |      0 |
| python-c        | A            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | A            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | A            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | B            | simple_password |    0 |             |             |            |      0 |
| python-c        | B            | simple_password |    0 |             |             |            |      0 |
| python-c        | B            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | B            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | B            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | C            | simple_password |    0 |             |             |            |      0 |
| python-c        | C            | simple_password |    0 |             |             |            |      0 |
| python-c        | C            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | C            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | C            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | D            | simple_password |    0 |             |             |            |      0 |
| python-c        | D            | simple_password |    0 |             |             |            |      0 |
| python-c        | D            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | D            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | D            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | E            | simple_password |    0 |             |             |            |      0 |
| python-c        | E            | simple_password |    0 |             |             |            |      0 |
| python-c        | E            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | E            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | E            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | F            | simple_password |    0 |             |             |            |      0 |
| python-c        | F            | simple_password |    0 |             |             |            |      0 |
| python-c        | F            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | F            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | F            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | G            | simple_password |    0 |             |             |            |      0 |
| python-c        | G            | simple_password |    0 |             |             |            |      0 |
| python-c        | G            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | G            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | G            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | H            | simple_password |    0 |             |             |            |      0 |
| python-c        | H            | simple_password |    0 |             |             |            |      0 |
| python-c        | H            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | H            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | H            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | I            | simple_password |    0 |             |             |            |      0 |
| python-c        | I            | simple_password |    0 |             |             |            |      0 |
| python-c        | I            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | I            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | I            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |
| python-c        | J            | simple_password |    0 |             |             |            |      0 |
| python-c        | J            | simple_password |    0 |             |             |            |      0 |
| python-c        | J            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | J            | complex_password_123!@# |    0 |             |             |            |      0 |
| python-c        | J            | 🚀🌟🎉 |    0 |             |             |            |      0 |

## Performance Analysis

### Fastest Implementations
- **Encode**: [Implementation] - [Time] ms
- **Decode**: [Implementation] - [Time] ms
- **Total**: [Implementation] - [Time] ms

### Memory Usage
- **Static C**: No dynamic allocation, predictable memory usage
- **Dynamic C**: Uses malloc/free, variable memory usage
- **Rust**: Safe memory management with ownership
- **Go**: Garbage collected, automatic memory management
- **Python**: Garbage collected, higher memory overhead

### Recommendations
- Use **Static C** for embedded/safety-critical systems
- Use **Rust** for high-performance applications
- Use **Python** for rapid prototyping and development
- Use **Go** for concurrent applications
- Use **Dynamic C** for flexibility and large data

## Test Environment
- **OS**: $(uname -s) $(uname -r)
- **Architecture**: $(uname -m)
- **CPU**: $(grep "model name" /proc/cpuinfo | head -1 | cut -d':' -f2 | xargs)
- **Memory**: $(free -h | grep Mem | awk '{print $2}')
- **Date**: $(date)
