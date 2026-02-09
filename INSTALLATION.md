# Installation Guide

Detailed installation instructions for Network OSINT Scanner.

## Table of Contents
- [System Requirements](#system-requirements)
- [Quick Install](#quick-install)
- [Detailed Installation](#detailed-installation)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

---

## System Requirements

### Operating System
- Windows 10/11
- macOS 10.14+
- Linux (Ubuntu 18.04+, Debian, CentOS, etc.)

### Software
- **Python 3.6 or higher** (3.9+ recommended)
- **pip** (Python package manager)
- **git** (for cloning repository)

### Check Your Python Version

```bash
# Windows
python --version

# macOS/Linux
python3 --version
```

Should show `Python 3.6.0` or higher.

---

## Quick Install

### 1. Clone Repository
```bash
git clone https://github.com/xdrew87/network-osint-scanner.git
cd network-osint-scanner
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Application
```bash
python main.py
```

**That's it!** You're ready to scan.

---

## Detailed Installation

### Step-by-Step Installation

#### Step 1: Install Python

**Windows:**
1. Download from https://www.python.org/downloads/
2. Run installer
3. ✅ **Important**: Check "Add Python to PATH"
4. Click Install
5. Verify: `python --version`

**macOS:**
```bash
# Using Homebrew
brew install python3

# Or download from https://www.python.org/downloads/
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

#### Step 2: Create Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

#### Step 3: Clone Repository

```bash
git clone https://github.com/xdrew87/network-osint-scanner.git
cd network-osint-scanner
```

#### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 5: Test Installation

```bash
# Should show help/menu
python main.py

# If you see the banner and menu, you're ready!
```

---

## Verification

### Test Commands

```bash
# Test 1: Run interactive mode
python main.py
# Should display: Banner and menu

# Test 2: Direct IP scan
python main.py 8.8.8.8
# Should prompt for port range

# Test 3: Help mode
python main.py
# Select option [5] for help
```

### Success Indicators

- ✅ Banner displays correctly with ASCII art
- ✅ Colors appear properly (pink header, cyan menu, etc.)
- ✅ Can enter IP addresses
- ✅ Can enter port ranges
- ✅ Port scanning starts and shows progress

---

## Advanced Installation Options

### Using Docker (Optional)

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

ENTRYPOINT ["python", "main.py"]
```

Build and run:
```bash
docker build -t osint-scanner .
docker run -it osint-scanner
```

### Installing from Source with git

```bash
# Clone with SSH (if you have SSH keys configured)
git clone git@github.com:xdrew87/network-osint-scanner.git

# Clone with HTTPS
git clone https://github.com/xdrew87/network-osint-scanner.git

# Navigate to directory
cd network-osint-scanner

# Install
pip install -r requirements.txt

# Run
python main.py
```

### Development Installation

```bash
# Clone repository
git clone https://github.com/xdrew87/network-osint-scanner.git
cd network-osint-scanner

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Ready for development!
```

---

## Troubleshooting

### Issue: "Python not found"

**Solution:**
```bash
# Verify Python is installed
python --version

# If not found, add Python to PATH:
# Windows: Reinstall Python and check "Add Python to PATH"
# macOS/Linux: Ensure Python3 is installed and linked properly
```

### Issue: "pip: command not found"

**Solution:**
```bash
# Use python -m pip instead
python -m pip install -r requirements.txt

# Or upgrade pip
python -m pip install --upgrade pip
```

### Issue: "requests module not found"

**Solution:**
```bash
# Install missing module
pip install requests

# Or reinstall all requirements
pip install -r requirements.txt
```

### Issue: Permission denied (Linux/macOS)

**Solution:**
```bash
# Add execute permission
chmod +x main.py

# Run with python explicitly
python main.py
```

### Issue: Colors not displaying properly

**Solution:**
```bash
# Update terminal encoding to UTF-8
# Windows: Character set in console properties
# macOS/Linux: Usually already UTF-8, but check:
echo $LANG  # Should include UTF-8
```

### Issue: Port scan not working

**Solution:**
1. Check internet connection
2. Verify firewall allows outbound connections
3. Try smaller port range first (80-443)
4. Increase timeout value if needed

### Issue: "ModuleNotFoundError: No module named 'requests'"

**Solution:**
```bash
# Update pip first
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Or install specific module
pip install requests
```

---

## Platform-Specific Notes

### Windows
- Terminal colors work in Windows 10+
- Use `cmd.exe` or PowerShell
- Windows Terminal recommended for best colors

### macOS
- Install Xcode Command Line Tools first:
```bash
xcode-select --install
```
- Use Terminal or iTerm2
- Install Python via Homebrew recommended

### Linux
- Most distributions include Python
- May need to use `python3` explicitly
- Ensure UTF-8 locale is set
- Install build-essential for some packages:
```bash
sudo apt-get install build-essential
```

---

## Uninstallation

### Remove Virtual Environment
```bash
# Remove venv folder
# Windows:
rmdir /s venv

# macOS/Linux:
rm -rf venv
```

### Remove Installation
```bash
# Just delete the folder or:
# If cloned via git:
cd ..
rm -rf network-osint-scanner
```

---

## Getting Help

- 📖 **Documentation**: See README.md
- 🆘 **Issues**: GitHub Issues page
- 💬 **Discussions**: GitHub Discussions
- 📧 **Email**: Check SECURITY.md for contact

---

## Next Steps

After installation:

1. **Read Documentation**: [README.md](README.md)
2. **Try Examples**: See examples section in README
3. **Configure APIs** (Optional): Add API keys for enhanced features
4. **Review Security**: Check [SECURITY.md](SECURITY.md)
5. **Start Scanning**: Run `python main.py`

---

**Happy scanning!** 🎯
