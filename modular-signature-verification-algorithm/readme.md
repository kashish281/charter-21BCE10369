# charter-21BCE10369-modular-signature-verification-algorithm
# Modular Signature Verification Algorithm

This project implements a flexible algorithm to verify digital signatures across multiple signature schemes, including ECDSA and Schnorr. 

## Features
- Recognizes and supports various signature schemes.
- Optimized for low time complexity to minimize gas usage.

## Setup Instructions
See [docs/setup_instructions.md](docs/setup_instructions.md) for setup and usage.

## Usage Example
```python
from src.signature_verifier import SignatureVerifier

verifier = SignatureVerifier()
result = verifier.verify_signature(address, signature_data, signed_hash, scheme_type="ecdsa")
print("Signature valid:", result)
