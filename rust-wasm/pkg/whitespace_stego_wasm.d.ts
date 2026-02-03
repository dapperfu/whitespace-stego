/* tslint:disable */
/* eslint-disable */

/**
 * Decode a message from invisible Unicode characters.
 *
 * # Arguments
 *
 * * `encoded_text` - Text containing the encoded message
 * * `password` - Optional password for decryption (null/undefined for no password)
 *
 * # Returns
 *
 * Decoded original message
 *
 * # Errors
 *
 * Throws a JavaScript error if decoding fails
 */
export function decode_message(encoded_text: string, password?: string | null): string;

/**
 * Encode a message into invisible Unicode characters.
 *
 * # Arguments
 *
 * * `message` - The message to encode
 * * `carrier` - Optional carrier text (null/undefined for no carrier)
 * * `password` - Optional password for encryption (null/undefined for no password)
 *
 * # Returns
 *
 * Encoded string with invisible Unicode characters
 *
 * # Errors
 *
 * Throws a JavaScript error if encoding fails
 */
export function encode_message(message: string, carrier?: string | null, password?: string | null): string;

/**
 * Check if a string contains encoded data.
 *
 * # Arguments
 *
 * * `text` - Text to check
 *
 * # Returns
 *
 * True if the text contains encoded data markers
 */
export function has_encoded_data(text: string): boolean;

export type InitInput = RequestInfo | URL | Response | BufferSource | WebAssembly.Module;

export interface InitOutput {
    readonly memory: WebAssembly.Memory;
    readonly encode_message: (a: number, b: number, c: number, d: number, e: number, f: number) => [number, number, number, number];
    readonly decode_message: (a: number, b: number, c: number, d: number) => [number, number, number, number];
    readonly has_encoded_data: (a: number, b: number) => number;
    readonly __wbindgen_externrefs: WebAssembly.Table;
    readonly __wbindgen_malloc: (a: number, b: number) => number;
    readonly __wbindgen_realloc: (a: number, b: number, c: number, d: number) => number;
    readonly __externref_table_dealloc: (a: number) => void;
    readonly __wbindgen_free: (a: number, b: number, c: number) => void;
    readonly __wbindgen_start: () => void;
}

export type SyncInitInput = BufferSource | WebAssembly.Module;

/**
 * Instantiates the given `module`, which can either be bytes or
 * a precompiled `WebAssembly.Module`.
 *
 * @param {{ module: SyncInitInput }} module - Passing `SyncInitInput` directly is deprecated.
 *
 * @returns {InitOutput}
 */
export function initSync(module: { module: SyncInitInput } | SyncInitInput): InitOutput;

/**
 * If `module_or_path` is {RequestInfo} or {URL}, makes a request and
 * for everything else, calls `WebAssembly.instantiate` directly.
 *
 * @param {{ module_or_path: InitInput | Promise<InitInput> }} module_or_path - Passing `InitInput` directly is deprecated.
 *
 * @returns {Promise<InitOutput>}
 */
export default function __wbg_init (module_or_path?: { module_or_path: InitInput | Promise<InitInput> } | InitInput | Promise<InitInput>): Promise<InitOutput>;
