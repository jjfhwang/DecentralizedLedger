# DecentralizedLedger: A Python-Based Simplified Blockchain Implementation

This repository contains a Python implementation of a simplified blockchain, providing a foundational understanding of decentralized ledger technology.

## Detailed Description

This project aims to demystify the concepts behind blockchain technology by providing a concise and understandable Python implementation. While not intended for production use due to its simplified nature, it serves as an excellent educational tool for developers interested in learning how blockchains work under the hood. The core functionality encompasses creating blocks, chaining them together, validating the chain's integrity, and basic transaction handling. This implementation avoids external dependencies wherever possible to maximize clarity and minimize complexity.

The DecentralizedLedger project focuses on the fundamental aspects of blockchain, such as cryptographic hashing, proof-of-work (albeit simplified), and distributed consensus. It provides a clear and manageable codebase for developers to examine, modify, and experiment with. The simplicity allows for easier debugging and understanding of the underlying mechanisms. While more advanced features like smart contracts or sophisticated consensus algorithms are omitted for clarity, this foundational understanding can be extended to explore more complex blockchain systems.

The primary benefit of this project is its accessibility. It's designed to be easily understood by developers with basic Python knowledge. By stepping through the code, users can gain a practical understanding of blockchain principles. This is achieved through well-commented code, clear variable names, and a straightforward project structure. This project strives to be a stepping stone for developers who want to delve deeper into the world of blockchain technology and decentralized applications.

## Key Features

*   **Block Creation:** The system allows the creation of new blocks containing transaction data, a timestamp, and a reference to the previous block's hash. The `Block` class encapsulates this functionality, ensuring data integrity through hashing.
*   **Blockchain Chaining:** Blocks are linked together chronologically using cryptographic hash functions, forming an immutable chain. Each block contains the hash of the preceding block, creating a secure and tamper-proof record.
*   **Simplified Proof-of-Work:** A basic proof-of-work mechanism is implemented to simulate the computational effort required to add new blocks to the chain. This involves finding a nonce value that satisfies a specific difficulty target when hashed with the block data.
*   **Chain Validation:** The system includes a function to validate the integrity of the blockchain. This function iterates through the chain, verifying the hash of each block and ensuring that it matches the stored previous hash in the subsequent block. This ensures that the chain has not been tampered with.
*   **Transaction Handling:** A basic transaction model is included, allowing for the recording of simple data transfers between parties. Transaction details are stored within each block.
*   **Genesis Block:** The blockchain begins with a genesis block, which is the first block in the chain and has no preceding block. This provides the initial foundation for the chain.

## Technology Stack

*   **Python 3:** The primary programming language used for the entire project. Its readability and simplicity make it ideal for educational purposes.
*   **hashlib (Python Standard Library):** Used for cryptographic hashing of block data and transaction information. The SHA-256 algorithm is employed for its security and widespread adoption.
*   **datetime (Python Standard Library):** Used for timestamping each block with the time of its creation. This provides a chronological record of the blockchain's evolution.

## Installation

1.  **Clone the repository:** Open your terminal and execute the following command:
    git clone https://github.com/jjfhwang/DecentralizedLedger.git
2.  **Navigate to the project directory:**
    cd DecentralizedLedger
3.  **Create a virtual environment (recommended):**
    python3 -m venv venv
4.  **Activate the virtual environment:**
    *   On Linux/macOS: source venv/bin/activate
    *   On Windows: venv\Scripts\activate
5.  **Install dependencies (if any, although this project avoids external dependencies):**
    pip install -r requirements.txt (if a requirements.txt file exists)
6.  **Verify Installation:** Run the main script to ensure the environment is set up correctly.

## Configuration

This project currently does not require any external configuration files or environment variables. All parameters, such as the difficulty level for proof-of-work, are defined directly within the Python code. You can modify these parameters to experiment with different blockchain characteristics. For example, you can change the `difficulty` variable in the main script to adjust the computational effort required for mining new blocks.

## Usage

To run the blockchain simulation, execute the main Python script:

python3 main.py

This will create a blockchain, add some sample transactions, and validate the chain's integrity. The output will display the details of each block, including its hash, timestamp, and transaction data.

Example code snippet demonstrating block creation (not executable markdown):

class Block:
    def __init__(self, timestamp, transactions, previous_hash, nonce=0):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

Example code snippet demonstrating proof-of-work (not executable markdown):

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Block mined:", self.hash)

## Contributing

We welcome contributions to improve the DecentralizedLedger project. Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise code with comprehensive comments.
4.  Submit a pull request with a detailed description of your changes.
5.  Ensure your code adheres to PEP 8 style guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/jjfhwang/DecentralizedLedger/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to acknowledge the numerous online resources and tutorials that have helped in understanding and implementing blockchain technology. This project is built upon the collective knowledge and contributions of the open-source community.