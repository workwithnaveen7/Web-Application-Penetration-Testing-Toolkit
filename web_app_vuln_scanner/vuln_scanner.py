from zapv2 import ZAPv2
import time

# Configuration
API_KEY = 'd0t812v737odei53lda18er4dk'  # Replace with your ZAP API key
ZAP_URL = 'http://localhost:8080'  # ZAP's URL
TARGET_URL = input("Enter The URL:")  # Replace with your target URL

def start_zap_scan(target_url):
    zap = ZAPv2(apikey=API_KEY, proxies={'http': ZAP_URL, 'https': ZAP_URL})
    
    print(f"Accessing target URL: {target_url}")
    zap.urlopen(target_url)
    time.sleep(5)  # Wait for the site to load
    
    print("Starting active scan...")
    scan_id = zap.ascan.scan(target_url, apikey=API_KEY)
    
    while int(zap.ascan.status(scan_id)) < 100:
        print(f"Scan progress: {zap.ascan.status(scan_id)}%")
        time.sleep(10)
    
    print("Scan completed.")
    
    return zap

def generate_report(zap, base_url):
    alerts = zap.core.alerts(baseurl=base_url)
    unique_alerts = list(set([(alert['url'], alert['alert'], alert['description']) for alert in alerts]))
    
    with open('vulnerability_report.html', 'w') as f:
        f.write('<html>\n<head>\n<title>Vulnerability Report</title>\n</head>\n<body>\n')
        f.write('<h1>Vulnerability Report</h1>\n')
        f.write(f'<p>Report for: <a href="{base_url}">{base_url}</a></p>\n')
        
        count = len(unique_alerts)
        f.write(f'<p>Total vulnerabilities found: {count}</p>\n')
        
        if unique_alerts:
            f.write('<ul>\n')
            for url, alert, description in unique_alerts:
                f.write(f'<li><a href="{url}">{url}</a> - {alert}: {description}</li>\n')
            f.write('</ul>\n')
        else:
            f.write('<p>No vulnerabilities detected.</p>\n')
        
        f.write('</body>\n</html>')

def main():
    zap = start_zap_scan(TARGET_URL)
    generate_report(zap, TARGET_URL)

if __name__ == "__main__":
    main()
