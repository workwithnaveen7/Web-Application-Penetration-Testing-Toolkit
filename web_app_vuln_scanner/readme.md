# Web Application Vulnerability Scanner

This project is a web application vulnerability scanner that uses the OWASP ZAP (Zed Attack Proxy) API to perform automated scans on a target URL. The scanner identifies common vulnerabilities, generates a detailed report, and saves it as an HTML file.

## Features

- **Automated Scanning**: Initiates an active scan on the target URL using OWASP ZAP.
- **Vulnerability Detection**: Detects a wide range of web application vulnerabilities, including XSS, CSRF, SQL Injection, and more.
- **Report Generation**: Generates an HTML report summarizing the vulnerabilities found, including descriptions and the affected URLs.

## Requirements

- Python 3.x
- [OWASP ZAP](https://www.zaproxy.org/) installed and running locally or remotely
- Python `zapv2` module (`pip install python-owasp-zap-v2.4`)


## Usage

1. Run the Python script:
    ```bash
    python vuln_scanner.py
    ```

2. Enter the URL of the web application you want to scan when prompted.

3. The script will start the scan and display the progress in the terminal.

4. After the scan is completed, an HTML report named `vulnerability_report.html` will be generated in the project directory.

## Example
    ```bash
    $ python vuln_scanner.py
    Enter The URL: https://juice-shop.herokuapp.com/
    Accessing target URL: https://juice-shop.herokuapp.com/
    Starting active scan...
    Scan progress: 20%
    Scan progress: 40%
    Scan progress: 60%
    Scan progress: 80%
    Scan progress: 100%
    Scan completed.

## Configuration

- **API_KEY**: Your OWASP ZAP API key. Replace the placeholder in the script with your actual API key.
    ```python
    API_KEY = 'your-zap-api-key'  # Replace with your ZAP API key
    ```
- **ZAP_URL**: The URL where OWASP ZAP is running. The default is `http://localhost:8080`.
    ```python
    ZAP_URL = 'http://localhost:8080'  # ZAP's URL
    ```
- **TARGET_URL**: The URL of the target web application to scan. This can be entered at runtime.
    ```python
    TARGET_URL = input("Enter The URL:")  # Enter the target URL when prompted
    ```

## Output

- The scanner generates an HTML report (`vulnerability_report.html`) with a summary of the vulnerabilities detected, including:
    - **Affected URLs**: Links to the URLs where vulnerabilities were found.
    - **Vulnerability Names**: The type of vulnerability detected, such as XSS, CSRF, etc.
    - **Descriptions**: Brief descriptions of the vulnerabilities.

Example of the output in `vulnerability_report.html`:

```html
<html>
<head>
<title>Vulnerability Report</title>
</head>
<body>
<h1>Vulnerability Report</h1>
<p>Report for: <a href="https://juice-shop.herokuapp.com/">https://juice-shop.herokuapp.com/</a></p>
<p>Total vulnerabilities found: 3</p>
<ul>
    <li><a href="https://juice-shop.herokuapp.com/login">https://juice-shop.herokuapp.com/login</a> - XSS: Reflected XSS vulnerability</li>
    <li><a href="https://juice-shop.herokuapp.com/cart">https://juice-shop.herokuapp.com/cart</a> - CSRF: Cross-Site Request Forgery</li>
    <li><a href="https://juice-shop.herokuapp.com/admin">https://juice-shop.herokuapp.com/admin</a> - SQL Injection: SQL injection vulnerability</li>
</ul>
</body>
</html>

