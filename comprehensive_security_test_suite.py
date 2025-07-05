#!/usr/bin/env python3
"""
Comprehensive Security and Edge Case Test Suite for Whitespace Steganography

This test suite covers:
1. Edge cases (empty messages, single characters, very long messages)
2. Security scenarios (malicious inputs, memory exhaustion attempts)
3. Unicode and encoding edge cases
4. Cross-implementation compatibility
5. Protocol robustness
6. Performance under stress
"""

import subprocess
import sys
import os
import tempfile
import json
import time
import hashlib
from typing import List, Dict, Tuple, Optional, Any
from dataclasses import dataclass
from enum import Enum

# Add Python implementation to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'implementations', 'python'))

class TestResult(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    ERROR = "ERROR"
    SKIP = "SKIP"

@dataclass
class TestCase:
    name: str
    category: str
    description: str
    message: str
    carrier: str
    password: str
    expected_result: TestResult
    expected_error: Optional[str] = None
    timeout: int = 30

class SecurityTestSuite:
    def __init__(self):
        self.results = {}
        self.implementations = {
            'cpp': self.test_cpp,
            'c': self.test_c,
            'go': self.test_go,
            'python_core': self.test_python_core,
            'python_rust': self.test_python_rust,
            'python_c': self.test_python_c
        }
        
    def run_command(self, cmd: List[str], input_data: Optional[str] = None, timeout: int = 30) -> Tuple[int, str, str]:
        """Run a command and return (return_code, stdout, stderr)"""
        try:
            result = subprocess.run(
                cmd,
                input=input_data.encode() if input_data else None,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return -1, "", "Command timed out"
        except Exception as e:
            return -1, "", str(e)

    def create_temp_file(self, content: str, suffix: str = ".txt") -> str:
        """Create a temporary file with content and return the path"""
        fd, path = tempfile.mkstemp(suffix=suffix)
        with os.fdopen(fd, 'w') as f:
            f.write(content)
        return path

    def cleanup_temp_file(self, path: str):
        """Clean up a temporary file"""
        try:
            os.unlink(path)
        except:
            pass

    def test_cpp(self, test_case: TestCase) -> Dict[str, Any]:
        """Test C++ implementation"""
        print(f"    Testing C++...")
        
        # Create temporary files
        message_file = self.create_temp_file(test_case.message)
        carrier_file = self.create_temp_file(test_case.carrier)
        output_file = self.create_temp_file("")
        decoded_file = self.create_temp_file("")
        
        try:
            # Encode
            encode_cmd = [
                "./implementations/cpp/bin/whitespace-stego-cpp",
                "encode",
                "-mf", message_file,
                "-cf", carrier_file,
                "-o", output_file
            ]
            if test_case.password:
                encode_cmd.extend(["-p", test_case.password])
            
            ret_code, stdout, stderr = self.run_command(encode_cmd, timeout=test_case.timeout)
            if ret_code != 0:
                return {
                    "success": False,
                    "error": f"Encode failed: {stderr}",
                    "return_code": ret_code
                }
            
            # Read encoded output
            with open(output_file, 'r') as f:
                encoded = f.read()
            
            # Decode
            decode_cmd = [
                "./implementations/cpp/bin/whitespace-stego-cpp",
                "decode",
                "-cf", output_file,
                "-o", decoded_file
            ]
            if test_case.password:
                decode_cmd.extend(["-p", test_case.password])
            
            ret_code, stdout, stderr = self.run_command(decode_cmd, timeout=test_case.timeout)
            if ret_code != 0:
                return {
                    "success": False,
                    "error": f"Decode failed: {stderr}",
                    "return_code": ret_code
                }
            
            # Read decoded output
            with open(decoded_file, 'r') as f:
                decoded = f.read().strip()
            
            success = decoded == test_case.message
            return {
                "success": success,
                "encoded_size": len(encoded),
                "decoded": decoded,
                "expected": test_case.message
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            self.cleanup_temp_file(message_file)
            self.cleanup_temp_file(carrier_file)
            self.cleanup_temp_file(output_file)
            self.cleanup_temp_file(decoded_file)

    def test_c(self, test_case: TestCase) -> Dict[str, Any]:
        """Test C implementation"""
        print(f"    Testing C...")
        
        # Create temporary files
        message_file = self.create_temp_file(test_case.message)
        carrier_file = self.create_temp_file(test_case.carrier)
        output_file = self.create_temp_file("")
        decoded_file = self.create_temp_file("")
        
        try:
            # Encode
            encode_cmd = [
                "./implementations/c/bin/whitespace-stego-c",
                "encode",
                "--message-file", message_file,
                "--carrier-file", carrier_file,
                "--output", output_file
            ]
            if test_case.password:
                encode_cmd.extend(["--password", test_case.password])
            
            ret_code, stdout, stderr = self.run_command(encode_cmd, timeout=test_case.timeout)
            if ret_code != 0:
                return {
                    "success": False,
                    "error": f"Encode failed: {stderr}",
                    "return_code": ret_code
                }
            
            # Read encoded output
            with open(output_file, 'r') as f:
                encoded = f.read()
            
            # Decode
            decode_cmd = [
                "./implementations/c/bin/whitespace-stego-c",
                "decode",
                "--carrier-file", output_file,
                "--output", decoded_file
            ]
            if test_case.password:
                decode_cmd.extend(["--password", test_case.password])
            
            ret_code, stdout, stderr = self.run_command(decode_cmd, timeout=test_case.timeout)
            if ret_code != 0:
                return {
                    "success": False,
                    "error": f"Decode failed: {stderr}",
                    "return_code": ret_code
                }
            
            # Read decoded output
            with open(decoded_file, 'r') as f:
                decoded = f.read().strip()
            
            success = decoded == test_case.message
            return {
                "success": success,
                "encoded_size": len(encoded),
                "decoded": decoded,
                "expected": test_case.message
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            self.cleanup_temp_file(message_file)
            self.cleanup_temp_file(carrier_file)
            self.cleanup_temp_file(output_file)
            self.cleanup_temp_file(decoded_file)

    def test_go(self, test_case: TestCase) -> Dict[str, Any]:
        """Test Go implementation"""
        print(f"    Testing Go...")
        
        # Create temporary files
        carrier_file = self.create_temp_file(test_case.carrier)
        output_file = self.create_temp_file("")
        decoded_file = self.create_temp_file("")
        
        try:
            # Encode
            encode_cmd = [
                "./implementations/go/bin/whitespace-stego-go",
                "encode",
                "-message", test_case.message,
                "-carrier-file", carrier_file,
                "-output", output_file
            ]
            if test_case.password:
                encode_cmd.extend(["-password", test_case.password])
            
            ret_code, stdout, stderr = self.run_command(encode_cmd, timeout=test_case.timeout)
            if ret_code != 0:
                return {
                    "success": False,
                    "error": f"Encode failed: {stderr}",
                    "return_code": ret_code
                }
            
            # Read encoded output
            with open(output_file, 'r') as f:
                encoded = f.read()
            
            # Decode
            decode_cmd = [
                "./implementations/go/bin/whitespace-stego-go",
                "decode",
                "-carrier-file", output_file,
                "-output", decoded_file
            ]
            if test_case.password:
                decode_cmd.extend(["-password", test_case.password])
            
            ret_code, stdout, stderr = self.run_command(decode_cmd, timeout=test_case.timeout)
            if ret_code != 0:
                return {
                    "success": False,
                    "error": f"Decode failed: {stderr}",
                    "return_code": ret_code
                }
            
            # Read decoded output
            with open(decoded_file, 'r') as f:
                decoded = f.read().strip()
            
            success = decoded == test_case.message
            return {
                "success": success,
                "encoded_size": len(encoded),
                "decoded": decoded,
                "expected": test_case.message
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            self.cleanup_temp_file(carrier_file)
            self.cleanup_temp_file(output_file)
            self.cleanup_temp_file(decoded_file)

    def test_python_core(self, test_case: TestCase) -> Dict[str, Any]:
        """Test Python core implementation"""
        print(f"    Testing Python (core)...")
        return self._test_python(test_case, "core")

    def test_python_rust(self, test_case: TestCase) -> Dict[str, Any]:
        """Test Python Rust backend"""
        print(f"    Testing Python (Rust)...")
        return self._test_python(test_case, "rust")

    def test_python_c(self, test_case: TestCase) -> Dict[str, Any]:
        """Test Python C backend"""
        print(f"    Testing Python (C)...")
        return self._test_python(test_case, "c")

    def _test_python(self, test_case: TestCase, backend: str) -> Dict[str, Any]:
        """Test Python implementation with specified backend"""
        test_script = f"""
import sys
sys.path.insert(0, 'implementations/python')

try:
    import whitespace_stego
    
    # Test encoding
    if '{backend}' == 'rust' and whitespace_stego.rust_available:
        encoded = whitespace_stego.rust_encode('{test_case.message}', '{test_case.carrier}', '{test_case.password}')
    elif '{backend}' == 'c' and whitespace_stego.c_available:
        encoded = whitespace_stego.c_encode('{test_case.message}', '{test_case.carrier}', '{test_case.password}')
    else:
        encoded = whitespace_stego.encode('{test_case.message}', '{test_case.carrier}', '{test_case.password}')
    
    # Test decoding
    if '{backend}' == 'rust' and whitespace_stego.rust_available:
        decoded = whitespace_stego.rust_decode(encoded, '{test_case.password}')
    elif '{backend}' == 'c' and whitespace_stego.c_available:
        decoded = whitespace_stego.c_decode(encoded, '{test_case.password}')
    else:
        decoded = whitespace_stego.decode(encoded, '{test_case.password}')
    
    print(f"ENCODED_SIZE:{{len(encoded)}}")
    print(f"DECODED:{{decoded}}")
    print(f"SUCCESS:{{decoded == '{test_case.message}'}}")
    
except Exception as e:
    print(f"ERROR:{{str(e)}}")
    sys.exit(1)
"""
        
        ret_code, stdout, stderr = self.run_command(["python3", "-c", test_script], timeout=test_case.timeout)
        if ret_code != 0:
            return {"success": False, "error": f"Python test failed: {stderr}"}
        
        # Parse output
        lines = stdout.strip().split('\n')
        encoded_size = None
        decoded = None
        success = False
        
        for line in lines:
            if line.startswith("ENCODED_SIZE:"):
                encoded_size = int(line[13:])
            elif line.startswith("DECODED:"):
                decoded = line[8:]
            elif line.startswith("SUCCESS:"):
                success = line[8:].lower() == "true"
        
        if encoded_size is None or decoded is None:
            return {"success": False, "error": "Could not parse Python output"}
        
        return {
            "success": success,
            "encoded_size": encoded_size,
            "decoded": decoded,
            "expected": test_case.message
        }

    def generate_test_cases(self) -> List[TestCase]:
        """Generate comprehensive test cases"""
        test_cases = []
        
        # 1. Edge Cases
        test_cases.extend([
            TestCase("Empty message", "edge_cases", "Empty message", "", "Carrier text", "", TestResult.PASS),
            TestCase("Empty carrier", "edge_cases", "Empty carrier", "Message", "", "", TestResult.PASS),
            TestCase("Single character", "edge_cases", "Single character message", "A", "Carrier", "", TestResult.PASS),
            TestCase("Single character carrier", "edge_cases", "Single character carrier", "Message", "B", "", TestResult.PASS),
            TestCase("Very long message", "edge_cases", "Very long message", "A" * 100000, "Carrier", "", TestResult.PASS),
            TestCase("Very long carrier", "edge_cases", "Very long carrier", "Message", "B" * 100000, "", TestResult.PASS),
            TestCase("Null bytes in message", "edge_cases", "Message with null bytes", "Hello\0World", "Carrier", "", TestResult.PASS),
            TestCase("Null bytes in carrier", "edge_cases", "Carrier with null bytes", "Message", "Carrier\0text", "", TestResult.PASS),
        ])
        
        # 2. Unicode Edge Cases
        test_cases.extend([
            TestCase("Basic Unicode", "unicode", "Basic Unicode characters", "Hello 世界!", "Carrier 测试", "", TestResult.PASS),
            TestCase("Emoji", "unicode", "Emoji characters", "Hello 🌍!", "Carrier 🚀", "", TestResult.PASS),
            TestCase("Combining characters", "unicode", "Combining Unicode characters", "e\u0301", "Carrier", "", TestResult.PASS),
            TestCase("Right-to-left text", "unicode", "RTL text", "שָׁלוֹם", "Carrier", "", TestResult.PASS),
            TestCase("Zero-width characters", "unicode", "Zero-width characters in message", "Hello\u200bWorld", "Carrier", "", TestResult.PASS),
            TestCase("Surrogate pairs", "unicode", "Surrogate pairs", "Hello \U0001F600", "Carrier", "", TestResult.PASS),
        ])
        
        # 3. Security Scenarios
        test_cases.extend([
            TestCase("Memory exhaustion attempt", "security", "Very large message", "A" * (1024 * 1024), "Carrier", "", TestResult.FAIL, "Input too large"),
            TestCase("Memory exhaustion carrier", "security", "Very large carrier", "Message", "B" * (1024 * 1024), "", TestResult.PASS),
            TestCase("Malicious UTF-8", "security", "Invalid UTF-8 sequences", "Hello\xFF\xFEWorld", "Carrier", "", TestResult.PASS),
            TestCase("Control characters", "security", "Control characters", "Hello\x01\x02\x03World", "Carrier", "", TestResult.PASS),
            TestCase("Long password", "security", "Very long password", "Message", "Carrier", "P" * 10000, TestResult.PASS),
            TestCase("Empty password", "security", "Empty password", "Message", "Carrier", "", TestResult.PASS),
        ])
        
        # 4. Protocol Edge Cases
        test_cases.extend([
            TestCase("Message with markers", "protocol", "Message containing protocol markers", "Hello\uFEFFWorld\u200C", "Carrier", "", TestResult.PASS),
            TestCase("Carrier with markers", "protocol", "Carrier containing protocol markers", "Message", "Carrier\uFEFFtext\u200C", "", TestResult.PASS),
            TestCase("Mixed encoding", "protocol", "Mixed ASCII and Unicode", "Hello 世界! 🌍", "Carrier 测试 🚀", "", TestResult.PASS),
            TestCase("Special whitespace", "protocol", "Special whitespace characters", "Hello\u00A0\u2000\u2001World", "Carrier", "", TestResult.PASS),
        ])
        
        # 5. Performance Tests
        test_cases.extend([
            TestCase("Medium message", "performance", "Medium sized message", "A" * 50000, "B" * 25000, "", TestResult.PASS, timeout=60),
            TestCase("Large message", "performance", "Large sized message", "A" * 200000, "B" * 100000, "", TestResult.PASS, timeout=120),
        ])
        
        # 6. Encryption Edge Cases
        test_cases.extend([
            TestCase("Simple encryption", "encryption", "Simple password", "Secret message", "Carrier", "password123", TestResult.PASS),
            TestCase("Unicode password", "encryption", "Unicode password", "Secret message", "Carrier", "密码123", TestResult.PASS),
            TestCase("Special chars password", "encryption", "Special characters in password", "Secret message", "Carrier", "p@ssw0rd!#$", TestResult.PASS),
            TestCase("Empty message encrypted", "encryption", "Empty message with password", "", "Carrier", "password", TestResult.PASS),
        ])
        
        return test_cases

    def run_test_case(self, test_case: TestCase) -> Dict[str, Any]:
        """Run a single test case across all implementations"""
        print(f"  Running: {test_case.name} ({test_case.category})")
        print(f"    Description: {test_case.description}")
        print(f"    Message size: {len(test_case.message)} bytes")
        print(f"    Carrier size: {len(test_case.carrier)} bytes")
        print(f"    Password: {'Yes' if test_case.password else 'No'}")
        
        results = {}
        
        for impl_name, test_func in self.implementations.items():
            try:
                start_time = time.time()
                result = test_func(test_case)
                end_time = time.time()
                
                result["execution_time"] = end_time - start_time
                result["implementation"] = impl_name
                
                # Determine if result matches expected
                if test_case.expected_result == TestResult.PASS:
                    success = result.get("success", False)
                elif test_case.expected_result == TestResult.FAIL:
                    success = not result.get("success", True)
                    if test_case.expected_error and test_case.expected_error not in result.get("error", ""):
                        success = False
                else:
                    success = True  # For SKIP cases
                
                result["expected_result"] = test_case.expected_result.value
                result["test_passed"] = success
                
                if success:
                    print(f"    ✓ {impl_name}: PASS ({result['execution_time']:.2f}s)")
                else:
                    print(f"    ✗ {impl_name}: FAIL - {result.get('error', 'Unknown error')}")
                
                results[impl_name] = result
                
            except Exception as e:
                print(f"    ✗ {impl_name}: ERROR - {str(e)}")
                results[impl_name] = {
                    "success": False,
                    "error": str(e),
                    "implementation": impl_name,
                    "expected_result": test_case.expected_result.value,
                    "test_passed": False
                }
        
        return results

    def run_all_tests(self) -> Dict[str, Any]:
        """Run all test cases"""
        print("=== Comprehensive Security and Edge Case Test Suite ===")
        print(f"Testing {len(self.implementations)} implementations")
        print()
        
        test_cases = self.generate_test_cases()
        all_results = {}
        
        # Group by category
        categories = {}
        for test_case in test_cases:
            if test_case.category not in categories:
                categories[test_case.category] = []
            categories[test_case.category].append(test_case)
        
        for category, cases in categories.items():
            print(f"\n=== {category.upper()} TESTS ===")
            category_results = {}
            
            for test_case in cases:
                test_results = self.run_test_case(test_case)
                category_results[test_case.name] = test_results
                all_results[test_case.name] = test_results
                print()
            
            # Category summary
            total_tests = len(cases) * len(self.implementations)
            passed_tests = sum(
                1 for case_results in category_results.values()
                for impl_result in case_results.values()
                if impl_result.get("test_passed", False)
            )
            print(f"Category {category}: {passed_tests}/{total_tests} tests passed")
        
        return all_results

    def generate_report(self, results: Dict[str, Any]) -> str:
        """Generate a comprehensive test report"""
        report = []
        report.append("# Comprehensive Security and Edge Case Test Report")
        report.append("")
        
        # Summary statistics
        total_tests = 0
        passed_tests = 0
        failed_tests = 0
        error_tests = 0
        
        implementation_stats = {impl: {"passed": 0, "failed": 0, "errors": 0} for impl in self.implementations.keys()}
        
        for test_name, test_results in results.items():
            for impl_name, impl_result in test_results.items():
                total_tests += 1
                if impl_result.get("test_passed", False):
                    passed_tests += 1
                    implementation_stats[impl_name]["passed"] += 1
                elif "error" in impl_result:
                    error_tests += 1
                    implementation_stats[impl_name]["errors"] += 1
                else:
                    failed_tests += 1
                    implementation_stats[impl_name]["failed"] += 1
        
        report.append("## Summary")
        report.append(f"- **Total Tests**: {total_tests}")
        report.append(f"- **Passed**: {passed_tests} ({passed_tests/total_tests*100:.1f}%)")
        report.append(f"- **Failed**: {failed_tests} ({failed_tests/total_tests*100:.1f}%)")
        report.append(f"- **Errors**: {error_tests} ({error_tests/total_tests*100:.1f}%)")
        report.append("")
        
        # Implementation comparison
        report.append("## Implementation Comparison")
        report.append("| Implementation | Passed | Failed | Errors | Success Rate |")
        report.append("|----------------|--------|--------|--------|--------------|")
        
        for impl_name, stats in implementation_stats.items():
            total_impl_tests = stats["passed"] + stats["failed"] + stats["errors"]
            success_rate = stats["passed"] / total_impl_tests * 100 if total_impl_tests > 0 else 0
            report.append(f"| {impl_name} | {stats['passed']} | {stats['failed']} | {stats['errors']} | {success_rate:.1f}% |")
        
        report.append("")
        
        # Detailed results by category
        categories = {}
        for test_name, test_results in results.items():
            # Extract category from test name or use a default
            category = "general"
            for cat in ["edge_cases", "unicode", "security", "protocol", "performance", "encryption"]:
                if cat in test_name.lower():
                    category = cat
                    break
            
            if category not in categories:
                categories[category] = []
            categories[category].append((test_name, test_results))
        
        for category, tests in categories.items():
            report.append(f"## {category.replace('_', ' ').title()} Tests")
            report.append("")
            
            for test_name, test_results in tests:
                report.append(f"### {test_name}")
                
                for impl_name, impl_result in test_results.items():
                    status = "✅ PASS" if impl_result.get("test_passed", False) else "❌ FAIL"
                    error_msg = f" - {impl_result.get('error', '')}" if "error" in impl_result else ""
                    exec_time = f" ({impl_result.get('execution_time', 0):.2f}s)" if "execution_time" in impl_result else ""
                    
                    report.append(f"- **{impl_name}**: {status}{error_msg}{exec_time}")
                
                report.append("")
        
        return "\n".join(report)

def main():
    """Main test function"""
    test_suite = SecurityTestSuite()
    results = test_suite.run_all_tests()
    
    # Generate and save report
    report = test_suite.generate_report(results)
    
    with open("comprehensive_test_report.md", "w") as f:
        f.write(report)
    
    # Save detailed results
    with open("comprehensive_test_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\n" + "="*80)
    print("TEST SUITE COMPLETED")
    print("="*80)
    print(f"Detailed report: comprehensive_test_report.md")
    print(f"Raw results: comprehensive_test_results.json")
    
    # Print summary
    total_tests = sum(len(test_results) for test_results in results.values())
    passed_tests = sum(
        1 for test_results in results.values()
        for impl_result in test_results.values()
        if impl_result.get("test_passed", False)
    )
    
    print(f"\nSummary: {passed_tests}/{total_tests} tests passed ({passed_tests/total_tests*100:.1f}%)")

if __name__ == "__main__":
    main() 