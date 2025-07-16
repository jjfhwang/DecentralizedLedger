# DecentralizedLedger: A Byzantine Fault-Tolerant, Cryptographically Verifiable Ledger

This repository contains a Python implementation of a Merkleized Directed Acyclic Graph (DAG) designed for tracking decentralized state transitions. It provides a secure, tamper-proof, and Byzantine fault-tolerant ledger for applications requiring a high degree of data integrity and consensus across a distributed network.

This project aims to provide a robust foundation for building decentralized applications, particularly those requiring immutable and auditable records of state changes. Unlike traditional blockchains which rely on linear chains of blocks, this implementation leverages a DAG structure. This allows for concurrent transactions and potentially higher throughput by enabling parallel processing of state updates. The use of Merkle trees within the DAG provides efficient data verification and ensures that any attempt to alter the ledger's history will be easily detectable. Furthermore, the system is designed to be resilient to Byzantine faults, meaning it can continue to operate correctly even if some nodes in the network are compromised or malicious.

The primary goal is to facilitate the development of decentralized systems that require high levels of security and trust. The ledger's structure allows for the efficient recording and verification of complex state transitions, making it suitable for various applications such as supply chain management, digital asset tracking, and decentralized identity verification. By providing a cryptographically verifiable and tamper-proof record of events, DecentralizedLedger empowers developers to build applications where data integrity is paramount. It promotes transparency and accountability by ensuring that all state transitions are recorded and verifiable by all participants.

The system is designed to be modular and extensible, allowing developers to customize the consensus mechanisms and data validation rules to fit their specific needs. The provided implementation includes a basic consensus algorithm suitable for smaller, permissioned networks. However, it can be readily adapted to incorporate more sophisticated Byzantine Fault Tolerance (BFT) algorithms for larger, more open networks. The use of Python facilitates rapid prototyping and experimentation, allowing developers to quickly iterate on their designs and test different configurations.

## Key Features

*   **Merkleized DAG Structure:** Transactions are organized in a Directed Acyclic Graph (DAG) where each node represents a state transition. Each node's hash is calculated based on the Merkle root of the included transactions, ensuring data integrity and efficient verification.
*   **Byzantine Fault Tolerance (BFT) Foundation:** The system is designed with BFT principles in mind, allowing it to tolerate a certain number of faulty or malicious nodes. The current implementation provides a basic consensus mechanism that can be replaced with more advanced BFT algorithms.
*   **Cryptographic Verification:** All state transitions are cryptographically signed, ensuring authenticity and non-repudiation. Each node contains the signatures of participating nodes, providing an auditable trail of consensus.
*   **Efficient Data Verification:** Merkle trees enable efficient verification of individual transactions without requiring the entire ledger to be downloaded. This allows for lightweight clients to participate in the network and verify the integrity of specific data points.
*   **Modular Architecture:** The system is designed with a modular architecture, allowing for easy customization and extension. Developers can replace components such as the consensus algorithm, data validation rules, and storage mechanisms.
*   **Python Implementation:** The use of Python allows for rapid prototyping and experimentation. The code is well-documented and easy to understand, making it accessible to a wide range of developers.
*   **Concurrent Transaction Processing:** The DAG structure allows for the parallel processing of transactions, potentially increasing throughput compared to traditional blockchain implementations.

## Technology Stack

*   **Python 3.7+:** The primary programming language used for the implementation.
*   **Cryptographic Libraries (e.g., `cryptography` package):** Used for generating cryptographic signatures and hashing data. This ensures the security and integrity of the ledger.
*   **Data Serialization (e.g., `pickle` or `json`):** Used for serializing and deserializing data structures for storage and transmission. Choose a library based on performance and security requirements.
*   **Database (e.g., SQLite, LevelDB, or PostgreSQL):** Used for storing the ledger data. The choice of database depends on the performance and scalability requirements of the application. SQLite is suitable for smaller, single-node deployments, while LevelDB or PostgreSQL may be more appropriate for larger, distributed networks.
*   **Networking Library (e.g., `asyncio` or `Twisted`):** Used for communication between nodes in the network. `asyncio` is a built-in library that provides asynchronous I/O capabilities. Twisted is a more mature and feature-rich networking framework.

## Installation

1.  **Clone the repository:**
    git clone https://github.com/jjfhwang/DecentralizedLedger.git
    cd DecentralizedLedger

2.  **Create a virtual environment:**
    python3 -m venv venv

3.  **Activate the virtual environment:**
    source venv/bin/activate  (Linux/macOS)
    venv\Scripts\activate  (Windows)

4.  **Install the required dependencies:**
    pip install -r requirements.txt

5.  **Verify Installation:** Run the sample node to ensure the correct installation.
    python3 run_node.py --node_id 1 --port 5001

## Configuration

The system can be configured using environment variables and configuration files.

*   **NODE_ID:** A unique identifier for each node in the network. This is used to identify the node in the consensus process.
*   **PORT:** The port number on which the node will listen for incoming connections.
*   **DATABASE_PATH:** The path to the database file where the ledger data will be stored.
*   **CONSENSUS_ALGORITHM:** Specifies the consensus algorithm to be used. The default algorithm is a simple majority-based algorithm.
*   **INITIAL_NODES:** A comma-separated list of initial nodes in the network. These nodes will be used to bootstrap the network. Format: `node_id@ip_address:port`.

Environment variables can be set in the `.env` file. An example `.env` file is provided in the repository.

## Usage

The `run_node.py` script starts a node in the decentralized ledger network.

Example usage:

python3 run_node.py --node_id 1 --port 5001

This command starts a node with ID 1, listening on port 5001.

The system provides a basic API for interacting with the ledger:

*   **`add_transaction(transaction_data)`:** Adds a transaction to the ledger. The `transaction_data` must be a dictionary containing the transaction details.
*   **`get_state(key)`:** Retrieves the current state for a given key.
*   **`verify_transaction(transaction_id)`:** Verifies the validity of a transaction.

Detailed API documentation will be provided in a separate document.

## Contributing

We welcome contributions to this project! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Write tests to cover your changes.
5.  Submit a pull request.

Please ensure that your code adheres to the project's coding style and that all tests pass before submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/jjfhwang/DecentralizedLedger/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the open-source community for their contributions to the tools and libraries used in this project.