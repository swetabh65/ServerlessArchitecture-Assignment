# Analyze Sentiment of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend


This project demonstrates how to automatically analyze the **sentiment of user reviews** using AWS Lambda and Amazon Comprehend. It uses Python and Boto3 to classify incoming text as **Positive**, **Negative**, **Neutral**, or **Mixed**.

---

## 📌 Objective

Automatically receive user reviews, process them via Amazon Comprehend, and log the sentiment analysis result using AWS Lambda.

---

## 🧰 Services Used

| AWS Service             | Purpose                                |
|-------------------------|----------------------------------------|
| **AWS Lambda**          | Serverless function to run analysis    |
| **Amazon Comprehend**   | NLP service to analyze sentiment       |
| **IAM**                 | Manage Lambda permissions              |
| **CloudWatch Logs**     | Store Lambda execution logs            |

---

## 📁 Project Structure


🟢 Step 1: Create IAM Role

![image](https://github.com/user-attachments/assets/0e7baa70-cd49-419f-9fa2-e00313c3ab3d)


🟢 Step 2: Create Lambda Function

![image](https://github.com/user-attachments/assets/8bb85476-f227-4c13-a496-3fed44ae6dc1)


🟢 Step 3: Lambda Function Code

![image](https://github.com/user-attachments/assets/982ac9c0-e4c2-4ac5-9daf-efee9325b270)


🟢 Step 4: Test the Lambda Function



