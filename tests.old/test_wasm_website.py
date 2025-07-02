"""
Selenium tests for the WASM implementation website.

This module contains comprehensive tests for the Whitespace Steganography
WASM web application, covering all major functionality including encoding,
decoding, file uploads, and UI interactions.
"""

import time
import tempfile
import os
from pathlib import Path
from typing import Optional, Tuple, Any
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager


class WASMWebsiteTester:
    """
    A test class for the WASM implementation website.

    This class provides methods to interact with the Whitespace Steganography
    web application and test its functionality using Selenium WebDriver.

    Attributes
    ----------
    driver : webdriver.Firefox
        The Firefox WebDriver instance for browser automation.
    base_url : str
        The base URL of the WASM website.
    wait : WebDriverWait
        WebDriverWait instance for handling dynamic content.
    """

    def __init__(self, base_url: str = "http://localhost:8000") -> None:
        """
        Initialize the WASM website tester.

        Parameters
        ----------
        base_url : str, optional
            The base URL of the WASM website, defaults to localhost:8000.
        """
        self.base_url = base_url
        self.driver: Optional[webdriver.Firefox] = None
        self.wait: Optional[WebDriverWait] = None

    def setup_driver(self) -> None:
        """Set up the Firefox WebDriver with appropriate options."""
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")  # Run in headless mode
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.add_argument("--disable-gpu")

        service = FirefoxService()
        self.driver = webdriver.Firefox(service=service, options=firefox_options)
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_driver(self) -> None:
        """Clean up the WebDriver instance."""
        if self.driver:
            self.driver.quit()

    def navigate_to_page(self) -> None:
        """Navigate to the WASM website."""
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call setup_driver() first.")
        self.driver.get(self.base_url)

    def wait_for_page_load(self) -> None:
        """Wait for the page to fully load and WASM module to initialize."""
        if not self.wait:
            raise RuntimeError("Wait not initialized. Call setup_driver() first.")
        # Wait for the main container to be present
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "container")))
        # Wait for WASM module to load (check for encode button to be present)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-primary")))
        # Additional wait to ensure WASM is fully loaded
        time.sleep(4)

    def get_element(self, element_id: str) -> WebElement:
        """
        Get a web element by its ID.

        Parameters
        ----------
        element_id : str
            The ID of the element to find.

        Returns
        -------
        WebElement
            The found web element.
        """
        if not self.driver:
            raise RuntimeError("Driver not initialized. Call setup_driver() first.")
        return self.driver.find_element(By.ID, element_id)

    def get_status_message(self) -> str:
        """
        Get the current status message from the page.

        Returns
        -------
        str
            The status message text, or empty string if no status.
        """
        try:
            status_element = self.driver.find_element(By.ID, "status")
            status_div = status_element.find_element(By.CLASS_NAME, "status")
            return status_div.text
        except:
            return ""

    def clear_all_fields(self) -> None:
        """Clear all input fields on the page."""
        self.get_element("message").clear()
        self.get_element("carrier").clear()
        self.get_element("password").clear()
        # Use JavaScript to clear the readonly output textarea
        if self.driver:
            self.driver.execute_script('document.getElementById("output").value = "";')

    def encode_message(self, message: str, carrier: str, password: str = "") -> str:
        """
        Encode a message using the web interface.

        Parameters
        ----------
        message : str
            The secret message to encode.
        carrier : str
            The carrier text where to hide the message.
        password : str, optional
            The password for encryption (not supported in WASM).

        Returns
        -------
        str
            The encoded result or error message.
        """
        self.get_element("message").send_keys(message)
        self.get_element("carrier").send_keys(carrier)
        if password:
            self.get_element("password").send_keys(password)
        # Wait for the encode button to be clickable by class
        if not self.wait or not self.driver:
            raise RuntimeError("Wait or driver not initialized.")
        encode_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
        )
        encode_button.click()

        # Wait for processing
        time.sleep(1)

        return self.get_element("output").get_attribute("value")

    def decode_message(self, carrier: str, password: str = "") -> str:
        """
        Decode a message using the web interface.

        Parameters
        ----------
        carrier : str
            The carrier text containing the encoded message.
        password : str, optional
            The password for decryption (not supported in WASM).

        Returns
        -------
        str
            The decoded result or error message.
        """
        self.get_element("carrier").send_keys(carrier)
        if password:
            self.get_element("password").send_keys(password)
        # Wait for the decode button to be clickable by class
        if not self.wait or not self.driver:
            raise RuntimeError("Wait or driver not initialized.")
        decode_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-secondary"))
        )
        decode_button.click()

        # Wait for processing
        time.sleep(1)

        return self.get_element("output").get_attribute("value")

    def upload_file(self, file_path: str) -> str:
        """
        Upload a file for decoding.

        Parameters
        ----------
        file_path : str
            Path to the file to upload.

        Returns
        -------
        str
            Status message after file upload.
        """
        file_input = self.get_element("file-upload")
        file_input.send_keys(file_path)

        load_button = self.driver.find_element(
            By.XPATH, "//button[contains(text(), 'Load File')]"
        )
        load_button.click()

        time.sleep(1)
        return self.get_status_message()

    def copy_to_clipboard(self) -> str:
        """
        Copy the output to clipboard.

        Returns
        -------
        str
            Status message after copy operation.
        """
        copy_button = self.driver.find_element(
            By.XPATH, "//button[contains(text(), 'Copy to Clipboard')]"
        )
        copy_button.click()

        time.sleep(1)
        return self.get_status_message()

    def download_output(self) -> str:
        """
        Download the output as a file.

        Returns
        -------
        str
            Status message after download operation.
        """
        download_button = self.driver.find_element(
            By.XPATH, "//button[contains(text(), 'Download File')]"
        )
        download_button.click()

        time.sleep(1)
        return self.get_status_message()


@pytest.fixture(scope="module")
def wasm_tester() -> WASMWebsiteTester:
    """
    Create a WASM website tester instance.

    Returns
    -------
    WASMWebsiteTester
        A configured tester instance.
    """
    tester = WASMWebsiteTester()
    tester.setup_driver()
    yield tester
    tester.teardown_driver()


@pytest.fixture
def clean_page(wasm_tester: WASMWebsiteTester) -> WASMWebsiteTester:
    """
    Provide a clean page for each test.

    Parameters
    ----------
    wasm_tester : WASMWebsiteTester
        The tester instance.

    Returns
    -------
    WASMWebsiteTester
        The tester with a clean page.
    """
    wasm_tester.navigate_to_page()
    wasm_tester.wait_for_page_load()
    wasm_tester.clear_all_fields()
    return wasm_tester


@pytest.mark.skip(reason="WASM tests require a running server and are failing due to network issues")
class TestWASMWebsiteBasic:
    """Test basic functionality of the WASM website."""

    def test_page_loads_correctly(self, wasm_tester: WASMWebsiteTester) -> None:
        """Test that the page loads and WASM module initializes."""
        wasm_tester.navigate_to_page()
        wasm_tester.wait_for_page_load()

        # Check that main elements are present
        assert wasm_tester.get_element("message").is_displayed()
        assert wasm_tester.get_element("carrier").is_displayed()
        assert wasm_tester.get_element("output").is_displayed()

        # Wait for encode/decode buttons to be clickable by class
        if not wasm_tester.wait or not wasm_tester.driver:
            raise RuntimeError("Wait or driver not initialized.")
        encode_button = wasm_tester.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
        )
        decode_button = wasm_tester.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-secondary"))
        )
        assert encode_button.is_displayed()
        assert decode_button.is_displayed()

    def test_page_title(self, wasm_tester: WASMWebsiteTester) -> None:
        """Test that the page has the correct title."""
        wasm_tester.navigate_to_page()
        wasm_tester.wait_for_page_load()

        assert "Whitespace Steganography Tool" in wasm_tester.driver.title

    def test_clear_all_functionality(self, clean_page: WASMWebsiteTester) -> None:
        """Test the clear all functionality."""
        # Fill in some data
        clean_page.get_element("message").send_keys("test message")
        clean_page.get_element("carrier").send_keys("test carrier")
        clean_page.get_element("password").send_keys("test password")

        # Click clear all
        clear_button = clean_page.driver.find_element(
            By.XPATH, "//button[contains(text(), 'Clear All')]"
        )
        clear_button.click()

        # Verify all fields are cleared
        assert clean_page.get_element("message").get_attribute("value") == ""
        assert clean_page.get_element("carrier").get_attribute("value") == ""
        assert clean_page.get_element("password").get_attribute("value") == ""
        assert clean_page.get_element("output").get_attribute("value") == ""


@pytest.mark.skip(reason="WASM tests require a running server and are failing due to network issues")
class TestWASMWebsiteEncoding:
    """Test encoding functionality of the WASM website."""

    def test_basic_encoding(self, clean_page: WASMWebsiteTester) -> None:
        """Test basic message encoding."""
        message = "Hello, World!"
        carrier = "This is a normal text message that will contain hidden data."

        result = clean_page.encode_message(message, carrier)

        # Check that encoding was successful
        assert result != ""
        assert "Hello, World!" not in result  # Original message should not be visible
        # Note: Carrier text is encoded with invisible characters, so we can't check for it directly
        # Instead, check that the result is different from the original carrier
        assert result != carrier

        # Check status message
        status = clean_page.get_status_message()
        assert "encoded successfully" in status.lower()

    def test_encoding_with_empty_message(self, clean_page: WASMWebsiteTester) -> None:
        """Test encoding with empty message (should show error)."""
        carrier = "This is carrier text."
        # Try to encode with empty message
        clean_page.get_element("carrier").send_keys(carrier)
        if not clean_page.wait or not clean_page.driver:
            raise RuntimeError("Wait or driver not initialized.")
        encode_button = clean_page.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
        )
        encode_button.click()
        time.sleep(1)
        # Check error message
        status = clean_page.get_status_message()
        assert "error" in status.lower()
        assert "message" in status.lower()

    def test_encoding_with_empty_carrier(self, clean_page: WASMWebsiteTester) -> None:
        """Test encoding with empty carrier (should show error)."""
        message = "Secret message"
        # Try to encode with empty carrier
        clean_page.get_element("message").send_keys(message)
        if not clean_page.wait or not clean_page.driver:
            raise RuntimeError("Wait or driver not initialized.")
        encode_button = clean_page.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
        )
        encode_button.click()
        time.sleep(1)
        # Check error message
        status = clean_page.get_status_message()
        assert "error" in status.lower()
        assert "carrier" in status.lower()

    def test_encoding_special_characters(self, clean_page: WASMWebsiteTester) -> None:
        """Test encoding with special characters."""
        message = "Special chars: !@#$%^&*()_+-=[]{}|;':\",./<>?"
        carrier = "Carrier with special chars: áéíóú ñ ç ß"

        result = clean_page.encode_message(message, carrier)

        # Check that encoding was successful
        assert result != ""
        assert "Special chars:" not in result  # Original message should not be visible
        # Note: Carrier text is encoded with invisible characters, so we can't check for it directly
        # Instead, check that the result is different from the original carrier
        assert result != carrier

        status = clean_page.get_status_message()
        assert "encoded successfully" in status.lower()


@pytest.mark.skip(reason="WASM tests require a running server and are failing due to network issues")
class TestWASMWebsiteDecoding:
    """Test decoding functionality of the WASM website."""

    def test_basic_decoding(self, clean_page: WASMWebsiteTester) -> None:
        """Test basic message decoding."""
        message = "Secret message for decoding"
        carrier = "This is carrier text for decoding test."

        # First encode a message
        encoded = clean_page.encode_message(message, carrier)
        clean_page.clear_all_fields()

        # Then decode it
        result = clean_page.decode_message(encoded)

        # Check that decoding was successful
        assert result == message

        status = clean_page.get_status_message()
        assert "decoded successfully" in status.lower()

    def test_decoding_without_encoded_data(self, clean_page: WASMWebsiteTester) -> None:
        """Test decoding text without encoded data."""
        plain_text = "This is just plain text without any encoded data."

        result = clean_page.decode_message(plain_text)

        # Check that no data was found
        status = clean_page.get_status_message()
        assert "no encoded data found" in status.lower() or "info" in status.lower()

    def test_decoding_empty_input(self, clean_page: WASMWebsiteTester) -> None:
        """Test decoding with empty input (should show error)."""
        # Try to decode with empty carrier
        if not clean_page.wait or not clean_page.driver:
            raise RuntimeError("Wait or driver not initialized.")
        decode_button = clean_page.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-secondary"))
        )
        decode_button.click()

        time.sleep(1)

        # Check error message
        status = clean_page.get_status_message()
        assert "error" in status.lower()
        assert "text to decode" in status.lower() or "enter text" in status.lower()


@pytest.mark.skip(reason="WASM tests require a running server and are failing due to network issues")
class TestWASMWebsiteFileOperations:
    """Test file upload and download functionality."""

    def test_file_upload(self, clean_page: WASMWebsiteTester) -> None:
        """Test file upload functionality."""
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("This is test content for file upload.")
            temp_file_path = f.name

        try:
            # Upload the file
            status = clean_page.upload_file(temp_file_path)

            # Check that file was loaded
            assert "loaded successfully" in status.lower()

            # Check that content was loaded into carrier field
            carrier_content = clean_page.get_element("carrier").get_attribute("value")
            assert "This is test content for file upload." in carrier_content

        finally:
            # Clean up temporary file
            os.unlink(temp_file_path)

    def test_file_upload_without_selection(self, clean_page: WASMWebsiteTester) -> None:
        """Test file upload without selecting a file (should show error)."""
        # Try to load file without selecting one
        load_button = clean_page.driver.find_element(
            By.XPATH, "//button[contains(text(), 'Load File')]"
        )
        load_button.click()

        time.sleep(1)

        # Check error message
        status = clean_page.get_status_message()
        assert "error" in status.lower()
        assert "select a file" in status.lower()

    def test_download_output(self, clean_page: WASMWebsiteTester) -> None:
        """Test downloading output as a file."""
        # First encode a message to have output
        message = "Message for download test"
        carrier = "Carrier text for download test"

        clean_page.encode_message(message, carrier)

        # Try to download (this will trigger download in headless mode)
        status = clean_page.download_output()

        # Check that download was attempted
        assert (
            "downloaded successfully" in status.lower() or "download" in status.lower()
        )


@pytest.mark.skip(reason="WASM tests require a running server and are failing due to network issues")
class TestWASMWebsiteClipboard:
    """Test clipboard functionality."""

    def test_copy_to_clipboard(self, clean_page: WASMWebsiteTester) -> None:
        """Test copying output to clipboard."""
        # First encode a message to have output
        message = "Message for clipboard test"
        carrier = "Carrier text for clipboard test"

        clean_page.encode_message(message, carrier)

        # Try to copy to clipboard
        status = clean_page.copy_to_clipboard()

        # Check that copy was successful
        assert "copied to clipboard" in status.lower()


@pytest.mark.skip(reason="WASM tests require a running server and are failing due to network issues")
class TestWASMWebsitePassword:
    """Test password functionality (not supported in WASM)."""

    def test_password_field_disabled_notice(
        self, clean_page: WASMWebsiteTester
    ) -> None:
        """Test that password field shows it's not supported."""
        password_field = clean_page.get_element("password")
        placeholder = password_field.get_attribute("placeholder")

        # Check that placeholder indicates password is not supported
        assert (
            "not yet supported" in placeholder.lower()
            or "not supported" in placeholder.lower()
        )

    def test_encoding_with_password(self, clean_page: WASMWebsiteTester) -> None:
        """Test encoding with password (should still work but ignore password)."""
        message = "Secret message"
        carrier = "Carrier text"
        password = "testpassword"

        result = clean_page.encode_message(message, carrier, password)

        # Password is not supported in WASM, so result might be empty or show an error
        # Check status message instead of result content
        status = clean_page.get_status_message()
        # Either encoding succeeds (ignoring password) or shows an error about password
        assert (
            "encoded successfully" in status.lower()
            or "error" in status.lower()
            or "password" in status.lower()
        )


@pytest.mark.skip(reason="WASM tests require a running server and are failing due to network issues")
class TestWASMWebsiteRoundTrip:
    """Test complete round-trip encoding and decoding."""

    def test_simple_round_trip(self, clean_page: WASMWebsiteTester) -> None:
        """Test simple round-trip encoding and decoding."""
        original_message = "This is a test message for round-trip testing."
        carrier = "This is the carrier text that will contain the hidden message."

        # Encode
        encoded = clean_page.encode_message(original_message, carrier)
        clean_page.clear_all_fields()

        # Decode
        decoded = clean_page.decode_message(encoded)

        # Verify round-trip
        assert decoded == original_message

    def test_complex_round_trip(self, clean_page: WASMWebsiteTester) -> None:
        """Test complex round-trip with special characters and long text."""
        original_message = """
        This is a complex message with:
        - Multiple lines
        - Special characters: !@#$%^&*()_+-=[]{}|;':",./<>?
        - Unicode: áéíóú ñ ç ß αβγδε ζηθικλμν ξοπρστ υφχψω
        - Numbers: 1234567890
        - Emojis: 🚀🔐💻📱
        """

        carrier = """
        This is a complex carrier text with:
        - Multiple paragraphs
        - Various formatting
        - Special characters: áéíóú ñ ç ß
        - Numbers: 9876543210
        - And more content to make it realistic.
        """

        # Encode
        encoded = clean_page.encode_message(original_message, carrier)
        clean_page.clear_all_fields()

        # Decode
        decoded = clean_page.decode_message(encoded)

        # Verify round-trip (strip whitespace to handle formatting differences)
        assert decoded.strip() == original_message.strip()


@pytest.mark.skip(reason="WASM tests require a running server and are failing due to network issues")
class TestWASMWebsiteErrorHandling:
    """Test error handling and edge cases."""

    def test_very_long_message(self, clean_page: WASMWebsiteTester) -> None:
        """Test encoding with a very long message."""
        long_message = "A" * 10000  # 10KB message
        carrier = "Short carrier text."

        result = clean_page.encode_message(long_message, carrier)

        # Should handle long messages gracefully
        assert result != ""
        status = clean_page.get_status_message()
        assert "error" not in status.lower() or "encoded successfully" in status.lower()

    def test_very_long_carrier(self, clean_page: WASMWebsiteTester) -> None:
        """Test encoding with a very long carrier."""
        message = "Short message"
        long_carrier = "B" * 10000  # 10KB carrier

        result = clean_page.encode_message(message, long_carrier)

        # Should handle long carriers gracefully
        assert result != ""
        status = clean_page.get_status_message()
        assert "error" not in status.lower() or "encoded successfully" in status.lower()

    def test_unicode_edge_cases(self, clean_page: WASMWebsiteTester) -> None:
        """Test encoding with Unicode edge cases."""
        message = "🚀🔐💻📱" * 100  # Many emojis
        carrier = "Normal carrier text"

        result = clean_page.encode_message(message, carrier)

        # Should handle Unicode gracefully
        assert result != ""
        status = clean_page.get_status_message()
        assert "error" not in status.lower() or "encoded successfully" in status.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
