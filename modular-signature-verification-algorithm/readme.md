# Technical Documentation: Modular Signature Scheme Verification Algorithm

This project implements a flexible algorithm to verify digital signatures across multiple signature schemes, including ECDSA and Schnorr.

## Features
- **Multi-Signature Scheme Support**: Recognizes and supports various signature schemes.
- **Optimized Performance**: Optimized for low time complexity to minimize gas usage.

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system.
- Clone this repository or download the source code.

### Installation
1. Navigate to the project directory:
    ```bash
    cd path/to/project-directory
    ```

2. (Optional) Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install any required packages (if needed):
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To use the `SignatureVerifier` class, import it and call `verify_signature` with appropriate parameters.

### Running Tests
Run the tests with the following command:
    ```bash
    python -m unittest discover tests

 -------------------------------------------------------
 
## Special Thanks

I would like to extend my gratitude to **CharterLabs** for giving me the opportunity to work on this project as a part of their Qualifier Round assignment. I appreciate the time and effort they took to evaluate my skills and provide me with a chance to showcase my abilities. Thank you for the experience.
<br>
**contact-kashishsin28@gmail.com**
