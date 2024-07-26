# AWS Lambda Function Manager
This repository contains a Python script for managing AWS Lambda functions. The script allows users to create and update Lambda functions with specified configurations, including roles, handlers, runtime environments, and network access settings. The script uses the boto3 library to interact with AWS Lambda and the zipfile module to package function code.

## Features
- Create and update AWS Lambda functions.
- Set roles, handlers, runtime environments, and network access settings for Lambda functions.
- Package Lambda function code into a zip file for deployment.

## Technologies Used
- Python: As the programming language.
- Boto3: For interacting with AWS Lambda.
- Zipfile: For packaging Lambda function code.

## Installation
1. Clone the repository to your local machine:

```sh
git clone https://github.com/yourusername/lambda-function-manager.git

```
2. Navigate to the project directory:
```sh

cd lambda-function-manager
```

3. Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```
4. Install the required packages:
```sh
pip install -r requirements.txt
```

## Usage
Configure the script with your AWS credentials. You can do this by setting up your AWS credentials file or by exporting the necessary environment variables:

```sh
export AWS_ACCESS_KEY_ID='your_access_key_id'
export AWS_SECRET_ACCESS_KEY='your_secret_access_key'
export AWS_DEFAULT_REGION='your_aws_region'
```
Example
```sh

python manage_lambda.py type=lambda name=your_function_name rolename=your_role_name handler=your_handler internetaccess=No intranetaccess=No runtime=python3.11 action=create newname=your_new_function_name
