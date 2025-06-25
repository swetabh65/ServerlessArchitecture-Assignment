# Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3


This project demonstrates how to **automatically tag newly launched EC2 instances** with custom metadata using AWS Lambda and EventBridge. It ensures consistent tagging for easier billing, management, and automation across AWS infrastructure.

---

## 📌 Objective

Automatically apply two tags to any EC2 instance launched in the AWS Oregon region:

- `LaunchDate`: The UTC date the instance was launched.
- `Owner`: Custom tag (e.g., `SwetabhSonal`) for ownership tracking.

---

## 🧰 Tools & Services Used

| Tool/Service       | Purpose                           |
|--------------------|------------------------------------|
| **AWS Lambda**     | Run Boto3 script on EC2 launch     |
| **EventBridge**    | Trigger Lambda on EC2 state change |
| **IAM Role**       | Allow Lambda to tag EC2 instances  |
| **Boto3 (Python)** | Script logic for tagging           |
| **CloudWatch**     | Monitor Lambda execution logs      |

---

## 📁 Project Structure

🟢 Step 1: IAM Role for Lambda

![image](https://github.com/user-attachments/assets/158ebb7a-2a4c-4e57-9685-bf8967d652e4)


🟢 Step 2: Create the Lambda Function

![image](https://github.com/user-attachments/assets/4c502e03-0e0a-4202-8264-d668688f6a11)


🟢 Step 2: Create the Lambda Function
