#!/bin/bash

HWID="hw:4,0,0"
SLEEP="3"

bytes=""
for pad in {0..63}; do
    bytes+="$(printf '%02x%02x%02x' 0x96 "${pad}" "${pad}")"
done
amidi -p "${HWID}" -S "${bytes}"

bytes=""
for button in $(seq 0x64 0x6B) $(seq 0x70 0x77); do
    bytes+="$(printf '%02x%02x%02x' 0x90 "${button}" 0x01)"
done
amidi -p "${HWID}" -S "${bytes}"

sleep "${SLEEP}"

bytes=""
for pad in {0..63}; do
    bytes+="$(printf '%02x%02x%02x' 0x96 "${pad}" "$((pad + 64))")"
done
amidi -p "${HWID}" -S "${bytes}"

bytes=""
for button in $(seq 0x64 0x6B) $(seq 0x70 0x77); do
    bytes+="$(printf '%02x%02x%02x' 0x90 "${button}" 0x02)"
done
amidi -p "${HWID}" -S "${bytes}"

sleep "${SLEEP}"

amidi -p "${HWID}" -S "F0477F4F240008003F000000000000F7"
bytes=""
for button in $(seq 0x64 0x6B) $(seq 0x70 0x77); do
    bytes+="$(printf '%02x%02x%02x' 0x90 "${button}" 0x00)"
done
amidi -p "${HWID}" -S "${bytes}"
