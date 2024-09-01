# 🌐 Web Application Penetration Testing Toolkit 🛡️

Welcome to the **Web Application Penetration Testing Toolkit** – your go-to resource for automating the discovery of web application vulnerabilities! This toolkit provides two powerful tools to help you identify and mitigate potential security threats in your web applications.

## 🚀 Toolkit Overview

This repository contains two distinct tools, each designed for specific vulnerability testing:

### 1️⃣ SQL Injection Testing Automation Tool
- **Description**: A Python-based tool designed to scan for SQL injection vulnerabilities. It uses both direct payload testing and SQLMap for automated detection, generating a comprehensive HTML report.
- **Key Features**:
  - **Automated Detection**: Leverages SQLMap along with custom payloads.
  - **HTML Reporting**: Detailed HTML report of detected SQL injection vulnerabilities.
- **Folder**: `sql-injection-automation`

### 2️⃣ Web Application Vulnerability Scanner
- **Description**: Utilizes the OWASP ZAP (Zed Attack Proxy) API to perform automated vulnerability scans on a target URL, identifying a range of common vulnerabilities and generating a detailed report.
- **Key Features**:
  - **Automated Scans**: Conducts scans on any target URL.
  - **Detailed Reports**: Generates an HTML report summarizing detected vulnerabilities.
- **Folder**: `web-app-vuln-scanner`

## 🛠️ Getting Started

To get started with the tools in this repository, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/workwithnaveen7/Web-Application-Penetration-Testing-Toolkit.git
    cd web-application-penetration-testing-toolkit
    ```

2. **Navigate to the Desired Tool**:
   - For SQL Injection Testing Automation: `cd sql-injection-automation-tool`
   - For Web Application Vulnerability Scanner: `cd web-app-vuln-scanner`

3. **Install Required Packages**:
   - For SQL Injection Testing Automation:
     ```bash
     pip install -r requirements.txt
     ```
   - For Web Application Vulnerability Scanner:
     ```bash
     pip install python-owasp-zap-v2.4
     ```

4. **Run the Tools**:
   - For SQL Injection Testing Automation:
     ```bash
     python sql_injection_automation.py -u https://example.com/login
     ```
   - For Web Application Vulnerability Scanner:
     ```bash
     python vuln_scanner.py
     ```

## 📋 Configuration

### SQL Injection Testing Automation Tool
- **SQLMap**: Ensure SQLMap is installed and configured correctly.

### Web Application Vulnerability Scanner
- **API_KEY**: Set your OWASP ZAP API key in the script.
    ```python
    API_KEY = 'your-zap-api-key'
    ```
- **ZAP_URL**: URL where OWASP ZAP is running.
    ```python
    ZAP_URL = 'http://localhost:8080'
    ```
- **TARGET_URL**: Enter the target URL when prompted.

## 📊 Output

- **SQL Injection Testing Automation**: Generates an HTML report summarizing SQL injection vulnerabilities.
- **Web Application Vulnerability Scanner**: Produces an HTML report with a summary of all detected vulnerabilities.


---

Enhance your web application's security with the **Web Application Penetration Testing Toolkit**! 🌐🛡️

