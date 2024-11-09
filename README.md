# Task-1: Merkle Proof Verification of Blockchain Transactions

## Overview
This solution enables the verification of transaction inclusion in a Merkle tree using an Ethereum smart contract. It integrates with a React-based frontend, which allows users to interact with the smart contract by fetching and setting a Merkle Root and verifying transactions using Merkle proofs. The solution incorporates a user-friendly UI with MetaMask integration for Ethereum wallet interaction.

## Features
- **Merkle Root Fetching**: Fetch the current Merkle Root stored in the contract.
- **Setting a New Merkle Root**: Allow users to set a new Merkle Root if they are the owner of the contract.
- **Transaction Verification**: Users can verify the inclusion of a transaction in the Merkle tree by providing a transaction hash and its Merkle proof.

## High-Level Architecture
- **Frontend**: ReactJS-based frontend using Web3.js to interact with the Ethereum blockchain and the smart contract.
- **Backend (Blockchain)**: Ethereum-based smart contract deployed on the Ethereum blockchain that handles Merkle root management and transaction verification.
- **Wallet Integration**: MetaMask extension for handling user accounts and interacting with Ethereum.

## 1. Smart Contract Design
The smart contract serves as the core of the solution. The contract handles the storage of the Merkle Root and the verification of transactions within the Merkle tree.

### Contract Features:
- `setMerkleRoot`: Allows the contract owner to set the Merkle Root.
- `verifyTransactionInclusion`: Verifies whether a transaction is part of the Merkle tree, given the transaction hash and the Merkle proof.
- `owner`: Stores the contract owner’s address.
- `merkleRoot`: Stores the current Merkle root, which represents the root of the Merkle tree for the stored transactions.

## 2. Frontend Implementation (ReactJS with Web3.js)
The frontend allows users to interact with the smart contract functions using the MetaMask wallet for Ethereum transaction signing.

### Steps:
1. **Initialize Web3.js**: Establish the connection to the Ethereum blockchain using the user's MetaMask account.
2. **Interacting with Smart Contract**: Use Web3.js to call smart contract functions such as `setMerkleRoot`, `verifyTransactionInclusion`, and `fetchMerkleRoot`.
3. **User Input Forms**: Allow users to input a new Merkle root, transaction hash, and proof to interact with the contract.

### Dependencies:
- `web3.js`: For interacting with the Ethereum blockchain.
- `react`: For building the frontend UI.
- `react-dom`: For rendering the UI components.
- `ethers`: Optional for easier interaction with Ethereum contracts.

### Install required dependencies:
    ```bash
    npm install web3 react

## 3. User Interface Design:
The frontend user interface (UI) is designed to be intuitive and responsive. It consists of three main functionalities:
- **Fetch Merkle Root**: A button to fetch and display the current Merkle root stored in the contract.
- **Set Merkle Root**: An input field for setting a new Merkle root and a button to trigger the contract's `setMerkleRoot` function.
- **Verify Transaction Inclusion**: Two input fields (one for transaction hash and one for the Merkle proof) and a button to verify transaction inclusion using the `verifyTransactionInclusion` function.


## 4. Deployment and Hosting

### Deploy Smart Contract:
Deploy the smart contract on Ethereum using Truffle, Hardhat, or Remix IDE. After deployment, obtain the contract address and ABI.

#### Example using Truffle:
1. Write migration scripts.
2. Deploy using `truffle migrate`.

### Deploy Frontend:
Host the React frontend using services like Netlify, Vercel, or GitHub Pages. Make sure that the frontend is connected to the deployed smart contract on Ethereum.

#### Example with Netlify:
1. Build the React app:
    ```bash
    npm run build
    ```
2. Deploy the build folder to Netlify.

## 5. MetaMask Integration
MetaMask provides the wallet connection to interact with the Ethereum blockchain. Users can use their MetaMask extension to sign transactions and interact with the contract. The React app automatically detects MetaMask and prompts the user to connect their wallet.

## Conclusion
This solution provides an easy-to-use interface for users to:
- Interact with a smart contract deployed on Ethereum.
- Set and fetch Merkle roots.
- Verify transaction inclusion in a Merkle tree.

By integrating Web3.js with React and leveraging MetaMask for Ethereum wallet interaction, users can seamlessly interact with the blockchain while verifying the validity of transactions using Merkle proofs.

 -------------------------------------------------------

# Task-3: Modular Signature Scheme Verification Algorithm

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

### Example Test Code:
    import unittest
    from src.signature_verifier import SignatureVerifier

    class TestSignatureVerifier(unittest.TestCase):
    def setUp(self):
        self.verifier = SignatureVerifier()

    def test_verify_signature_ecdsa(self):
        address = "0xExampleAddress"
        signature_data = b"\x00\x01"
        signed_hash = b"\x00" * 32
        result = self.verifier.verify_signature(address, signature_data, signed_hash, "ecdsa")
        self.assertTrue(result)

    def test_verify_signature_schnorr(self):
        address = "0xExampleAddress"
        signature_data = b"\x00\x02"
        signed_hash = b"\x00" * 32
        result = self.verifier.verify_signature(address, signature_data, signed_hash, "schnorr")
        self.assertTrue(result)

     if __name__ == '__main__':
     unittest.main()


 --------------------------------------------------------------------------------------------------
 
## Special Thanks

I would like to extend my gratitude to **CharterLabs** for giving me the opportunity to work on this project as a part of their Qualifier Round assignment. I appreciate the time and effort they took to evaluate my skills and provide me with a chance to showcase my abilities. Thank you for the experience.
<br>
**contact-kashishsin28@gmail.com**



