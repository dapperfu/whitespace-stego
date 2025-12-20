"""Error classes for whitespace steganography operations."""


class StegoError(Exception):
    """Base exception for all steganography errors."""

    pass


class EncodingError(StegoError):
    """Raised when encoding fails."""

    pass


class DecodingError(StegoError):
    """Raised when decoding fails."""

    pass


class InvalidPayloadError(DecodingError):
    """Raised when payload contains invalid characters."""

    pass


class MissingMarkerError(DecodingError):
    """Raised when control markers are missing from encoded text."""

    pass


class InvalidBase64Error(DecodingError):
    """Raised when Base64 decoding fails."""

    pass


class InvalidUTF8Error(DecodingError):
    """Raised when UTF-8 decoding fails."""

    pass

