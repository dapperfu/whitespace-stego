# Test Results Report

**Generated:** 2025-07-01 13:03:05

## Summary

| Metric | Count |
|--------|-------|
| Total Tests | 2552 |
| Passed | 2500 |
| Failed | 52 |
| Skipped | 0 |
| Expected Failures | 0 |
| Unexpected Passes | 0 |
| Total Duration | 0.0ms |

**Success Rate:** 98.0%

## Test Results

### ✅ PASSED (2500)

| Test | Duration |
|------|----------|
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Cover-Hello-python] | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_cli_get_backend_python | 0.0ms |
| tests/test_core.py::test_encode_decode[-None-Hello, World!] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-Cover-Hello] | 0.0ms |
| tests/test_cross_implementation_simple.py::test_python_rust_cross_has_encoded_message | 0.0ms |
| TestCImplementationCoverage::test_c_cli_help | 0.0ms |
| tests/test_cli_simple_coverage.py::test_get_backend_implementation_rust_import_error | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-Cover-Hello] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-Cover-\U0001f600] | 0.0ms |
| tests/test_cross_implementation_simple.py::test_rust_python_cross_has_encoded_message | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-Simple ASCII message] | 0.0ms |
| TestRustBackendCoverage::test_rust_backend_import_success | 0.0ms |
| TestRustBackendCoverage::test_rust_backend_functionality | 0.0ms |
| TestCrossImplementationCoverage::test_python_rust_cross_compatibility | 0.0ms |
| TestCrossImplementationCoverage::test_password_protection_cross_backend | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-Cover-Hello] | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_cli_get_backend_rust_importerror | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_cli_get_backend_c_importerror | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_cli_get_backend_unknown | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_encode_message_unknown_backend | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-Cover-\xa1Hola!] | 0.0ms |
| tests/test_cli_simple_coverage.py::test_get_backend_implementation_c_import_error | 0.0ms |
| tests/test_cli_simple_coverage.py::test_get_backend_implementation_unknown_backend | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-A-Hello] | 0.0ms |
| TestCImplementationCoverage::test_c_cli_encode_help | 0.0ms |
| tests/test_cli_simple_coverage.py::test_cli_main_entry_point | 0.0ms |
| tests/test_core.py::test_encode_decode[-None-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_decode[-None-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_decode_message_unknown_backend | 0.0ms |
| tests/test_cli_and_api_coverage.py::test__decode_python_missing_markers | 0.0ms |
| tests/test_cross_implementation_simple.py::test_python_rust_cross_roundtrip | 0.0ms |
| tests/test_cross_implementation_simple.py::test_python_rust_cross_roundtrip_with_password | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-A-\U0001f600] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCImplementationCoverage::test_c_cli_decode_help | 0.0ms |
| tests/test_core.py::test_encode_decode[-None-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_decode[-None-] | 0.0ms |
| TestErrorHandlingCoverage::test_encode_with_invalid_unicode | 0.0ms |
| TestCImplementationCoverage::test_c_cli_basic_encode_decode | 0.0ms |
| tests/test_cross_implementation_simple.py::test_python_rust_cross_roundtrip_unicode | 0.0ms |
| tests/test_cross_implementation_simple.py::test_message_size_consistency | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-A-\xa1Hola!] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_core.py::test_encode_decode[-simple_password-Hello, World!] | 0.0ms |
| tests/test_cli_and_api_coverage.py::test__decode_python_no_binary | 0.0ms |
| tests/test_cli_and_api_coverage.py::test__decode_python_short_binary | 0.0ms |
| tests/test_cli_and_api_coverage.py::test__decode_python_truncated_message | 0.0ms |
| tests/test_cli_and_api_coverage.py::test__decode_python_corrupted_base64 | 0.0ms |
| tests/test_cli_and_api_coverage.py::test__decode_python_password_xor | 0.0ms |
| tests/test_cli_and_api_coverage.py::test__encode_python_and_decode_python_roundtrip | 0.0ms |
| tests/test_cli_and_api_coverage.py::test__encode_python_carrier_length_one | 0.0ms |
| tests/test_cli_and_api_coverage.py::test__encode_python_carrier_length_greater_than_one | 0.0ms |
| tests/test_cli_and_api_coverage.py::test__encode_python_empty_carrier | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_encode_message_rust_backend | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_cli_verbose_logging | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_cli_main_function | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_core_decode_invalid_password | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_decode_python_skip_non_binary_chars | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_decode_python_general_exception | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_decode_python_password_exception | 0.0ms |
| tests/test_cli_and_api_coverage.py::test_decode_python_password_encode_raises | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-Cover-\U0001f600] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None--Hello] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None--\U0001f600] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None--\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCImplementationCoverage::test_c_cli_file_operations | 0.0ms |
| TestErrorHandlingCoverage::test_decode_with_malformed_data | 0.0ms |
| TestErrorHandlingCoverage::test_binary_encoding_with_special_bytes | 0.0ms |
| TestErrorHandlingCoverage::test_logger_with_special_characters | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-Cover-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cross_implementation_simple.py::test_empty_message_cross_implementation | 0.0ms |
| tests/test_cross_implementation_simple.py::test_empty_carrier_cross_implementation | 0.0ms |
| tests/test_cross_implementation_simple.py::test_implementation_availability | 0.0ms |
| tests/test_core.py::test_encode_decode[-simple_password-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-Hidden-Hello] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-Hidden-\U0001f600] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-Hidden-\xa1Hola!] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_core.py::test_encode_decode[-simple_password-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| TestCImplementationCoverage::test_c_cli_password_protection | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-\U0001f680-Hello] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_python_to_rust[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-Cover-Hello] | 0.0ms |
| tests/test_core.py::test_encode_decode[-simple_password-Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_core.py::test_encode_decode[-simple_password-] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-Cover-\U0001f600] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-Cover-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-Cover-\xa1Hola!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-Cover-\xa1Hola!] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-A-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-A-\U0001f600] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-A-\xa1Hola!] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None--Hello] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None--\U0001f600] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_core.py::test_encode_decode[-complex_password_123!@#-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None--\xa1Hola!] | 0.0ms |
| tests/test_core.py::test_encode_decode[-complex_password_123!@#-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_decode[-complex_password_123!@#-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-A-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-A-Hello] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-Hidden-Hello] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-Hidden-\U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_decode[-complex_password_123!@#-Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--Simple ASCII message] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-Hidden-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-\U0001f680-Hello] | 0.0ms |
| tests/test_core.py::test_encode_decode[-complex_password_123!@#-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_in_memory_roundtrip.py::test_roundtrip_rust_to_python[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_core.py::test_encode_decode[--Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_decode[--Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_decode[--Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-A-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-Simple ASCII message] | 0.0ms |
| tests/test_core.py::test_encode_decode[--Special chars: !@#$%^&*()] | 0.0ms |
| TestCImplementationCoverage::test_c_cli_unicode_support | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_core.py::test_encode_decode[--] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-Numbers: 0123456789] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-A-\U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-None-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-None-Test message with emoji \U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-None-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-None-Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-None-] | 0.0ms |
| TestCImplementationCoverage::test_c_cli_error_handling | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-simple_password-Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-simple_password-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-A-\xa1Hola!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-simple_password-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-simple_password-Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-simple_password-] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-complex_password_123!@#-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-A-\xa1Hola!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-complex_password_123!@#-Test message with emoji \U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-complex_password_123!@#-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-complex_password_123!@#-Special chars: !@#$%^&*()] | 0.0ms |
| TestCImplementationCoverage::test_c_cli_verbose_mode | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text-complex_password_123!@#-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-Hello, World!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None--Hello] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Cover-Hello-rust] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text--Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text--Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text--Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| TestCCrossCompatibility::test_c_python_cross_compatibility | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None--\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-Simple ASCII message] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text--Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None--Hello] | 0.0ms |
| TestCCrossCompatibility::test_c_rust_cross_compatibility | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-Numbers: 0123456789] | 0.0ms |
| tests/test_core.py::test_encode_decode[Simple carrier text--] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-None-Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-None-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-None-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None--\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-None-Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-None-] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-simple_password-Hello, World!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None--\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-simple_password-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-simple_password-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-Hidden-Hello] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-simple_password-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-simple_password-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None--\xa1Hola!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-complex_password_123!@#-Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-complex_password_123!@#-Test message with emoji \U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-Hidden-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-Hidden-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-Hidden-Hello] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-Hidden-\U0001f600] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-complex_password_123!@#-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-complex_password_123!@#-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389-complex_password_123!@#-] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-\U0001f680-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389--Hello, World!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-Hidden-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389--Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389--Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389--Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_decode[Carrier with emoji \U0001f389--] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-None-Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-None-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-None-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-None-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-None-] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-simple_password-Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-simple_password-Test message with emoji \U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-\U0001f680-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-simple_password-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-Hello, World!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-simple_password-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-Cover-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Cover-\U0001f600-python] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-simple_password-] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-complex_password_123!@#-Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-complex_password_123!@#-Test message with emoji \U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-complex_password_123!@#-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-complex_password_123!@#-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d-complex_password_123!@#-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-Cover-\U0001f600] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d--Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d--Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d--Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d--Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_decode[Multilingual carrier: \u4f60\u597d--] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-Cover-Hello] | 0.0ms |
| tests/test_core.py::test_encode_without_password[-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_core.py::test_encode_without_password[-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_without_password[-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_encode_without_password[-Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| tests/test_core.py::test_encode_without_password[-] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Simple carrier text-Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Simple carrier text-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Simple carrier text-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Simple carrier text-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Simple carrier text-] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Carrier with emoji \U0001f389-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Carrier with emoji \U0001f389-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Carrier with emoji \U0001f389-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-Cover-\U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Carrier with emoji \U0001f389-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Carrier with emoji \U0001f389-] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Multilingual carrier: \u4f60\u597d-Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Multilingual carrier: \u4f60\u597d-Test message with emoji \U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-Simple ASCII message] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Multilingual carrier: \u4f60\u597d-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Multilingual carrier: \u4f60\u597d-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_without_password[Multilingual carrier: \u4f60\u597d-] | 0.0ms |
| tests/test_core.py::test_encode_with_password[-Hello, World!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_core.py::test_encode_with_password[-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_encode_with_password[-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_encode_with_password[-Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_core.py::test_encode_with_password[-] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Simple carrier text-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Simple carrier text-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-Cover-\xa1Hola!] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Simple carrier text-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-Cover-\xa1Hola!] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Simple carrier text-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Simple carrier text-] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Carrier with emoji \U0001f389-Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Carrier with emoji \U0001f389-Test message with emoji \U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Carrier with emoji \U0001f389-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Carrier with emoji \U0001f389-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Carrier with emoji \U0001f389-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Multilingual carrier: \u4f60\u597d-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Multilingual carrier: \u4f60\u597d-Test message with emoji \U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Multilingual carrier: \u4f60\u597d-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Multilingual carrier: \u4f60\u597d-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_encode_with_password[Multilingual carrier: \u4f60\u597d-] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_core.py::test_empty_carrier[Hello, World!] | 0.0ms |
| tests/test_core.py::test_empty_carrier[Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_empty_carrier[Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_empty_carrier[Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_empty_carrier[] | 0.0ms |
| tests/test_core.py::test_invalid_decode[] | 0.0ms |
| tests/test_core.py::test_invalid_decode[Simple carrier text] | 0.0ms |
| tests/test_core.py::test_invalid_decode[Carrier with emoji \U0001f389] | 0.0ms |
| tests/test_core.py::test_invalid_decode[Multilingual carrier: \u4f60\u597d] | 0.0ms |
| tests/test_core.py::test_extract_encoded[-Hello, World!] | 0.0ms |
| tests/test_core.py::test_extract_encoded[-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-A-Hello] | 0.0ms |
| tests/test_core.py::test_extract_encoded[-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_extract_encoded[-Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_core.py::test_extract_encoded[-] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Simple carrier text-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Simple carrier text-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Simple carrier text-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Simple carrier text-Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Simple carrier text-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-A-Hello] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-A-\U0001f600] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Carrier with emoji \U0001f389-Hello, World!] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Carrier with emoji \U0001f389-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Carrier with emoji \U0001f389-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Carrier with emoji \U0001f389-Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Carrier with emoji \U0001f389-] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Multilingual carrier: \u4f60\u597d-Hello, World!] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Multilingual carrier: \u4f60\u597d-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--Simple ASCII message] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Multilingual carrier: \u4f60\u597d-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Multilingual carrier: \u4f60\u597d-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_extract_encoded[Multilingual carrier: \u4f60\u597d-] | 0.0ms |
| tests/test_core.py::test_extract_encoded_invalid[] | 0.0ms |
| tests/test_core.py::test_extract_encoded_invalid[Simple carrier text] | 0.0ms |
| tests/test_core.py::test_extract_encoded_invalid[Carrier with emoji \U0001f389] | 0.0ms |
| tests/test_core.py::test_extract_encoded_invalid[Multilingual carrier: \u4f60\u597d] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Cover-\U0001f600-rust] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-A-\xa1Hola!] | 0.0ms |
| tests/test_core.py::test_password_mismatch[None-Hello, World!] | 0.0ms |
| tests/test_core.py::test_password_mismatch[None-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_password_mismatch[None-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_password_mismatch[None-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_password_mismatch[None-] | 0.0ms |
| tests/test_core.py::test_password_mismatch[simple_password-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_core.py::test_password_mismatch[simple_password-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_password_mismatch[simple_password-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_password_mismatch[simple_password-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-A-\U0001f600] | 0.0ms |
| tests/test_core.py::test_password_mismatch[simple_password-] | 0.0ms |
| tests/test_core.py::test_password_mismatch[complex_password_123!@#-Hello, World!] | 0.0ms |
| tests/test_core.py::test_password_mismatch[complex_password_123!@#-Test message with emoji \U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_core.py::test_password_mismatch[complex_password_123!@#-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_password_mismatch[complex_password_123!@#-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_password_mismatch[complex_password_123!@#-] | 0.0ms |
| tests/test_core.py::test_password_mismatch[-Hello, World!] | 0.0ms |
| tests/test_core.py::test_password_mismatch[-Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_password_mismatch[-Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_password_mismatch[-Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_password_mismatch[-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret--Hello] | 0.0ms |
| tests/test_core.py::test_no_carrier_no_password[Hello, World!] | 0.0ms |
| tests/test_core.py::test_no_carrier_no_password[Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_no_carrier_no_password[Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_no_carrier_no_password[Special chars: !@#$%^&*()] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_core.py::test_no_carrier_no_password[] | 0.0ms |
| tests/test_core.py::test_no_carrier_with_password[Hello, World!] | 0.0ms |
| tests/test_core.py::test_no_carrier_with_password[Test message with emoji \U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| tests/test_core.py::test_no_carrier_with_password[Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_no_carrier_with_password[Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_no_carrier_with_password[] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_core.py::test_with_carrier_no_password[Hello, World!] | 0.0ms |
| tests/test_core.py::test_with_carrier_no_password[Test message with emoji \U0001f600] | 0.0ms |
| tests/test_core.py::test_with_carrier_no_password[Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_with_carrier_no_password[Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_with_carrier_no_password[] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-A-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_core.py::test_with_carrier_with_password[Hello, World!] | 0.0ms |
| tests/test_core.py::test_with_carrier_with_password[Test message with emoji \U0001f600] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret--\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_core.py::test_with_carrier_with_password[Multilingual text: \u4f60\u597d, \u4e16\u754c!] | 0.0ms |
| tests/test_core.py::test_with_carrier_with_password[Special chars: !@#$%^&*()] | 0.0ms |
| tests/test_core.py::test_with_carrier_with_password[] | 0.0ms |
| tests/test_core.py::test_has_encoded_message | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Numbers: 0123456789] | 0.0ms |
| tests/test_core.py::test_get_encoded_message_size | 0.0ms |
| tests/test_core.py::test_has_encoded_message_edge_cases | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret--\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-Hidden-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret--Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-Hidden-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret--\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Cover-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-Hidden-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--Numbers: 0123456789] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-Numbers: 0123456789] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret--\xa1Hola!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-\U0001f680-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-\U0001f680-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-\U0001f680-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Simple ASCII message] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[secret-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-Hidden-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-Hidden-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Cover-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-Hidden-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Simple ASCII message] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-A-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-A-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-A-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-\U0001f680-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_rust_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c--Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-\U0001f680-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c--\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Cover-\xa1Hola!-python] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c--\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-\U0001f680-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[secret-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-Simple ASCII message] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Cover-\xa1Hola!-rust] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--Hello, World!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-Cover-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-Cover-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-A-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-Cover-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-A-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-A-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-A-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-A-\xa1Hola!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-A-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512--Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c--Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512--\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c--\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512--\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-Hidden-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c--\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-Hidden-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-Hidden-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-\U0001f680-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-\U0001f680-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--Hello, World!] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-\U0001f680-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-Simple ASCII message] | 0.0ms |
| tests/test_cli_whitespace_stego_rs.py::test_cli_roundtrip_whitespace_stego_rs[\U0001f512-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-A-Hello-python] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-A-Hello-rust] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-Cover-Hello] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_rust_has_encoded_message_with_python_encoded[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Simple carrier-Numbers: 0123456789] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-Cover-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-Cover-\xa1Hola!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-A-\U0001f600-python] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-A-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-A-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-A-\xa1Hola!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-A-\U0001f600-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512--Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512--\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512--\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-A-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-Hidden-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-Hidden-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-Hidden-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-A-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-\U0001f680-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-\U0001f680-\U0001f600] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Simple carrier-Hello, World!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-\U0001f680-\xa1Hola!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_roundtrip[\U0001f512-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-A-\xa1Hola!-python] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-A-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-Hello-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-Hello-python-c-cli] | 0.0ms |
| TestCrossImplementationHasEncodedMessage::test_has_encoded_message_with_plain_text | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-Hello-rust-cli-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-Hello-rust-cli-rust-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-Hello-rust-cli-c-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-Hello-c-cli-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[None-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-Hello-c-cli-rust-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-Hello-c-cli-c-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\U0001f600-python-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None--Hello-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\U0001f600-python-rust-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[simple_password-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None--Hello-rust] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\U0001f600-python-c-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\U0001f600-rust-cli-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None--\U0001f600-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[password_with_special_chars!@#$%-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-Numbers: 0123456789] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\U0001f600-rust-cli-rust-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\U0001f600-rust-cli-c-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\U0001f600-c-cli-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\U0001f600-c-cli-rust-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--Simple ASCII message] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\U0001f600-c-cli-c-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None--\U0001f600-rust] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[Unicode password: \u5bc6\u7801-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Simple carrier-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Carrier with spaces and punctuation!-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u3053\u3093\u306b\u3061\u306f-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None--\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Unicode carrier: \u4f60\u597d\u4e16\u754c-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u3053\u3093\u306b\u3061\u306f-python-c-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Single char: A-Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u4f60\u597d\uff0c\u4e16\u754c\uff01] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None--\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \uc548\ub155\ud558\uc138\uc694, \uc138\uacc4!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u041f\u0440\u0438\u0432\u0435\u0442, \u043c\u0438\u0440!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Unicode: \u0645\u0631\u062d\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_rust_cross_roundtrip[very_long_password_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-Very long carrier: carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text carrier text -Very long message: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u3053\u3093\u306b\u3061\u306f-rust-cli-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u3053\u3093\u306b\u3061\u306f-rust-cli-rust-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u3053\u3093\u306b\u3061\u306f-rust-cli-c-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u3053\u3093\u306b\u3061\u306f-c-cli-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None--\xa1Hola!-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u3053\u3093\u306b\u3061\u306f-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u3053\u3093\u306b\u3061\u306f-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None--\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\xa1Hola!-python-rust-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[None-Simple carrier-Hello, World!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None--\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[None-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[None-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\xa1Hola!-python-c-cli] | 0.0ms |
| TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[None-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[None-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[None-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\xa1Hola!-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None--\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Simple carrier-Simple ASCII message] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[None-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Simple carrier-Hello, World!] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Simple carrier-Simple ASCII message] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\xa1Hola!-rust-cli-rust-cli] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Simple carrier-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Simple carrier-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\xa1Hola!-rust-cli-c-cli] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Carrier with spaces and punctuation!-Hello, World!] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Carrier with spaces and punctuation!-Simple ASCII message] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Carrier with spaces and punctuation!-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\xa1Hola!-c-cli-python] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_consistency[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#] | 0.0ms |
| TestCrossImplementationMessageSize::test_message_size_with_no_message | 0.0ms |
| TestCrossImplementationEdgeCases::test_empty_message_all_implementations | 0.0ms |
| TestCrossImplementationEdgeCases::test_empty_carrier_all_implementations | 0.0ms |
| TestCrossImplementationEdgeCases::test_single_character_carrier_all_implementations | 0.0ms |
| TestCrossImplementationEdgeCases::test_very_long_messages | 0.0ms |
| tests/test_cross_implementation.py::test_implementation_availability | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\xa1Hola!-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\xa1Hola!-c-cli-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Hidden-Hello-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Hidden-Hello-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-python-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Hidden-\U0001f600-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Hidden-\U0001f600-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Hidden-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-Hello-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Hidden-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-Hello-python-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-Hello-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Hidden-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-Hello-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-Hello-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-Hello-c-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-Hello-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Hidden-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-Hello-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\U0001f600-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\U0001f600-python-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\U0001f600-rust-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\U0001f600-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\U0001f600-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\U0001f600-c-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-\U0001f680-Hello-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\U0001f600-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\U0001f600-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-\U0001f680-Hello-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u3053\u3093\u306b\u3061\u306f-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-\U0001f680-\U0001f600-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u3053\u3093\u306b\u3061\u306f-python-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u3053\u3093\u306b\u3061\u306f-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-\U0001f680-\U0001f600-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u3053\u3093\u306b\u3061\u306f-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u3053\u3093\u306b\u3061\u306f-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u3053\u3093\u306b\u3061\u306f-c-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u3053\u3093\u306b\u3061\u306f-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u3053\u3093\u306b\u3061\u306f-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\xa1Hola!-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\xa1Hola!-python-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-\U0001f680-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\xa1Hola!-rust-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\xa1Hola!-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\xa1Hola!-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-\U0001f680-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\xa1Hola!-c-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\xa1Hola!-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\xa1Hola!-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-python-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Cover-Hello-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Cover-Hello-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Cover-\U0001f600-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--Hello-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--Hello-python-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--Hello-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Cover-\U0001f600-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--Hello-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--Hello-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--Hello-c-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Cover-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--Hello-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--Hello-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Cover-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\U0001f600-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\U0001f600-python-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Cover-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\U0001f600-rust-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\U0001f600-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\U0001f600-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\U0001f600-c-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Cover-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\U0001f600-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\U0001f600-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u3053\u3093\u306b\u3061\u306f-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u3053\u3093\u306b\u3061\u306f-python-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u3053\u3093\u306b\u3061\u306f-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-A-Hello-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u3053\u3093\u306b\u3061\u306f-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u3053\u3093\u306b\u3061\u306f-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u3053\u3093\u306b\u3061\u306f-c-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u3053\u3093\u306b\u3061\u306f-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u3053\u3093\u306b\u3061\u306f-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-A-Hello-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\xa1Hola!-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-A-\U0001f600-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\xa1Hola!-python-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\xa1Hola!-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-A-\U0001f600-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\xa1Hola!-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\xa1Hola!-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\xa1Hola!-c-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\xa1Hola!-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\xa1Hola!-c-cli-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-A-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u041f\u0440\u0438\u0432\u0435\u0442-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-A-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u041f\u0440\u0438\u0432\u0435\u0442-python-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-A-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-A-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None--\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-A-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-Hello-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-Hello-python-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-A-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-Hello-rust-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-Hello-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-Hello-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-Hello-c-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret--Hello-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-Hello-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-Hello-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret--Hello-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\U0001f600-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\U0001f600-python-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret--\U0001f600-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\U0001f600-rust-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\U0001f600-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\U0001f600-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret--\U0001f600-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\U0001f600-c-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\U0001f600-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\U0001f600-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret--\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u3053\u3093\u306b\u3061\u306f-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u3053\u3093\u306b\u3061\u306f-python-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret--\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u3053\u3093\u306b\u3061\u306f-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret--\xa1Hola!-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u3053\u3093\u306b\u3061\u306f-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u3053\u3093\u306b\u3061\u306f-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u3053\u3093\u306b\u3061\u306f-c-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u3053\u3093\u306b\u3061\u306f-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u3053\u3093\u306b\u3061\u306f-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret--\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\xa1Hola!-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret--\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\xa1Hola!-python-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\xa1Hola!-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret--\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\xa1Hola!-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\xa1Hola!-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\xa1Hola!-c-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\xa1Hola!-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\xa1Hola!-c-cli-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Hidden-Hello-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Hidden-Hello-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-python-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Hidden-\U0001f600-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Hidden-\U0001f600-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Hidden-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-Hello-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-Hello-python-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Hidden-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-Hello-rust-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-Hello-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-Hello-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-Hello-c-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Hidden-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-Hello-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-Hello-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Hidden-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\U0001f600-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\U0001f600-python-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\U0001f600-rust-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\U0001f600-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\U0001f600-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\U0001f600-c-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\U0001f600-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\U0001f600-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-\U0001f680-Hello-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-python-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-python-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-\U0001f680-Hello-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-\U0001f680-\U0001f600-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-c-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-\U0001f680-\U0001f600-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\xa1Hola!-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-\U0001f680-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\xa1Hola!-python-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\xa1Hola!-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-\U0001f680-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\xa1Hola!-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\xa1Hola!-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\xa1Hola!-c-cli-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\xa1Hola!-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\xa1Hola!-c-cli-c-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-\U0001f680-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-\U0001f680-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-python-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[secret-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-rust-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_cross_tool_roundtrip_with_c[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-c-cli-c-cli] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-Cover-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-Cover-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-Cover-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-A-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-A-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-A-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None--Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None--\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None--\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-Hidden-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-Hidden-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-Hidden-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-\U0001f680-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-Hello-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-Cover-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-Cover-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-Cover-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-A-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-A-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-A-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-Hello-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret--Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret--\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret--\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-Hidden-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-Hidden-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-Hidden-\xa1Hola!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\U0001f600-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-\U0001f680-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[secret-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\U0001f600-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-A-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-A-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-A-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c--Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c--\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c--\xa1Hola!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-Cover-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-Cover-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-Cover-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-A-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-A-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-A-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512--Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512--\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512--\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-Hidden-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-Hidden-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-Hidden-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-\U0001f680-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_verbose_output[\U0001f512-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-Cover-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-Cover-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-Cover-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-A-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-A-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-A-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None--Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None--\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None--\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-Hidden-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-Hidden-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-Hidden-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-\U0001f680-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-Cover-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-Cover-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-Cover-\xa1Hola!] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-A-Hello-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-A-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-A-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-A-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret--Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret--\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret--\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-Hidden-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-Hidden-\U0001f600] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-A-Hello-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-Hidden-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-\U0001f680-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[secret-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-A-\U0001f600-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-A-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-A-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-A-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c--Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c--\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c--\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-A-\U0001f600-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-Cover-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-Cover-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-Cover-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-Cover-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-Cover-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-A-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-A-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-A-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-A-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-A-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512--Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512--\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512--\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512--\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512--\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-Hidden-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-Hidden-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-Hidden-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-Hidden-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-\U0001f680-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-\U0001f680-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-\U0001f680-\u3053\u3093\u306b\u3061\u306f] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-A-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-\U0001f680-\xa1Hola!] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_error_handling[\U0001f512-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_help_output | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_output_consistency[Cover-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_output_consistency[Cover-\U0001f600] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_output_consistency[A-Hello] | 0.0ms |
| tests/test_cli_c_coverage.py::test_c_cli_output_consistency[A-\U0001f600] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-A-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-A-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c--Hello-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c--Hello-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c--\U0001f600-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c--\U0001f600-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c--\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c--\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c--\xa1Hola!-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c--\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c--\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c--\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-Hello-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-Hello-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\U0001f600-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\U0001f600-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-Hello-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-Hello-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\U0001f600-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\U0001f600-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\u043f\u0430\u0440\u043e\u043b\u044c-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Cover-Hello-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Cover-Hello-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Cover-\U0001f600-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Cover-\U0001f600-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Cover-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Cover-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Cover-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Cover-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-A-Hello-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-A-Hello-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-A-\U0001f600-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-A-\U0001f600-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-A-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-A-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-A-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-A-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-A-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-A-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512--Hello-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512--Hello-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512--\U0001f600-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512--\U0001f600-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512--\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512--\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512--\xa1Hola!-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512--\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512--\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512--\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Hidden-Hello-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Hidden-Hello-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Hidden-\U0001f600-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Hidden-\U0001f600-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Hidden-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Hidden-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Hidden-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Hidden-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-\U0001f680-Hello-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-\U0001f680-Hello-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-\U0001f680-\U0001f600-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-\U0001f680-\U0001f600-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-\U0001f680-\u3053\u3093\u306b\u3061\u306f-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-\U0001f680-\u3053\u3093\u306b\u3061\u306f-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-\U0001f680-\xa1Hola!-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-\U0001f680-\xa1Hola!-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_roundtrip_whitespace_stego[\U0001f512-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-Hello-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-Hello-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-Hello-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\U0001f600-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\U0001f600-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\U0001f600-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\u3053\u3093\u306b\u3061\u306f-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\u3053\u3093\u306b\u3061\u306f-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\u3053\u3093\u306b\u3061\u306f-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\xa1Hola!-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\xa1Hola!-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\xa1Hola!-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-Hello-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-Hello-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-Hello-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\U0001f600-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\U0001f600-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\U0001f600-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\u3053\u3093\u306b\u3061\u306f-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\u3053\u3093\u306b\u3061\u306f-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\u3053\u3093\u306b\u3061\u306f-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\xa1Hola!-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\xa1Hola!-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\xa1Hola!-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--Hello-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--Hello-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--Hello-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\U0001f600-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\U0001f600-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\U0001f600-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\u3053\u3093\u306b\u3061\u306f-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\u3053\u3093\u306b\u3061\u306f-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\u3053\u3093\u306b\u3061\u306f-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\xa1Hola!-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\xa1Hola!-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\xa1Hola!-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\u041f\u0440\u0438\u0432\u0435\u0442-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\u041f\u0440\u0438\u0432\u0435\u0442-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None--\u041f\u0440\u0438\u0432\u0435\u0442-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-Hello-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-Hello-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-Hello-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\U0001f600-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\U0001f600-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\U0001f600-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\u3053\u3093\u306b\u3061\u306f-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\u3053\u3093\u306b\u3061\u306f-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\u3053\u3093\u306b\u3061\u306f-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\xa1Hola!-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\xa1Hola!-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\xa1Hola!-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-Hello-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-Hello-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-Hello-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\U0001f600-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\U0001f600-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\U0001f600-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\xa1Hola!-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\xa1Hola!-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\xa1Hola!-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-rust-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_backend_roundtrip[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-rust-rust] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-Hello-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-Hello-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-Hello-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\U0001f600-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\U0001f600-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\U0001f600-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\u3053\u3093\u306b\u3061\u306f-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\u3053\u3093\u306b\u3061\u306f-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\u3053\u3093\u306b\u3061\u306f-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\xa1Hola!-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\xa1Hola!-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\xa1Hola!-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Cover-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-Hello-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-Hello-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-Hello-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\U0001f600-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\U0001f600-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\U0001f600-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\u3053\u3093\u306b\u3061\u306f-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\u3053\u3093\u306b\u3061\u306f-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\u3053\u3093\u306b\u3061\u306f-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\xa1Hola!-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\xa1Hola!-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\xa1Hola!-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-A-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--Hello-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--Hello-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--Hello-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\U0001f600-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\U0001f600-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\U0001f600-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\u3053\u3093\u306b\u3061\u306f-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\u3053\u3093\u306b\u3061\u306f-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\u3053\u3093\u306b\u3061\u306f-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\xa1Hola!-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\xa1Hola!-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\xa1Hola!-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\u041f\u0440\u0438\u0432\u0435\u0442-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None--\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-Hello-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-Hello-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-Hello-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\U0001f600-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\U0001f600-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\U0001f600-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\u3053\u3093\u306b\u3061\u306f-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\u3053\u3093\u306b\u3061\u306f-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\u3053\u3093\u306b\u3061\u306f-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\xa1Hola!-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\xa1Hola!-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\xa1Hola!-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-Hidden-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-Hello-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-Hello-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-Hello-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-Hello-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\U0001f600-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\U0001f600-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\U0001f600-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\U0001f600-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\u3053\u3093\u306b\u3061\u306f-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\xa1Hola!-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\xa1Hola!-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\xa1Hola!-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\xa1Hola!-rust-cli-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-python-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-python-rust-cli] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-python] | 0.0ms |
| tests/test_cli_whitespace_stego.py::test_cli_cross_tool_roundtrip[None-\U0001f680-\u041f\u0440\u0438\u0432\u0435\u0442-rust-cli-rust-cli] | 0.0ms |

### ❌ FAILED (52)

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Simple carrier-Hello, World!]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'S\u200b\u200d\ufeff\ufeff\u200d\ufeff\ufeff\ufeff\u200d\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\u200d\u200d\ufeff\u...00d\u200d\ufeff\u200d\u200d\ufeff\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\u200cimple carrier'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'nDZR9KNFKf7crkc6R5vBr+joY+TRE7/+cDwpN0NV1K2lx2/efnh/znIlnbI0'

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d882e70>
message = 'Hello, World!', carrier = 'Simple carrier', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'S\u200b\u200d\ufeff\ufeff\u200d\ufeff\ufeff\ufeff\u200d\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\u200d\u200d\ufeff\u...00d\u200d\ufeff\u200d\u200d\ufeff\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\u200cimple carrier'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Simple carrier-Simple ASCII message]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'S\u200b\u200d\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u...eff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'POA40EqYByx++XnsGgBLvDlIM/38MZvai1o3d8b3b9LS6FHZRt/26GtgkGJXa4U4bbS9lQ=='

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d882f30>
message = 'Simple ASCII message', carrier = 'Simple carrier', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'S\u200b\u200d\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u...eff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\u200d\u200d\u200d\u...eff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'bR5da+rL5EHmbYDW/XYHUNoCc/3ce8UKkD5wjV7QSl9ZK5rjxVqaNpdVro2yhpJq7A50LRenUGB2z0Xb66ruAbPLu91uT50Wvnol7A=='

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d882ff0>
message = 'Special chars: !@#$%^&*()_+-=[]{}|;\':",./<>?', carrier = 'Simple carrier'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\u200d\u200d\u200d\u...eff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Simple carrier-Numbers: 0123456789]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'S\u200b\u200d\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\u200d\ufeff\u200d\ufeff\u...eff\u200d\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\u200d\u200cimple carrier'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'3ML4aD6l461Y4bjCkRR9vbtJj27tlAdGEOTRgjDkO9ajUvOMksKHkTgpy6wbXmY63y3X'

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8830b0>
message = 'Numbers: 0123456789', carrier = 'Simple carrier', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'S\u200b\u200d\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\u200d\ufeff\u200d\ufeff\u...eff\u200d\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\u200d\u200cimple carrier'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Simple carrier-Mixed case: Hello World 123 !@#]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'S\u200b\u200d\ufeff\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...00d\u200d\ufeff\ufeff\ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\u200cimple carrier'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'QABzhdbit5BvIVxIkATjHSKw+xFuEEgDiwwN4j0mOmmlGrtC86PQP40LuFfamF4FR8aWfTxprTnSkOJKYBqN'

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d883170>
message = 'Mixed case: Hello World 123 !@#', carrier = 'Simple carrier'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'S\u200b\u200d\ufeff\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...00d\u200d\ufeff\ufeff\ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\u200cimple carrier'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Carrier with spaces and punctuation!-Hello, World!]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'C\u200b\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\u...ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'XL9g3uPFasXTLD5+2R9d2n4vYR2dzSk+g889r+1HzZj3/HLZmKETkSdd7cQe'

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d883230>
message = 'Hello, World!', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'C\u200b\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\u...ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Carrier with spaces and punctuation!-Simple ASCII message]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'C\u200b\u200d\ufeff\ufeff\ufeff\u200d\ufeff\ufeff\u200d\u200d\ufeff\u200d\u200d\u200d\ufeff\ufeff\ufeff\u200d\u200d\u...ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'vG/ya0WyhZmjOab8S1OTnPpGeH3Na/VqZmNJ/IKi9k1f8Ns+LrAMNOhfa1hjnnTPCsdH2Q=='

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8832f0>
message = 'Simple ASCII message', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'C\u200b\u200d\ufeff\ufeff\ufeff\u200d\ufeff\ufeff\u200d\u200d\ufeff\u200d\u200d\u200d\ufeff\ufeff\ufeff\u200d\u200d\u...ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'C\u200b\u200d\ufeff\ufeff\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\u200d\ufeff\ufeff\u200d\ufeff\u...ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'jsPa7UM7wcw2msOX3/NPfB3UXbRHo8nlPfRdjTmRrzQn+jPKr+8ev44Mf1VN849k3VTdo46m7bh1MEnEUSSoGS120LBuekIg7maMFg=='

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8833b0>
message = 'Special chars: !@#$%^&*()_+-=[]{}|;\':",./<>?'
carrier = 'Carrier with spaces and punctuation!', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'C\u200b\u200d\ufeff\ufeff\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\u200d\ufeff\ufeff\u200d\ufeff\u...ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Carrier with spaces and punctuation!-Numbers: 0123456789]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'C\u200b\u200d\ufeff\u200d\ufeff\u200d\ufeff\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\u...ufeff\u200d\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\u200d\ufeff\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'UK1GVOq34JdlqZ4PYYIGnfGpK4euI+8x5dMpoMrDEDKv7fFQGPyKUZsaG7jjnovAEG2+'

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d883470>
message = 'Numbers: 0123456789', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'C\u200b\u200d\ufeff\u200d\ufeff\u200d\ufeff\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\u...ufeff\u200d\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\u200d\ufeff\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'C\u200b\u200d\ufeff\u200d\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u...u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'GOIVy+we91ZSykdanPNXDFbOIQMZNHT/Il7dFEYk2upVmvbmlhZjr5NlDIw+0q4gC3ympaOCeosjkGNX2y/i'

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d883530>
message = 'Mixed case: Hello World 123 !@#', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'C\u200b\u200d\ufeff\u200d\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u...u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'U\u200b\u200d\ufeff\u200d\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\u200d\ufeff\u200d\u200d\u...0d\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\ufeff\u200d\u200d\ufeff\u200d\u200d\u200cnicode carrier: 你好世界'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'BM2baJ6MIDfSZH2BICVb97d0g0aRy4yQTe1Tn9dZVPBrS64IBE+ZHFvMz0Pd'

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8835f0>
message = 'Hello, World!', carrier = 'Unicode carrier: 你好世界', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'U\u200b\u200d\ufeff\u200d\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\u200d\ufeff\u200d\u200d\u...0d\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\ufeff\u200d\u200d\ufeff\u200d\u200d\u200cnicode carrier: 你好世界'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'U\u200b\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'XahTOLRl3wVcvZaoG0X2KgzHXnTlIwGF/Zn6SXoSBfdvnGJU89c4qM6x/UIsDlr4s62PdA=='

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8836b0>
message = 'Simple ASCII message', carrier = 'Unicode carrier: 你好世界', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'U\u200b\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'U\u200b\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\ufeff\u...0d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'EXxNHuCihORGlRsKLbJsmUFADV5onucV1S99zQLter9gWKWyr7i9sEWchWdfwLzHHkFS/fPtFMZRKpzW1KlBXAcUGIZA4ze9fFEFbA=='

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d883770>
message = 'Special chars: !@#$%^&*()_+-=[]{}|;\':",./<>?', carrier = 'Unicode carrier: 你好世界'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'U\u200b\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\ufeff\u...0d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <cryptography.fernet.Fernet object at 0x7a061e39b980>
data = b'\x80\x9b!8l\xd4\x8d6\xd9\x0c=\xda\xaaOS\x1f3|\xea\xa24\xe2\xb1\r\x87\x9b\xb8\x01>n\xedrh\x1eN\xbbE\x15\xc9\xcaV\xdb\xae\xaa\xa3\xe6\x14\xc9\xbf\xd4\xc2'

    def _verify_signature(self, data: bytes) -> None:
        h = HMAC(self._signing_key, hashes.SHA256())
        h.update(data[:-32])
        try:
>           h.verify(data[-32:])
E           cryptography.exceptions.InvalidSignature: Signature did not match digest.

.venv/lib/python3.12/site-packages/cryptography/fernet.py:131: InvalidSignature

During handling of the above exception, another exception occurred:

carrier = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\u...0d\ufeff\u200d\ufeff\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\u200d\u200d\u200d\ufeff\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:90: in decrypt
    return self._decrypt_data(data, timestamp, time_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.12/site-packages/cryptography/fernet.py:149: in _decrypt_data
    self._verify_signature(data)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <cryptography.fernet.Fernet object at 0x7a061e39b980>
data = b'\x80\x9b!8l\xd4\x8d6\xd9\x0c=\xda\xaaOS\x1f3|\xea\xa24\xe2\xb1\r\x87\x9b\xb8\x01>n\xedrh\x1eN\xbbE\x15\xc9\xcaV\xdb\xae\xaa\xa3\xe6\x14\xc9\xbf\xd4\xc2'

    def _verify_signature(self, data: bytes) -> None:
        h = HMAC(self._signing_key, hashes.SHA256())
        h.update(data[:-32])
        try:
            h.verify(data[-32:])
        except InvalidSignature:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:133: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d883830>
message = 'Numbers: 0123456789', carrier = 'Unicode carrier: 你好世界', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\u...0d\ufeff\u200d\ufeff\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\u200d\u200d\u200d\ufeff\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_python_has_encoded_message_with_c_encoded[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

carrier = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\u200d\ufeff\u200d\ufeff\ufeff\ufeff\u200d\u200d\u200d\u200d\u200d\u200d\u...0d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\u200cnicode carrier: 你好世界'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
>               data = f.decrypt(data)
                       ^^^^^^^^^^^^^^^

whitespace_stego/core.py:155: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.12/site-packages/cryptography/fernet.py:85: in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

token = b'ep1dLaY3KPfcJIopMbG7LWw8Ido8CmMUvcamyOoeSKdAAXrE+kyktgDDvVgBMg0LbCrMrPQthHaf+w2x1GtN'

    @staticmethod
    def _get_unverified_token_data(token: bytes | str) -> tuple[int, bytes]:
        if not isinstance(token, (str, bytes)):
            raise TypeError("token must be bytes or str")
    
        try:
            data = base64.urlsafe_b64decode(token)
        except (TypeError, binascii.Error):
            raise InvalidToken
    
        if not data or data[0] != 0x80:
>           raise InvalidToken
E           cryptography.fernet.InvalidToken

.venv/lib/python3.12/site-packages/cryptography/fernet.py:119: InvalidToken

During handling of the above exception, another exception occurred:

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8838f0>
message = 'Mixed case: Hello World 123 !@#', carrier = 'Unicode carrier: 你好世界'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_has_encoded_message_with_c_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test Python has_encoded_message with C-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with C
        c_encoded = run_c_binary_encode(message, carrier, password)
    
        # Check with Python has_encoded_message
        assert py_has_encoded_message(c_encoded), f"Python failed to detect C-encoded message: {message}"
    
        # Verify the message can be decoded
>       decoded = py_decode(c_encoded, password)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

carrier = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\u200d\ufeff\u200d\ufeff\ufeff\ufeff\u200d\u200d\u200d\u200d\u200d\u200d\u...0d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\u200cnicode carrier: 你好世界'
password = 'test_password'

    def decode(carrier: str, password: Optional[str] = None) -> str:
        """Decode a message from carrier text containing zero-width characters.
    
        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            Optional password for decryption.
    
        Returns
        -------
        str
            The decoded message.
    
        Raises
        ------
        ValueError
            If no valid message is found in the carrier text.
        """
        logger.debug("Decoding message from text: %s", carrier)
        if password:
            logger.debug("Using password protection")
    
        # Find the encoded message between markers
        start = carrier.find(START_MARKER)
        end = carrier.find(END_MARKER)
    
        if start == -1 or end == -1:
            raise ValueError("No valid message found in carrier text")
    
        # Extract the encoded message
        encoded = carrier[start + 1 : end]
    
        # Convert from zero-width characters to bytes
        data = _decode_binary(encoded)
    
        # Decrypt if password provided
        if password:
            from cryptography.fernet import Fernet, InvalidToken
    
            key = base64.urlsafe_b64encode(password.encode("utf-8").ljust(32)[:32])
            f = Fernet(key)
            try:
                data = f.decrypt(data)
            except InvalidToken:
>               raise ValueError("Invalid password or corrupted data")
E               ValueError: Invalid password or corrupted data

whitespace_stego/core.py:157: ValueError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Simple carrier-Hello, World!]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b4c80>
message = 'Hello, World!', carrier = 'Simple carrier', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...00d\u200d\ufeff\ufeff\u200d\ufeff\ufeff\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Simple carrier-Simple ASCII message]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b4d40>
message = 'Simple ASCII message', carrier = 'Simple carrier', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...00d\u200d\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b4e00>
message = 'Special chars: !@#$%^&*()_+-=[]{}|;\':",./<>?', carrier = 'Simple carrier'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...eff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Simple carrier-Numbers: 0123456789]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b4ec0>
message = 'Numbers: 0123456789', carrier = 'Simple carrier', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...eff\u200d\ufeff\ufeff\ufeff\u200d\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Simple carrier-Mixed case: Hello World 123 !@#]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b4f80>
message = 'Mixed case: Hello World 123 !@#', carrier = 'Simple carrier'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...eff\u200d\ufeff\u200d\u200d\u200d\ufeff\ufeff\u200d\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Carrier with spaces and punctuation!-Hello, World!]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b5040>
message = 'Hello, World!', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...u200d\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Carrier with spaces and punctuation!-Simple ASCII message]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b5100>
message = 'Simple ASCII message', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...u200d\u200d\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b51c0>
message = 'Special chars: !@#$%^&*()_+-=[]{}|;\':",./<>?'
carrier = 'Carrier with spaces and punctuation!', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Carrier with spaces and punctuation!-Numbers: 0123456789]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b5280>
message = 'Numbers: 0123456789', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b5340>
message = 'Mixed case: Hello World 123 !@#', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...u200d\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\u200d\u200d\u200d\u200d\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b5400>
message = 'Hello, World!', carrier = 'Unicode carrier: 你好世界', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\ufeff\u200d\ufeff\ufeff\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b54c0>
message = 'Simple ASCII message', carrier = 'Unicode carrier: 你好世界', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b5580>
message = 'Special chars: !@#$%^&*()_+-=[]{}|;\':",./<>?', carrier = 'Unicode carrier: 你好世界'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b5640>
message = 'Numbers: 0123456789', carrier = 'Unicode carrier: 你好世界', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Decryption failed: wrong password or corrupted data

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_c_has_encoded_message_with_python_encoded[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b5700>
message = 'Mixed case: Hello World 123 !@#', carrier = 'Unicode carrier: 你好世界'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_c_has_encoded_message_with_python_encoded(self, message: str, carrier: str, password: Optional[str]):
        """Test C has_encoded_message with Python-encoded messages."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Encode with Python
        py_encoded = py_encode(message, carrier, password)
    
        # Decode with C to verify it can read Python-encoded messages
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:246: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\ufeff\u200d\u200d\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200cnicode carrier: 你好世界'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationHasEncodedMessage::test_has_encoded_message_with_partial_markers** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationHasEncodedMessage object at 0x7a061d8b57c0>

    def test_has_encoded_message_with_partial_markers(self):
        """Test has_encoded_message with partial markers (should return False)."""
        partial_marker_texts = [
            "Text with start\u200b",  # Only start marker
            "Text with end\u200c",    # Only end marker
            "Start\u200b middle end\u200c",  # Wrong order
        ]
    
        for text in partial_marker_texts:
>           assert not py_has_encoded_message(text), f"False positive for partial markers: {text}"
E           AssertionError: False positive for partial markers: Start​ middle end‌
E           assert not True
E            +  where True = py_has_encoded_message('Start\u200b middle end\u200c')

tests/test_cross_implementation.py:271: AssertionError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Simple carrier-Hello, World!]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d82f0>
message = 'Hello, World!', carrier = 'Simple carrier', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...00d\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Simple carrier-Simple ASCII message]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d83b0>
message = 'Simple ASCII message', carrier = 'Simple carrier', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...00d\u200d\ufeff\u200d\u200d\ufeff\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d8470>
message = 'Special chars: !@#$%^&*()_+-=[]{}|;\':",./<>?', carrier = 'Simple carrier'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...eff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Simple carrier-Numbers: 0123456789]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d8530>
message = 'Numbers: 0123456789', carrier = 'Simple carrier', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...eff\u200d\ufeff\ufeff\ufeff\u200d\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Simple carrier-Mixed case: Hello World 123 !@#]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d85f0>
message = 'Mixed case: Hello World 123 !@#', carrier = 'Simple carrier'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...00d\u200d\ufeff\u200d\ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\u200d\ufeff\u200d\u200d\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Carrier with spaces and punctuation!-Hello, World!]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d86b0>
message = 'Hello, World!', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...u200d\u200d\ufeff\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Carrier with spaces and punctuation!-Simple ASCII message]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d8770>
message = 'Simple ASCII message', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...ufeff\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d8830>
message = 'Special chars: !@#$%^&*()_+-=[]{}|;\':",./<>?'
carrier = 'Carrier with spaces and punctuation!', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Carrier with spaces and punctuation!-Numbers: 0123456789]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d88f0>
message = 'Numbers: 0123456789', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Carrier with spaces and punctuation!-Mixed case: Hello World 123 !@#]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d89b0>
message = 'Mixed case: Hello World 123 !@#', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...u200d\ufeff\u200d\u200d\u200d\u200d\ufeff\ufeff\u200d\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Hello, World!]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d8a70>
message = 'Hello, World!', carrier = 'Unicode carrier: 你好世界', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\ufeff\u200d\u200d\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Simple ASCII message]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d8b30>
message = 'Simple ASCII message', carrier = 'Unicode carrier: 你好世界', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\ufeff\u200d\ufeff\u200d\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d8bf0>
message = 'Special chars: !@#$%^&*()_+-=[]{}|;\':",./<>?', carrier = 'Unicode carrier: 你好世界'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Numbers: 0123456789]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d8cb0>
message = 'Numbers: 0123456789', carrier = 'Unicode carrier: 你好世界', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\ufeff\ufeff\ufeff\u200d\ufeff\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_python_c_cross_roundtrip[test_password-Unicode carrier: \u4f60\u597d\u4e16\u754c-Mixed case: Hello World 123 !@#]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d8d70>
message = 'Mixed case: Hello World 123 !@#', carrier = 'Unicode carrier: 你好世界'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:5])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_python_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Python <-> C cross round trip."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        # Python encode -> C decode
        py_encoded = py_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(py_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:305: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'U\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...0d\ufeff\u200d\ufeff\u200d\ufeff\u200d\ufeff\u200d\ufeff\ufeff\u200d\ufeff\ufeff\u200d\ufeff\u200cnicode carrier: 你好世界'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[test_password-Simple carrier-Hello, World!]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d9730>
message = 'Hello, World!', carrier = 'Simple carrier', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:2])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_rust_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Rust <-> C cross round trip."""
        if not RUST_AVAILABLE or not C_AVAILABLE:
            pytest.skip("Rust backend or C binary not available")
    
        # Rust encode -> C decode
        rust_encoded = rust_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(rust_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:323: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...eff\u200d\ufeff\ufeff\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[test_password-Simple carrier-Simple ASCII message]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d97f0>
message = 'Simple ASCII message', carrier = 'Simple carrier', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:2])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_rust_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Rust <-> C cross round trip."""
        if not RUST_AVAILABLE or not C_AVAILABLE:
            pytest.skip("Rust backend or C binary not available")
    
        # Rust encode -> C decode
        rust_encoded = rust_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(rust_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:323: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...eff\u200d\ufeff\u200d\ufeff\ufeff\u200d\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[test_password-Simple carrier-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d98b0>
message = 'Special chars: !@#$%^&*()_+-=[]{}|;\':",./<>?', carrier = 'Simple carrier'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:2])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_rust_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Rust <-> C cross round trip."""
        if not RUST_AVAILABLE or not C_AVAILABLE:
            pytest.skip("Rust backend or C binary not available")
    
        # Rust encode -> C decode
        rust_encoded = rust_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(rust_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:323: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'S\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...eff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200cimple carrier'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[test_password-Carrier with spaces and punctuation!-Hello, World!]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d9970>
message = 'Hello, World!', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:2])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_rust_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Rust <-> C cross round trip."""
        if not RUST_AVAILABLE or not C_AVAILABLE:
            pytest.skip("Rust backend or C binary not available")
    
        # Rust encode -> C decode
        rust_encoded = rust_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(rust_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:323: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...u200d\u200d\ufeff\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[test_password-Carrier with spaces and punctuation!-Simple ASCII message]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d9a30>
message = 'Simple ASCII message', carrier = 'Carrier with spaces and punctuation!'
password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:2])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_rust_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Rust <-> C cross round trip."""
        if not RUST_AVAILABLE or not C_AVAILABLE:
            pytest.skip("Rust backend or C binary not available")
    
        # Rust encode -> C decode
        rust_encoded = rust_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(rust_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:323: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...u200d\u200d\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

**TestCrossImplementationRoundTrip::test_rust_c_cross_roundtrip[test_password-Carrier with spaces and punctuation!-Special chars: !@#$%^&*()_+-=[]{}|;':",./<>?]** (0.0ms)

```
[gw0] linux -- Python 3.12.3 /projects/whitespace-stego3/.venv/bin/python3

self = <test_cross_implementation.TestCrossImplementationRoundTrip object at 0x7a061d7d9af0>
message = 'Special chars: !@#$%^&*()_+-=[]{}|;\':",./<>?'
carrier = 'Carrier with spaces and punctuation!', password = 'test_password'

    @pytest.mark.parametrize("message", TEST_MESSAGES[:3])  # Limit for C binary tests
    @pytest.mark.parametrize("carrier", TEST_CARRIERS[:2])  # Limit for C binary tests
    @pytest.mark.parametrize("password", [None, "test_password"])  # Limit for C binary tests
    def test_rust_c_cross_roundtrip(self, message: str, carrier: str, password: Optional[str]):
        """Test Rust <-> C cross round trip."""
        if not RUST_AVAILABLE or not C_AVAILABLE:
            pytest.skip("Rust backend or C binary not available")
    
        # Rust encode -> C decode
        rust_encoded = rust_encode(message, carrier, password)
>       c_decoded = run_c_binary_decode(rust_encoded, password)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_cross_implementation.py:323: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

encoded_text = 'C\u200b\u200d\ufeff\ufeff\u200d\u200d\ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\u200d\u200d\u200d\ufeff\u200d\ufeff\u...ufeff\ufeff\ufeff\u200d\ufeff\u200d\u200d\ufeff\ufeff\ufeff\ufeff\u200d\ufeff\u200carrier with spaces and punctuation!'
password = 'test_password'

    def run_c_binary_decode(encoded_text: str, password: Optional[str] = None) -> str:
        """Run the C binary to decode a message."""
        if not C_AVAILABLE:
            pytest.skip("C binary not available")
    
        cmd = [str(C_BINARY_PATH), "decode"]
    
        # Create temporary file for carrier (encoded) input
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as carrier_file:
            carrier_file.write(encoded_text)
            carrier_file_path = carrier_file.name
    
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as output_file:
            output_file_path = output_file.name
    
        try:
            cmd.extend(["--carrier-file", carrier_file_path])
            cmd.extend(["--output", output_file_path])
    
            if password:
                cmd.extend(["--password", password])
    
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
            if result.returncode != 0:
>               raise RuntimeError(f"C binary decode failed: {result.stderr}")
E               RuntimeError: C binary decode failed: Error decoding message: Base64 decode failed

tests/test_cross_implementation.py:148: RuntimeError
```

