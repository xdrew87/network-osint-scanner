# Network OSINT & Port Scanner

<div align="center">

![Version](https://img.shields.io/badge/version-2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

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

- **🌍 IP Geolocation** - Get detailed geographic and ISP information
- **🔌 Advanced Port Scanning** - Scan any port range from 1-65535
- **🛡️ Security Detection** - Identify VPNs, proxies, and hosting providers
- **📊 Threat Assessment** - Real-time threat level evaluation
- **⚡ Progress Tracking** - Live scanning progress with percentage indicator
- **📁 Batch Processing** - Scan multiple targets from a file
- **💾 Report Generation** - Automatic timestamped report saving
- **🎨 Beautiful UI** - Color-coded output with ASCII art
- **🔄 Multiple APIs** - Cross-reference data from multiple sources
- **📱 Interactive & CLI Modes** - Use menu system or command line

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/xdrew87/network-osint-scanner.git
cd network-osint-scanner

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Interactive menu mode (no arguments)
python main.py

# Direct scan (with IP/domain)
python main.py 8.8.8.8
```

---

## 📖 Usage Guide

### Interactive Mode (Recommended)

Run without arguments to access the menu:

```bash
python main.py
```

**Menu Options:**
- **[1] Full OSINT Scan** - Complete reconnaissance with custom port range
- **[2] Port Scan Only** - Fast port scanning for specific ranges
- **[3] Quick OSINT** - Fast scan using common ports
- **[4] Batch Scan** - Process multiple targets from a file
- **[5] Help & Documentation** - View built-in help
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

## 📊 Output Information

### Geolocation Data
- IP Address
- Hostname
- City, Region, Country
- ISP & Organization
- ASN (Autonomous System Number)
- Connection Type

### Security Flags
- VPN Detection
- Proxy Detection
- Hosting Provider Identification
- Threat Level Assessment
- Fraud Score (if API available)

### Port Scan Results
- Open ports list
- Real-time scanning progress
- Timestamped reports

---

## 💻 Examples

### Example 1: Quick OSINT of Google DNS
```bash
python main.py 8.8.8.8
```
Enter port range: 1 to 100

### Example 2: Full scan of cloudflare.com
```bash
python main.py cloudflare.com
```
Enter port range: 1 to 65535

### Example 3: Batch scan from file
```bash
python main.py
# Select option [4]
# Enter: targets.txt
```

---

## 📋 Requirements

- Python 3.6+
- requests
- socket (built-in)
- json (built-in)

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔒 Privacy & Disclaimer

**⚠️ Important:**

This tool is designed for:
- Academic and educational purposes
- Authorized security testing
- Personal network administration
- Legitimate penetration testing

**DO NOT** use this tool:
- Without explicit authorization
- Against targets you don't own or have permission to test
- For malicious purposes
- To probe networks illegally

Users are responsible for complying with all applicable laws and regulations.

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
