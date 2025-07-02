# PixelFlow API: Serverless Image Processing 🌟

---

## 🚀 Project Overview

**PixelFlow API** is a robust, cost-effective, and highly scalable serverless image processing solution built on **Amazon Web Services (AWS)**. It demonstrates the power of cloud-native architecture to handle common image manipulation tasks—specifically resizing—on demand. This project highlights proficiency in serverless development, API design, and cloud infrastructure management.

---

## 🛠️ Problem Solved

Traditional image processing often requires dedicated servers, leading to high operational overhead and inefficient resource utilization. PixelFlow API addresses this by providing an event-driven, pay-per-use model for image resizing, making it ideal for web applications, mobile backends, or any scenario requiring dynamic image transformations without managing underlying infrastructure.

---

## 🎯 Key Benefits

- **Scalability:** Automatically scales to handle fluctuating loads, from zero requests to millions, without manual intervention.
- **Cost-Effectiveness:** Operates on a pay-per-execution model, significantly reducing costs compared to always-on servers.
- **Low Maintenance:** AWS manages the underlying infrastructure, minimizing operational overhead.
- **API-Driven:** Provides a clean, RESTful API endpoint for easy integration into other applications.

---

## ✨ Features

- **Image Resizing:** Dynamically resizes input images to specified dimensions while maintaining aspect ratio.
- **Grayscale Conversion:** Converts color images to grayscale.
- **Base64 Encoding/Decoding:** Handles image data efficiently via Base64 encoding for API transfer.
- **JPEG Quality Control:** Allows specification of output JPEG compression quality.
- **Serverless Architecture:** Leverages AWS Lambda and API Gateway for highly available and scalable processing.
- **Infrastructure as Code (IaC):** Deployed and managed using the Serverless Framework for repeatable and version-controlled infrastructure.

---

## 🧰 Technologies Used

**AWS Services:**
- **AWS Lambda:** Serverless compute service for running the image processing logic.
- **Amazon API Gateway:** Creates a RESTful API endpoint to trigger the Lambda function.
- **AWS IAM:** Manages secure access and permissions.
- **Amazon CloudWatch:** For monitoring and logging Lambda function invocations and errors.
- **AWS SSM Parameter Store:** Used by Serverless Framework for deployment metadata.

**Frameworks & Libraries:**
- **Serverless Framework (v4):** Orchestrates the deployment and management of AWS serverless resources.
- **Python 3.13:** Primary programming language for the Lambda function.
- **Pillow (PIL Fork):** Python Imaging Library for robust image manipulation.
- **requests:** Python library for making HTTP requests (used in the testing script).

**Tools:**
- **Docker Desktop:** Utilized by serverless-python-requirements for cross-platform dependency compilation.
- **AWS CLI:** Command-line interface for interacting with AWS services.
- **Node.js & npm:** Required for the Serverless Framework CLI.
- **Git:** Version control.

---

## 🏛️ Architecture

The PixelFlow API follows a classic serverless API pattern:

```text
+----------------+       +-------------------+       +-----------------+
|     Client     | ----> |   API Gateway     | ----> |   AWS Lambda    |
| (test_api.py)  |       | (REST Endpoint)   |       | (processImage)  |
+----------------+       +-------------------+       +--------+--------+
                                                                |
                                                                v
                                                        +-----------------+
                                                        |  Pillow (Image  |
                                                        |  Processing)    |
                                                        +--------+--------+
                                                                |
                                                                v
                                                        +-----------------+
                                                        |  CloudWatch     |
                                                        |  Logs           |
                                                        +-----------------+
```

---

## 🏁 Getting Started

### Prerequisites

- **AWS Account:** An active AWS account (be aware of AWS Free Tier limits).
- **Node.js & npm:** [Download Node.js (LTS)](https://nodejs.org/).
- **Serverless Framework CLI:**  
  ```bash
  npm install -g serverless
  ```
- **AWS CLI:** [Install AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- **Python 3.13:** [Download Python](https://www.python.org/downloads/)
- **Docker Desktop:** [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)
- **Git:** [Download Git](https://git-scm.com/)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pixel-flow-api.git
cd pixel-flow-api
```
*(Replace `YOUR_USERNAME` with your actual GitHub username)*

### 2. Local Setup

Create and activate a Python virtual environment, then install the necessary Python libraries:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows Command Prompt:
venv\Scripts\activate.bat
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Install Python dependencies
pip install Pillow requests

# Generate requirements.txt (crucial for Serverless deployment)
pip freeze > requirements.txt
```
*Ensure `requirements.txt` contains only Pillow and requests on separate lines.*

### 3. Configure AWS IAM User

- **Create a dedicated IAM user** with programmatic access.
- Attach these AWS managed policies:
  - AWSLambda_FullAccess
  - AmazonS3FullAccess
  - AmazonAPIGatewayAdministratorAccess
  - AWSCloudFormationFullAccess
  - CloudWatchLogsFullAccess
  - AmazonSSMFullAccess
  - IAMFullAccess (for Serverless Framework role creation)
- Configure your AWS CLI:
  ```bash
  aws configure
  ```
  *(Paste Access Key ID, Secret Access Key, set default region, and output format)*

### 4. Update Serverless Configuration

Open `serverless.yml` and ensure it matches your deployment needs (see sample in repo).

### 5. Install Serverless Plugin

```bash
npm install serverless-python-requirements --save-dev
```

### 6. Deploy the API

With Docker Desktop running and your virtual environment activated:

```bash
serverless deploy
```
*Upon successful deployment, the terminal will output your API endpoint URL.*

---

## 🧪 Usage and Testing

1. **Update `test_api.py`:**  
   Replace the API endpoint with your deployed URL.

2. **Place an input image:**  
   Ensure `input_image.jpg` is in the same directory as `test_api.py`.
   

3. **Run the test script:**
   ```bash
   python test_api.py
   ```
   The script will send the image to your API, print the response, and save the processed image as `api_processed_output.jpg`.
   

4. **Check Results:**  
   - Terminal output for "Image processed successfully!"
   - Open `api_processed_output.jpg` to confirm resizing.
   - Check AWS CloudWatch Logs for Lambda execution details.

## 🖼️ Examples
Here are examples of image transformations using the PixelFlow API:

**Original Input Image:**

![Input Image](assests/input_image_example.png)

**Grayscale Transformation:**

![Grayscale Output](assests/grayscaled_image_example.png)

**API Processed Output:**

![API Processed Output](assests/api_processed_image_example.png)


---

## 💡 Key Learnings & Challenges

- **Serverless Architecture Design:** Practical implementation of Lambda and API Gateway for scalable solutions.
- **Infrastructure as Code (IaC):** Experience with the Serverless Framework for consistent, reproducible deployments.
- **AWS IAM Best Practices:** Secure, least-privilege access for deployments.
- **Cross-Platform Dependency Management:** Using Docker and serverless-python-requirements to package Python libraries for Lambda.
- **Cloud Debugging:** Leveraging CloudWatch logs for troubleshooting.
- **API Design & Data Transfer:** Efficient binary data transfer using Base64 encoding.

---

## ⏭️ Future Enhancements

- **Asynchronous Processing:** Integrate with S3 and SQS/SNS for large images and async workflows.
- **Image Format Conversion:** Support for PNG, WebP, etc.
- **Additional Transformations:** Watermarking, cropping, filters.
- **Enhanced Error Handling:** Better reporting and notifications.
- **Client-Side Integration:** Simple web or mobile frontend.

---

## 🧹 Cleanup

To avoid AWS charges, remove all deployed resources when done:

```bash
serverless remove
```
*Repeat for each region if deployed to multiple regions.*

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ✍️ Author

**[Sarim Javed]**  
[https://github.com/sarimjaved12]  
[www.linkedin.com/in/sarim-javed-9147a0328]

---

> **Note to Employers:**  
> While this project may not be actively deployed to minimize costs, the comprehensive documentation and well-structured codebase demonstrate my ability to design, implement, deploy, and debug a serverless application end-to-end. I am prepared to discuss any aspect of this project in detail.
