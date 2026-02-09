# Network OSINT & Port Scanner

<div align="center">

![Version](https://img.shields.io/badge/version-2.5-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen)
![Exports](https://img.shields.io/badge/exports-TXT%20%7C%20JSON%20%7C%20CSV-blue)

**Advanced IP Reconnaissance & Port Discovery Tool**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [API Keys](#api-keys) • [Examples](#examples) • [Contributing](#contributing)

</div>

---

## 🔍 Overview

**Network OSINT & Port Scanner** is a powerful command-line tool for comprehensive IP reconnaissance. Combine geolocation tracking, threat detection, and advanced port scanning with a user-friendly interactive menu system.

Perfect for:
- Security researchers
- Network administrators
- Penetration testers
- OSINT investigations
- Network reconnaissance

---

## ✨ Features

- **⚡ Professional UI** - Beautiful color-coded output with ASCII art banner
- **🌍 Comprehensive IP Geolocation** - Coordinates, timezone, currency, language, continent, ASN, RIR lookup  
- **🔌 Advanced Port Scanning** - Scan any port range from 1-65535 with real-time discovery
- **🛡️ Enhanced Security Detection** - 9 security flags: VPN, Proxy, Hosting, Datacenter, Tor, Residential, Mobile, Home Proxy, Premium
- **📊 Threat Assessment** - Real-time threat level evaluation with multiple security indicators
- **📈 Progress Tracking** - Live visual progress bar with percentage and block visualization
- **📁 Batch Processing** - Scan multiple targets from a file
- **💾 Multi-Format Exports** - Save reports as TXT, JSON, and CSV simultaneously with all data
- **🌐 Global Information** - Currency, language, timezone for each IP location
- **📱 Dual Mode Interface** - Interactive menu system or direct command-line arguments

---

## 🚀 Quick Start

## 🚀 Quick Start (2 Minutes)

```bash
# 1. Clone and install
git clone https://github.com/xdrew87/network-osint-scanner.git
cd network-osint-scanner
pip install -r requirements.txt

# 2. Run your first scan
python main.py 8.8.8.8

# 3. Check the generated reports
# - report_8.8.8.8_*.txt
# - report_8.8.8.8_*.json  
# - report_8.8.8.8_*.csv
```

---

## 📖 Usage Guide

### Interactive Mode (Recommended)

Run without arguments to access the menu:

```bash
python main.py
```

**Menu Options:**
- **[1] Full OSINT Scan** - Complete reconnaissance with geolocation + custom port range
- **[2] Port Scan Only** - Fast port scanning for targeted analysis
- **[3] Quick OSINT** - Speed-optimized scan using common ports
- **[4] Batch Scan** - Concurrent scanning of multiple targets from file
- **[5] Help & Documentation** - Built-in usage guide and examples
- **[0] Exit** - Quit the application

### Command Line Mode

```bash
# Scan a specific IP
python main.py 8.8.8.8

# Scan a domain
python main.py google.com

# Then enter port range when prompted
```

### Batch Scanning

Create a file with one IP/domain per line:

```bash
# ips.txt
8.8.8.8
google.com
cloudflare.com
1.1.1.1
```

Then select option [4] from the menu and specify `ips.txt`

---

## 🔑 API Keys (Optional)

For enhanced threat detection, add your API keys:

### IPQualityScore API

1. Sign up at https://ipqualityscore.com
2. Get your API key
3. Edit `main.py` and replace `YOUR_IPQUALITYSCORE_API_KEY` with your key

```python
IPQS_API_KEY = "your_actual_api_key_here"
```

### VPNAPI.io API

1. Sign up at https://vpnapi.io
2. Get your API key
3. Edit `main.py` and replace `YOUR_VPNAPIIO_API_KEY` with your key

```python
VPNAPIIO_API_KEY = "your_actual_api_key_here"
```

---

## 📊 Export Formats

Every scan automatically generates **three report formats**:

### Text Report (.txt)
Human-readable format with complete geolocation and security information:
```
OSINT REPORT FOR 1.1.1.1
══════════════════════════════════════════════════════════════
GEO-IP DATA:
  IP Address:          1.1.1.1
  Hostname:            one.one.one.one
  Country:             Hong Kong (HK)
  City:                Hong Kong
  Region:              Central and Western District
  Continent:           Asia
  Latitude:            22.3193
  Longitude:           114.1693
  Accuracy Radius:     1000 km
  Timezone:            Asia/Hong_Kong
  Currency:            Hong Kong Dollar (HKD)
  Language:            Mandarin Chinese (zh)
  ISP:                 Cloudflare, Inc
  Organization:        APNIC and Cloudflare DNS Resolver project
  ASN:                 AS13335 Cloudflare, Inc.
  Connection Type:     Hosting
  Threat Level:        medium

SECURITY FLAGS:
  VPN Detected:        False
  Proxy Detected:      False
  Hosting Provider:    True
  Datacenter:          False
  Tor Network:         False
  Residential:         False
  Mobile Network:      False
  Premium Data:        False

PORT SCAN RESULTS:
  Open Ports: 80, 443
```

### JSON Export (.json)
Structured data for automation and integration:
```json
{
  "metadata": {
    "scan_date": "2026-02-09T15:30:45Z",
    "target_ip": "1.1.1.1",
    "scanner": "Network OSINT Scanner v2.5",
    "api_source": "suicixde.com"
  },
  "geolocation": {
    "ip": "1.1.1.1",
    "hostname": "one.one.one.one",
    "country": "Hong Kong",
    "country_code": "HK",
    "city": "Hong Kong",
    "latitude": 22.3193,
    "longitude": 114.1693,
    "accuracy_radius": 1000,
    "timezone_name": "Asia/Hong_Kong",
    "utc_offset": 28800,
    "currency_code": "HKD",
    "currency_name": "Hong Kong Dollar",
    "language_code": "zh",
    "language_name": "Mandarin Chinese",
    "isp": "Cloudflare, Inc",
    "org": "APNIC and Cloudflare DNS Resolver project",
    "asn": "AS13335",
    "asn_number": "13335",
    "asn_org": "Cloudflare, Inc.",
    "rir": "APNIC",
    "connection_type": "Hosting",
    "threat_level": "medium",
    "is_vpn": false,
    "is_proxy": false,
    "is_hosting": true,
    "is_datacenter": false,
    "is_tor": false,
    "is_residential": false,
    "is_mobile": false,
    "premium": false
  },
  "ports": { 
    "open_count": 2, 
    "open_ports": [80, 443] 
  }
}
```

### CSV Export (.csv)
Spreadsheet-compatible format for analysis in Excel or Google Sheets:
```csv
Field,Value
Scan Date,2026-02-09 15:30:45
Target IP,1.1.1.1
GEOLOCATION,
IP,1.1.1.1
Hostname,one.one.one.one
Country,Hong Kong (HK)
City,Hong Kong
Region,Central and Western District
Continent,Asia
Latitude,22.3193
Longitude,114.1693
Accuracy Radius (km),1000
Timezone,Asia/Hong_Kong (UTC+8)
Currency,Hong Kong Dollar (HKD)
Language,Mandarin Chinese (zh)
ISP,Cloudflare, Inc
Organization,APNIC and Cloudflare DNS Resolver project
ASN,AS13335 Cloudflare, Inc.
RIR,APNIC
Connection Type,Hosting
Threat Level,medium
SECURITY FLAGS,
VPN Detected,False
Proxy Detected,False
Hosting Provider,True
Datacenter,False
Tor Network,False
Residential,False
Mobile Network,False
Premium Data,False
PORTS,
Total Open Ports,2
Open Port,80
Open Port,443
```

**All three formats are generated automatically after each scan with complete geolocation and security data!**

---

## 📈 Output Information

### Comprehensive Geolocation Data
- **Network Info**: IP, Hostname, ISP, Organization, Connection Type
- **Geographic Data**: Country, City, Region, Continent, Postal Code
- **Coordinates**: Latitude, Longitude, Accuracy Radius (km)
- **Timezone Info**: Timezone name, UTC offset
- **Regional Details**: Currency, Language, Currency Code, Language Code
- **ASN Details**: ASN Number, ASN Org, RIR (Regional Internet Registry)
- **Threat Level**: Risk assessment and threat classification

### Advanced Security Flags (9 Detections)
- VPN Detection
- Proxy Detection
- Hosting Provider Identification
- Datacenter Detection
- Tor Network Detection
- Residential Connection
- Mobile Network Detection
- Home Proxy Detection
- Premium Data Availability

### Port Scan Results
- Open ports discovery with real-time notifications
- Custom port range (1-65535)
- Visual progress bar with percentage tracking
- Common ports quick scan option
- Batch scanning from file
- Comprehensive threat level analysis

---

## 💻 Examples

### Example 1: Quick Scan
```bash
python main.py 8.8.8.8
# Enter port range: 1 to 1000
# Generates 3 reports automatically
```

### Example 2: Domain with Custom Range
```bash
python main.py google.com
# Reports saved as:
# - report_142.251.32.46_20260209_143015.txt
# - report_142.251.32.46_20260209_143015.json
# - report_142.251.32.46_20260209_143015.csv
```

### Example 3: Interactive Menu
```bash
python main.py
# Select [1] for Full OSINT
# Select [4] for Batch Scan
# Select [5] for Help
```

### Example 4: Batch Scanning
```bash
# Create targets.txt
# 8.8.8.8
# google.com
# cloudflare.com

python main.py
# Select [4] Batch Scan
# Enter: targets.txt
```

## 🎯 Common Use Cases

| Scenario | Command | Mode |
|----------|---------|------|
| Quick IP check | `python main.py 8.8.8.8` | CLI |
| Domain reconnaissance | `python main.py google.com` | CLI |
| Comprehensive scan | `python main.py` → [1] | Interactive |
| Multiple targets | `python main.py` → [4] | Batch |
| Learn features | `python main.py` → [5] | Help |

---

## 📋 Requirements

- Python 3.6 or higher
- `requests` library (for API calls)
- Standard library modules: `socket`, `json`, `csv`, `sys`, `time`, `os`

### Install Dependencies
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install requests
```

---

## 🔒 Privacy & Disclaimer

**⚠️ Legal & Ethical Notice:**

This tool is designed for:
- ✓ Authorized security testing
- ✓ Personal network administration  
- ✓ Legitimate penetration testing with written permission
- ✓ Educational and research purposes
- ✓ Network reconnaissance on systems you own

**This tool should NOT be used for:**
- ✗ Unauthorized network access
- ✗ Scanning without explicit permission
- ✗ Malicious purposes
- ✗ Violating local laws or regulations
- ✗ Probing production systems without approval

**Users are solely responsible for legal compliance.**

---

## 📁 Project Structure

```
network-osint-scanner/
├── main.py                 # Main application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
├── .gitignore             # Git ignore rules
└── reports/               # Generated scan reports
```

---

## 🐛 Troubleshooting

### Issue: "Could not retrieve geoip data"
- Check your internet connection
- Verify the API endpoint is accessible
- The service may be temporarily down

### Issue: Port scan times out
- Increase timeout value in the code
- Check if firewall is blocking connections
- Reduce port range for faster scans

### Issue: Encoding errors
- Ensure you're using Python 3.6+
- Check your terminal supports UTF-8

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 xdrew87

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 👨‍💻 Author

**xdrew87**

- GitHub: [@xdrew87](https://github.com/xdrew87)
- Project: [Network OSINT Scanner](https://github.com/xdrew87/network-osint-scanner)

---

## 🙏 Acknowledgments

- Uses IP geolocation data from suicixde.com API
- Threat detection from IPQualityScore and VPNAPI.io
- Built with Python and love for cybersecurity

---

## 📞 Support

For issues, questions, or suggestions:
1. Open an issue on GitHub
2. Check existing documentation
3. Review the help section in the app

---

<div align="center">

**Made with ❤️ for the cybersecurity community**

⭐ If you found this helpful, please consider starring the repository!

</div>
