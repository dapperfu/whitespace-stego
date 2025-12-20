//! Unicode control character constants.

/// U+2060 Word Joiner - marks the beginning of an encoded payload
pub const CONTROL_START: char = '\u{2060}';

/// U+2063 Invisible Separator - marks the end of an encoded payload
pub const CONTROL_END: char = '\u{2063}';

/// U+200B Zero Width Space - represents binary bit value 0
pub const BIT_0: char = '\u{200B}';

/// U+200C Zero Width Non-Joiner - represents binary bit value 1
pub const BIT_1: char = '\u{200C}';

