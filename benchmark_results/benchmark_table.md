# Benchmark Results

## Test Configuration
- **Test Messages**: Various sizes from 1 byte to Unicode strings
- **Test Passwords**: Empty, simple, complex, and Unicode
- **Carrier Text**: Standard test carrier
- **Runs**: Automatically adjusted based on coefficient of variation (CV < 10%)

## Results Summary

| Implementation | Message Size | Password | Runs | Encode (ms) | Decode (ms) | Total (ms) | CV (%) |
|----------------|--------------|----------|------|-------------|-------------|------------|--------|
| go              | J            | 🚀🌟🎉 |    0 |             |             |            |        |
| go              | J            | 🚀🌟🎉 |    0 |             |             |            |        |
| go              | J            | 🚀🌟🎉 |    0 |             |             |            |        |
| rust            | Hello, World! | 🚀🌟🎉 |    2 |       5.000 |       8.000 |     14.000 |      0 |
| rust            | Hello, World! | 🚀🌟🎉 |    2 |       5.000 |       8.000 |     14.000 |      0 |
| rust            | Hello, World! | 🚀🌟🎉 |    2 |       5.000 |       8.000 |     14.000 |      0 |
| rust            | Hello, World! | 🚀🌟🎉 |    2 |       5.000 |       8.000 |     14.000 |      0 |
| rust            | Hello, World! | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | Hello, World! | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | Hello, World! | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | Hello, World! | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | Hello, World! | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |  6.200 |
| rust            | Hello, World! | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |  6.200 |
| rust            | Hello, World! | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |  6.200 |
| rust            | Hello, World! | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |  6.200 |
| rust            | Hello, World! | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | Hello, World! | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | Hello, World! | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | Hello, World! | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    2 |       5.000 |      12.000 |     18.000 |      0 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    2 |       5.000 |      12.000 |     18.000 |      0 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    2 |       5.000 |      12.000 |     18.000 |      0 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    2 |       5.000 |      12.000 |     18.000 |      0 |
| rust            | This is a longer tes... | simple_password |    2 |       6.000 |      14.000 |     20.000 |      0 |
| rust            | This is a longer tes... | simple_password |    2 |       6.000 |      14.000 |     20.000 |      0 |
| rust            | This is a longer tes... | simple_password |    2 |       6.000 |      14.000 |     20.000 |      0 |
| rust            | This is a longer tes... | simple_password |    2 |       6.000 |      14.000 |     20.000 |      0 |
| rust            | This is a longer tes... | complex_password_123!@# |    2 |       6.000 |      13.000 |     20.000 |      0 |
| rust            | This is a longer tes... | complex_password_123!@# |    2 |       6.000 |      13.000 |     20.000 |      0 |
| rust            | This is a longer tes... | complex_password_123!@# |    2 |       6.000 |      13.000 |     20.000 |      0 |
| rust            | This is a longer tes... | complex_password_123!@# |    2 |       6.000 |      13.000 |     20.000 |      0 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    2 |       6.000 |      14.000 |     20.000 |  5.000 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    2 |       6.000 |      14.000 |     20.000 |  5.000 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    2 |       6.000 |      14.000 |     20.000 |  5.000 |
| rust            | This is a longer tes... | 🚀🌟🎉 |    2 |       6.000 |      14.000 |     20.000 |  5.000 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       6.000 |       8.000 |     14.000 |      0 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       6.000 |       8.000 |     14.000 |      0 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       6.000 |       8.000 |     14.000 |      0 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       6.000 |       8.000 |     14.000 |      0 |
| rust            | Unicode: 🚀🌟� | simple_password |    2 |       6.000 |      11.000 |     17.000 |      0 |
| rust            | Unicode: 🚀🌟� | simple_password |    2 |       6.000 |      11.000 |     17.000 |      0 |
| rust            | Unicode: 🚀🌟� | simple_password |    2 |       6.000 |      11.000 |     17.000 |      0 |
| rust            | Unicode: 🚀🌟� | simple_password |    2 |       6.000 |      11.000 |     17.000 |      0 |
| rust            | Unicode: 🚀🌟� | complex_password_123!@# |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | Unicode: 🚀🌟� | complex_password_123!@# |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | Unicode: 🚀🌟� | complex_password_123!@# |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | Unicode: 🚀🌟� | complex_password_123!@# |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | A            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | A            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | A            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | A            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | A            | simple_password |    2 |       6.000 |      10.000 |     17.000 |      0 |
| rust            | A            | simple_password |    2 |       6.000 |      10.000 |     17.000 |      0 |
| rust            | A            | simple_password |    2 |       6.000 |      10.000 |     17.000 |      0 |
| rust            | A            | simple_password |    2 |       6.000 |      10.000 |     17.000 |      0 |
| rust            | A            | complex_password_123!@# |    2 |       5.000 |      10.000 |     16.000 |  6.200 |
| rust            | A            | complex_password_123!@# |    2 |       5.000 |      10.000 |     16.000 |  6.200 |
| rust            | A            | complex_password_123!@# |    2 |       5.000 |      10.000 |     16.000 |  6.200 |
| rust            | A            | complex_password_123!@# |    2 |       5.000 |      10.000 |     16.000 |  6.200 |
| rust            | A            | 🚀🌟🎉 |    2 |       6.000 |      10.000 |     16.000 |  6.200 |
| rust            | A            | 🚀🌟🎉 |    2 |       6.000 |      10.000 |     16.000 |  6.200 |
| rust            | A            | 🚀🌟🎉 |    2 |       6.000 |      10.000 |     16.000 |  6.200 |
| rust            | A            | 🚀🌟🎉 |    2 |       6.000 |      10.000 |     16.000 |  6.200 |
| rust            | B            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | B            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | B            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | B            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | B            | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | B            | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | B            | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | B            | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | B            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | B            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | B            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | B            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | B            | 🚀🌟🎉 |    2 |       5.000 |      23.000 |     29.000 | 46.900 |
| rust            | B            | 🚀🌟🎉 |    2 |       5.000 |      23.000 |     29.000 | 46.900 |
| rust            | B            | 🚀🌟🎉 |    2 |       5.000 |      23.000 |     29.000 | 46.900 |
| rust            | B            | 🚀🌟🎉 |    2 |       5.000 |      23.000 |     29.000 | 46.900 |
| rust            | C            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | C            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | C            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | C            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | C            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | C            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | C            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | C            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | C            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | C            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | C            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | C            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | C            | 🚀🌟🎉 |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | C            | 🚀🌟🎉 |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | C            | 🚀🌟🎉 |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | C            | 🚀🌟🎉 |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | D            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | D            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | D            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | D            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | D            | simple_password |    2 |       5.000 |      10.000 |     16.000 |      0 |
| rust            | D            | simple_password |    2 |       5.000 |      10.000 |     16.000 |      0 |
| rust            | D            | simple_password |    2 |       5.000 |      10.000 |     16.000 |      0 |
| rust            | D            | simple_password |    2 |       5.000 |      10.000 |     16.000 |      0 |
| rust            | D            | complex_password_123!@# |    2 |      10.000 |      18.000 |     29.000 |      0 |
| rust            | D            | complex_password_123!@# |    2 |      10.000 |      18.000 |     29.000 |      0 |
| rust            | D            | complex_password_123!@# |    2 |      10.000 |      18.000 |     29.000 |      0 |
| rust            | D            | complex_password_123!@# |    2 |      10.000 |      18.000 |     29.000 |      0 |
| rust            | D            | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | D            | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | D            | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | D            | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | D            | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | E            | 🚀🌟🎉 |    3 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | E            | 🚀🌟🎉 |    3 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | E            | 🚀🌟🎉 |    3 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | E            | 🚀🌟🎉 |    3 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | E            | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | E            | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | E            | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | E            | simple_password |    2 |       5.000 |      10.000 |     15.000 |      0 |
| rust            | E            | complex_password_123!@# |    2 |       7.000 |      10.000 |     17.000 |      0 |
| rust            | E            | complex_password_123!@# |    2 |       7.000 |      10.000 |     17.000 |      0 |
| rust            | E            | complex_password_123!@# |    2 |       7.000 |      10.000 |     17.000 |      0 |
| rust            | E            | complex_password_123!@# |    2 |       7.000 |      10.000 |     17.000 |      0 |
| rust            | E            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     18.000 |  5.500 |
| rust            | E            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     18.000 |  5.500 |
| rust            | E            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     18.000 |  5.500 |
| rust            | E            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     18.000 |  5.500 |
| rust            | F            | 🚀🌟🎉 |    2 |       8.000 |      10.000 |     19.000 |      0 |
| rust            | F            | 🚀🌟🎉 |    2 |       8.000 |      10.000 |     19.000 |      0 |
| rust            | F            | 🚀🌟🎉 |    2 |       8.000 |      10.000 |     19.000 |      0 |
| rust            | F            | 🚀🌟🎉 |    2 |       8.000 |      10.000 |     19.000 |      0 |
| rust            | F            | simple_password |    2 |       6.000 |      12.000 |     19.000 |      0 |
| rust            | F            | simple_password |    2 |       6.000 |      12.000 |     19.000 |      0 |
| rust            | F            | simple_password |    2 |       6.000 |      12.000 |     19.000 |      0 |
| rust            | F            | simple_password |    2 |       6.000 |      12.000 |     19.000 |      0 |
| rust            | F            | complex_password_123!@# |    2 |       7.000 |      14.000 |     21.000 |      0 |
| rust            | F            | complex_password_123!@# |    2 |       7.000 |      14.000 |     21.000 |      0 |
| rust            | F            | complex_password_123!@# |    2 |       7.000 |      14.000 |     21.000 |      0 |
| rust            | F            | complex_password_123!@# |    2 |       7.000 |      14.000 |     21.000 |      0 |
| rust            | F            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     18.000 |      0 |
| rust            | F            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     18.000 |      0 |
| rust            | F            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     18.000 |      0 |
| rust            | F            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     18.000 |      0 |
| rust            | G            | 🚀🌟🎉 |    2 |       6.000 |       6.000 |     13.000 |      0 |
| rust            | G            | 🚀🌟🎉 |    2 |       6.000 |       6.000 |     13.000 |      0 |
| rust            | G            | 🚀🌟🎉 |    2 |       6.000 |       6.000 |     13.000 |      0 |
| rust            | G            | 🚀🌟🎉 |    2 |       6.000 |       6.000 |     13.000 |      0 |
| rust            | G            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | G            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | G            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | G            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | G            | complex_password_123!@# |    2 |       5.000 |       9.000 |     15.000 |  6.600 |
| rust            | G            | complex_password_123!@# |    2 |       5.000 |       9.000 |     15.000 |  6.600 |
| rust            | G            | complex_password_123!@# |    2 |       5.000 |       9.000 |     15.000 |  6.600 |
| rust            | G            | complex_password_123!@# |    2 |       5.000 |       9.000 |     15.000 |  6.600 |
| rust            | G            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     17.000 |      0 |
| rust            | G            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     17.000 |      0 |
| rust            | G            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     17.000 |      0 |
| rust            | G            | 🚀🌟🎉 |    2 |       6.000 |      11.000 |     17.000 |      0 |
| rust            | H            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | H            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | H            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | H            | 🚀🌟🎉 |    2 |       5.000 |       7.000 |     13.000 |      0 |
| rust            | H            | simple_password |    2 |       6.000 |       9.000 |     15.000 |  6.600 |
| rust            | H            | simple_password |    2 |       6.000 |       9.000 |     15.000 |  6.600 |
| rust            | H            | simple_password |    2 |       6.000 |       9.000 |     15.000 |  6.600 |
| rust            | H            | simple_password |    2 |       6.000 |       9.000 |     15.000 |  6.600 |
| rust            | H            | complex_password_123!@# |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | H            | complex_password_123!@# |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | H            | complex_password_123!@# |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | H            | complex_password_123!@# |    2 |       5.000 |      11.000 |     17.000 |      0 |
| rust            | H            | 🚀🌟🎉 |    2 |       5.000 |      10.000 |     15.000 |  6.600 |
| rust            | H            | 🚀🌟🎉 |    2 |       5.000 |      10.000 |     15.000 |  6.600 |
| rust            | H            | 🚀🌟🎉 |    2 |       5.000 |      10.000 |     15.000 |  6.600 |
| rust            | H            | 🚀🌟🎉 |    2 |       5.000 |      10.000 |     15.000 |  6.600 |
| rust            | I            | 🚀🌟🎉 |    2 |       6.000 |       7.000 |     13.000 |      0 |
| rust            | I            | 🚀🌟🎉 |    2 |       6.000 |       7.000 |     13.000 |      0 |
| rust            | I            | 🚀🌟🎉 |    2 |       6.000 |       7.000 |     13.000 |      0 |
| rust            | I            | 🚀🌟🎉 |    2 |       6.000 |       7.000 |     13.000 |      0 |
| rust            | I            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | I            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | I            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | I            | simple_password |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | I            | complex_password_123!@# |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | I            | complex_password_123!@# |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | I            | complex_password_123!@# |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | I            | complex_password_123!@# |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | I            | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | I            | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | I            | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | I            | 🚀🌟🎉 |    2 |       5.000 |       9.000 |     15.000 |      0 |
| rust            | J            | 🚀🌟🎉 |    2 |       6.000 |       7.000 |     13.000 |      0 |
| rust            | J            | 🚀🌟🎉 |    2 |       6.000 |       7.000 |     13.000 |      0 |
| rust            | J            | 🚀🌟🎉 |    2 |       6.000 |       7.000 |     13.000 |      0 |
| rust            | J            | 🚀🌟🎉 |    2 |       6.000 |       7.000 |     13.000 |      0 |
| rust            | J            | simple_password |    2 |       6.000 |      10.000 |     17.000 |      0 |
| rust            | J            | simple_password |    2 |       6.000 |      10.000 |     17.000 |      0 |
| rust            | J            | simple_password |    2 |       6.000 |      10.000 |     17.000 |      0 |
| rust            | J            | simple_password |    2 |       6.000 |      10.000 |     17.000 |      0 |
| rust            | J            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | J            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | J            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | J            | complex_password_123!@# |    2 |       6.000 |      10.000 |     16.000 |      0 |
| rust            | J            | 🚀🌟🎉 |    2 |       5.000 |      10.000 |     16.000 |      0 |
| rust            | J            | 🚀🌟🎉 |    2 |       5.000 |      10.000 |     16.000 |      0 |
| rust            | J            | 🚀🌟🎉 |    2 |       5.000 |      10.000 |     16.000 |      0 |
| rust            | J            | 🚀🌟🎉 |    2 |       5.000 |      10.000 |     16.000 |      0 |
| go              | Hello, World! | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | Hello, World! | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | Hello, World! | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | Hello, World! | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | Hello, World! | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | Hello, World! | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | Hello, World! | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | Hello, World! | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | Hello, World! | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | Hello, World! | complex_password_123!@# |    3 |       6.000 |       6.000 |     12.000 | 11.700 |
| go              | Hello, World! | complex_password_123!@# |    3 |       6.000 |       6.000 |     12.000 | 11.700 |
| go              | Hello, World! | complex_password_123!@# |    3 |       6.000 |       6.000 |     12.000 | 11.700 |
| go              | Hello, World! | complex_password_123!@# |    3 |       6.000 |       6.000 |     12.000 | 11.700 |
| go              | Hello, World! | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | Hello, World! | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | Hello, World! | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | Hello, World! | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | This is a longer tes... | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | This is a longer tes... | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | This is a longer tes... | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | This is a longer tes... | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | This is a longer tes... | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | This is a longer tes... | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | This is a longer tes... | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | This is a longer tes... | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    2 |       6.000 |       6.000 |     13.000 |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    2 |       6.000 |       6.000 |     13.000 |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    2 |       6.000 |       6.000 |     13.000 |      0 |
| go              | This is a longer tes... | 🚀🌟🎉 |    2 |       6.000 |       6.000 |     13.000 |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | Unicode: 🚀🌟� | simple_password |    2 |       6.000 |       5.000 |     11.000 |      0 |
| go              | Unicode: 🚀🌟� | simple_password |    2 |       6.000 |       5.000 |     11.000 |      0 |
| go              | Unicode: 🚀🌟� | simple_password |    2 |       6.000 |       5.000 |     11.000 |      0 |
| go              | Unicode: 🚀🌟� | simple_password |    2 |       6.000 |       5.000 |     11.000 |      0 |
| go              | Unicode: 🚀🌟� | complex_password_123!@# |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | Unicode: 🚀🌟� | complex_password_123!@# |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | Unicode: 🚀🌟� | complex_password_123!@# |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | Unicode: 🚀🌟� | complex_password_123!@# |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | Unicode: 🚀🌟� | 🚀🌟🎉 |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | A            | 🚀🌟🎉 |    3 |       4.000 |       4.000 |      9.000 |      0 |
| go              | A            | 🚀🌟🎉 |    3 |       4.000 |       4.000 |      9.000 |      0 |
| go              | A            | 🚀🌟🎉 |    3 |       4.000 |       4.000 |      9.000 |      0 |
| go              | A            | 🚀🌟🎉 |    3 |       4.000 |       4.000 |      9.000 |      0 |
| go              | A            | simple_password |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | A            | simple_password |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | A            | simple_password |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | A            | simple_password |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | A            | simple_password |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | A            | complex_password_123!@# |    3 |       4.000 |       4.000 |      9.000 |      0 |
| go              | A            | complex_password_123!@# |    3 |       4.000 |       4.000 |      9.000 |      0 |
| go              | A            | complex_password_123!@# |    3 |       4.000 |       4.000 |      9.000 |      0 |
| go              | A            | complex_password_123!@# |    3 |       4.000 |       4.000 |      9.000 |      0 |
| go              | A            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | A            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | A            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | A            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | B            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | B            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | B            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | B            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | B            | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | B            | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | B            | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | B            | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | B            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 | 11.100 |
| go              | B            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 | 11.100 |
| go              | B            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 | 11.100 |
| go              | B            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 | 11.100 |
| go              | B            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | B            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | B            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | B            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | C            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | C            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | C            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | C            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | C            | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | C            | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | C            | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | C            | simple_password |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | C            | complex_password_123!@# |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | C            | complex_password_123!@# |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | C            | complex_password_123!@# |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | C            | complex_password_123!@# |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | C            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      8.000 | 12.500 |
| go              | C            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      8.000 | 12.500 |
| go              | C            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      8.000 | 12.500 |
| go              | C            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      8.000 | 12.500 |
| go              | D            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | D            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | D            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | D            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | D            | simple_password |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | D            | simple_password |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | D            | simple_password |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | D            | simple_password |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | D            | complex_password_123!@# |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | D            | complex_password_123!@# |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | D            | complex_password_123!@# |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | D            | complex_password_123!@# |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | D            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | D            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | D            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | D            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | E            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | E            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | E            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | E            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | E            | simple_password |    2 |       5.000 |       5.000 |     10.000 | 10.000 |
| go              | E            | simple_password |    2 |       5.000 |       5.000 |     10.000 | 10.000 |
| go              | E            | simple_password |    2 |       5.000 |       5.000 |     10.000 | 10.000 |
| go              | E            | simple_password |    2 |       5.000 |       5.000 |     10.000 | 10.000 |
| go              | E            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | E            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | E            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | E            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 |      0 |
| go              | E            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | E            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | E            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | E            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | F            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | F            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | F            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | F            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | F            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | F            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | F            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | F            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | F            | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | F            | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | F            | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | F            | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | F            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | F            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | F            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | F            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | G            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      8.000 |      0 |
| go              | G            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      8.000 |      0 |
| go              | G            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      8.000 |      0 |
| go              | G            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      8.000 |      0 |
| go              | G            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | G            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | G            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | G            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | G            | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | G            | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | G            | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | G            | complex_password_123!@# |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | G            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | G            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | G            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | G            | 🚀🌟🎉 |    2 |       5.000 |       4.000 |     10.000 |      0 |
| go              | H            | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     11.000 |      0 |
| go              | H            | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     11.000 |      0 |
| go              | H            | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     11.000 |      0 |
| go              | H            | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     11.000 |      0 |
| go              | H            | simple_password |    2 |       5.000 |       5.000 |     11.000 |      0 |
| go              | H            | simple_password |    2 |       5.000 |       5.000 |     11.000 |      0 |
| go              | H            | simple_password |    2 |       5.000 |       5.000 |     11.000 |      0 |
| go              | H            | simple_password |    2 |       5.000 |       5.000 |     11.000 |      0 |
| go              | H            | simple_password |    2 |       5.000 |       5.000 |     11.000 |      0 |
| go              | H            | complex_password_123!@# |    3 |       4.000 |       5.000 |      9.000 |      0 |
| go              | H            | complex_password_123!@# |    3 |       4.000 |       5.000 |      9.000 |      0 |
| go              | H            | complex_password_123!@# |    3 |       4.000 |       5.000 |      9.000 |      0 |
| go              | H            | complex_password_123!@# |    3 |       4.000 |       5.000 |      9.000 |      0 |
| go              | H            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | H            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | H            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | H            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | I            | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | I            | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | I            | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | I            | 🚀🌟🎉 |    2 |       5.000 |       5.000 |     10.000 |      0 |
| go              | I            | simple_password |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | I            | simple_password |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | I            | simple_password |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | I            | simple_password |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | I            | complex_password_123!@# |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | I            | complex_password_123!@# |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | I            | complex_password_123!@# |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | I            | complex_password_123!@# |    2 |       5.000 |       4.000 |      9.000 |      0 |
| go              | I            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | I            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | I            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | I            | 🚀🌟🎉 |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | J            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | J            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | J            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | J            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |
| go              | J            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | J            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | J            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | J            | simple_password |    2 |       4.000 |       4.000 |      9.000 |      0 |
| go              | J            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 | 11.100 |
| go              | J            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 | 11.100 |
| go              | J            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 | 11.100 |
| go              | J            | complex_password_123!@# |    2 |       4.000 |       5.000 |      9.000 | 11.100 |
| go              | J            | 🚀🌟🎉 |    2 |       4.000 |       5.000 |     10.000 |      0 |

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
