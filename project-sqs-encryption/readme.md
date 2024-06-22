# SQS Queue Encryption Script

This repository contains a Python script to encrypt unencrypted SQS queues using a specified KMS key across multiple AWS accounts. The script assumes an IAM role in each account to perform the necessary operations.

# Medium blog explaining this automation

https://medium.com/@akhilesh-mishra/python-for-devops-automating-sqs-encryption-for-enhanced-security-641a3d22a958

## Prerequisites

- Python 3.6+
- Boto3 library
- AWS credentials with the necessary permissions to assume roles and manage SQS queues

## Installation

1. Clone the repository or copy the scripts to your local machine.

2. Install the required Python packages:
    ```sh
    pip install boto3
    ```

## Usage

### Command Line Arguments

- `--accounts` or `-a`: List of AWS account IDs.
- `--role-name` or `-r`: Name of the IAM role to assume in each account.
- `--kms-key-id` or `-k`: KMS key ID to use for encryption.

### Running the Script

1. Ensure you have configured AWS credentials with the permissions to assume the specified role in each AWS account.

2. Run the script with the required arguments:
    ```sh
    python main.py --accounts 123456789012 987654321098 --role-name MyRoleName --kms-key-id my-kms-key-id
    ```

## Example

```sh
python main.py --accounts 123456789012 987654321098 --role-name MyRoleName --kms-key-id my-kms-key-id
