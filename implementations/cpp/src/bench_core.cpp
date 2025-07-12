/*
 * Benchmark core encode/decode functions for C++ implementation.
 *
 * Build:
 *   g++ -O2 -I../include -o bench_core bench_core.cpp Encoder.cpp Decoder.cpp Utils.cpp Carrier.cpp Message.cpp Crypto.cpp
 *
 * Run:
 *   ./bench_core
 */
#include <iostream>
#include <string>
#include <chrono>
#include "Encoder.hpp"
#include "Decoder.hpp"

const int ITER = 1000;
const int MSG_REPEAT = 100;
const int CARRIER_REPEAT = 100;

int main() {
    std::string message, carrier, encoded, decoded;
    for (int i = 0; i < MSG_REPEAT; ++i) message += "Secret message";
    for (int i = 0; i < CARRIER_REPEAT; ++i) carrier += "This is the carrier text.";

    // Benchmark encode
    auto t0 = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < ITER; ++i) {
        encoded = Encoder::encode(message, carrier, "");
        if (encoded.empty()) { std::cout << "[WARN] encode error at iter " << i << std::endl; break; }
    }
    auto t1 = std::chrono::high_resolution_clock::now();
    double elapsed = std::chrono::duration<double>(t1 - t0).count();
    std::cout << "C++ encode: " << elapsed*1000 << " ms total, " << (elapsed/ITER)*1e6 << " us/call" << std::endl;

    // Benchmark decode
    t0 = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < ITER; ++i) {
        auto decodedVec = Decoder::decode(encoded, "");
        if (decodedVec.empty()) { 
            std::cout << "[WARN] decode error at iter " << i << std::endl; 
            break; 
        }
        decoded = decodedVec[0];
    }
    t1 = std::chrono::high_resolution_clock::now();
    elapsed = std::chrono::duration<double>(t1 - t0).count();
    std::cout << "C++ decode: " << elapsed*1000 << " ms total, " << (elapsed/ITER)*1e6 << " us/call" << std::endl;

    return 0;
} 