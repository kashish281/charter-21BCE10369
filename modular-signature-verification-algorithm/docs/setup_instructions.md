# Setup Instructions

## Prerequisites
- Python 3.x installed on your system.
- Clone this repository or download the source code.

## Installation
1. Navigate to the project directory:


## Usage
To use the `SignatureVerifier` class, import it and call `verify_signature` with appropriate parameters.

2. (Optional) Set up a virtual environment:
 
3. Install any required packages (if needed).

## Running Tests
Run the tests with the following command:



Example:
```python
from src.signature_verifier import SignatureVerifier

verifier = SignatureVerifier()
result = verifier.verify_signature("0xExampleAddress", b"\x00\x01", b"\x00" * 32, "ecdsa")
print("Signature valid:", result)


