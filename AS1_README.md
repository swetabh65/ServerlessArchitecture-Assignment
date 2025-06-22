# Automated Instance Management Using AWS Lambda and Boto3

## Objective
Automate EC2 instance management using AWS Lambda and Boto3.

## AWS Services Used
- EC2
- Lambda
- IAM
- Boto3 (Python)

## Solution Summary
- 2 EC2 instances created:
  - **Auto-Stop**: Stops via Lambda.
  - **Auto-Start**: Starts via Lambda.
- Lambda Python function checks EC2 tags and manages their state.

## Steps Performed
1. **EC2 Instances**:
   - Created 2 t2.micro instances.
   - Tagged: `Action=Auto-Stop` & `Action=Auto-Start`.
  
    ![image](https://github.com/user-attachments/assets/349f241a-65d9-43fb-8542-9526c4bcaa67)


2. **IAM Role**:
   - Created LambdaEC2ControlRole with AmazonEC2FullAccess.
  
    ![image](https://github.com/user-attachments/assets/dcaf5499-3fc9-43e4-9528-b76196b0a81f)


3. **Lambda Function**:
   - Python 3.12 function using Boto3.
   - Filters instances using tags and starts/stops accordingly.
  
    ![image](https://github.com/user-attachments/assets/f9bcef9b-ee15-4054-8110-eee3bb17918a)


4. **Testing**:
   - Manual Lambda trigger.
   - Verified EC2 state changes in the AWS Console.
  
   ![image](https://github.com/user-attachments/assets/a5a4736c-c75b-459f-b7c2-0d0a4e3b1d32)


## Files
- `lambda_function.py`: Lambda code.
- `README.md`: This documentation.
- `screenshots/`: AWS setup and testing screenshots.

## Screenshots
*(Add screenshots here — IAM Role, EC2 tags, Lambda Test, EC2 state change)*
