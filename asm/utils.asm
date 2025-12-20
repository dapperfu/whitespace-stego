; Utility functions for whitespace steganography

section .text

; Helper function to find substring in string
; find_substring(haystack, haystack_len, needle, needle_len)
; Returns: pointer to found substring or NULL
global find_substring_asm
find_substring_asm:
    ; TODO: Implement substring search
    xor rax, rax  ; Return NULL (not found)
    ret

