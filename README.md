# Local Hosted Password Manager

A secure password manager implemented in Python using MySQL for storing hashes, SHA256 for hashing the master password, PBKDF2 for key hashing, and AES for encryption.

## Features

- **Secure Storage**: All passwords are securely stored using AES encryption.
- **Master Password**: Uses a strong master password hashed with SHA256 for access.
- **Key Hashing**: Implements PBKDF2 for deriving encryption keys, enhancing security.
- **MySQL Database**: Password hashes are stored in a MySQL database.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- MySQL database installed and running.
- Python packages: `mysql-connector-python`, `cryptography`.

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/password-manager.git
    ```

2. Install the required Python packages:

    ```bash
    pip install mysql-connector-python cryptography
    ```

3. Set up your MySQL database by importing the `schema.sql` file:

    ```bash
    mysql -u your_username -p your_database_name < schema.sql
    ```

4. Update the `config.py` file with your MySQL database connection details:

    ```python
    DB_HOST = 'localhost'
    DB_USER = 'your_username'
    DB_PASSWORD = 'your_password'
    DB_NAME = 'your_database_name'
    ```

## Usage

1. Run the main script:

    ```bash
    python password_manager.py
    ```

2. Follow the prompts to:
    - Create a master password.
    - Add, retrieve, update, or delete passwords.

## Security

- **Master Password**: Ensure your master password is strong and kept confidential.
- **Database Security**:
# PasswordManager
