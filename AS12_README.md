# Auto-Scale EC2 Instances Based on Load Using AWS Lambda, Boto3, and SNS

This project demonstrates how to automatically scale Amazon EC2 instances based on network load using AWS Lambda, CloudWatch (EventBridge), and Amazon SNS. The Lambda function monitors Application Load Balancer (ALB) traffic and launches or terminates EC2 instances accordingly, sending notifications through SNS.

---

## 📌 Objective

Automatically:
- ✅ Launch an EC2 instance when ALB network load is **high**
- ✅ Terminate an EC2 instance when ALB load is **low**
- ✅ Send notifications via Amazon SNS for each scaling action

---

## 🛠️ Technologies & Services Used

- AWS Lambda (Python 3.x)
- Amazon EC2
- Application Load Balancer (ALB)
- Amazon CloudWatch / EventBridge
- Amazon SNS
- Boto3 SDK
- IAM Roles & Policies

---

## 📋 Setup Overview

### 🟢 1. Create IAM Role for Lambda

- Go to **IAM → Roles → Create Role**
- Select **Lambda**
- Attach these permissions:
  - `AmazonEC2FullAccess`
  - `CloudWatchReadOnlyAccess`
  - `AmazonSNSFullAccess`

---

### 🟢 2. Create the Lambda Function

- Go to **Lambda → Create Function**
- Runtime: **Python 3.x**
- Function name: `EC2AutoScaler`
- Assign the IAM role from Step 1
- Paste the Lambda code from [`lambda_function.py`](#)

> 🔧 Make sure to update:
> - `ALB_FULL_NAME`
> - `AMI_ID`, `Subnet ID`, `Security Group ID`
> - `SNS_TOPIC_ARN`

---

### 🟢 3. Create SNS Topic

- Go to **SNS → Topics → Create topic**
- Type: **Standard**
- Name: `Swetabh-EC2AutoScalerTopic`
- Copy the **Topic ARN**

💡 **Add an Email or SMS subscription** to receive notifications.

---

### 🟢 4. Create Application Load Balancer (ALB)

- Go to **EC2 → Load Balancers → Create**
- Type: **Application Load Balancer**
- Name: `Swetabh-AutoScaler-ALB-1`
- Create a **Target Group** and attach EC2 instances
- Use the ALB’s **Full Name** from its ARN:



---

### 🟢 5. Create CloudWatch Rule (EventBridge)

- Go to **EventBridge → Rules → Create Rule**
- Name: `Run-EC2AutoScaler-Every5Min`
- Type: `Schedule` → `rate(5 minutes)`
- Flexible Time Window: **Off**
- Target: `Lambda Function` → `EC2AutoScaler`  
(or specify ARN manually if not visible)

---

## ✅ Lambda Scaling Logic

- **If load > 80MB in 5 min** → Launch a new EC2 instance
- **If load < 20MB and more than 1 instance** → Terminate 1 instance
- **Else** → No action

All actions are logged and notified via SNS.

---

## 📊 Sample Logs (CloudWatch)

Average Load (NetworkIn): 91532485.00 bytes
🚀 High load detected. Launched a new EC2 instance.

Average Load (NetworkIn): 18924720.00 bytes
🧹 Low load detected. Terminated EC2 instance i-12345678


![image](https://github.com/user-attachments/assets/df883955-5f1b-447a-9339-ba1e17c204bb)



---


## 📬 Sample SNS Notification

Subject: EC2 AutoScaler Update
🚀 High load (91532485.00) - Launched a new EC2 instance.


---

## ✅ Final Checklist

- [x] Lambda deployed with proper VPC, AMI, Subnet, SG
- [x] CloudWatch rule triggers every 5 minutes
- [x] ALB metrics integrated
- [x] SNS topic with email/SMS subscription
- [x] IAM roles assigned securely

---

## 👨‍💻 Author

**Swetabh Sonal**  
Automating Cloud Infrastructure with 💡 and ☁️

---


