# SQL Injection Testing Automation Tool

This Python-based tool is designed to scan a given URL for SQL injection vulnerabilities. It uses both direct payload testing and SQLMap for automated vulnerability detection and generates a comprehensive HTML report.

## Features

- **Automated SQL Injection Testing:** Scans for common SQL injection vulnerabilities using a set of predefined payloads.
- **SQLMap Integration:** Utilizes SQLMap for advanced testing and extracting vulnerabilities from the URL.
- **Concurrency:** Uses multithreading to speed up the testing process.
- **HTML Report Generation:** Produces an HTML report summarizing the findings, including a count of vulnerabilities and links to affected URLs.

## Requirements

- Python 3.x
- `requests` library
- SQLMap installed and configured on your system


## Usage

1. **Run the Tool:**
   ```bash
   python sql_injection.py

2. **Enter the Base URL: When prompted, input the URL you want to test for SQL injection vulnerabilities.**

3. **View the Report: After the scan completes, check the generated HTML report named report_sql.html in the project directory.**

