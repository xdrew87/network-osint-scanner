# Contributing to Network OSINT Scanner

Thank you for considering a contribution! This document provides guidelines for contributing.

## Code of Conduct

- Be respectful and professional
- Follow best practices
- No malicious code or exploits
- Respect privacy and legal boundaries

## How to Contribute

### Reporting Bugs

1. Use the GitHub Issues page
2. Provide a clear title and description
3. Include steps to reproduce
4. Add your OS and Python version
5. Attach relevant logs if applicable

**Example Bug Report:**
```
Title: Port scan timeout on large ranges
Description: When scanning 1-65535, timeout errors occur
Steps: 1. Enter IP 2. Enter range 1-65535 3. See timeout errors
Environment: Windows 10, Python 3.9
```

### Suggesting Features

1. Check existing issues first
2. Describe the feature clearly
3. Explain the use case
4. Show any relevant examples

**Example Feature Request:**
```
Title: Add proxy/VPN filtering
Description: Allow filtering results by VPN/proxy status
Use Case: Researchers want to exclude VPN-detected IPs
```

### Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/network-osint-scanner.git
   cd network-osint-scanner
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/my-amazing-feature
   ```

3. **Make your changes**
   - Follow PEP 8 style guide
   - Add comments for complex logic
   - Test thoroughly before submitting

4. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: description of changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/my-amazing-feature
   ```

6. **Open a Pull Request**
   - Clear title describing changes
   - Detailed description of what was changed
   - Link to any related issues

## Code Style Guidelines

### Python Style (PEP 8)
```python
# Good
def scan_ports(ip, port_range=None):
    """Scan ports on target IP."""
    open_ports = []
    for port in port_range:
        result = socket.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
    return open_ports

# Avoid
def sp(i,p=None):
    op = []
    for pt in p:
        r = socket.connect_ex((i, pt))
        if r == 0:
            op.append(pt)
    return op
```

### Naming Conventions
- Functions: `snake_case` (e.g., `scan_ports()`)
- Classes: `PascalCase` (e.g., `Colors`)
- Constants: `UPPER_CASE` (e.g., `COMMON_PORTS`)
- Variables: `snake_case` (e.g., `open_ports`)

### Comments & Documentation
```python
def get_ipinfo(ip):
    """
    Retrieve geolocation information for an IP address.
    
    Args:
        ip (str): Target IP address
        
    Returns:
        dict: Geolocation data or empty dict if failed
    """
```

## Pull Request Process

1. Update README.md with any new features
2. Test all functionality
3. Add comments explaining new code
4. Ensure no breaking changes
5. Reference related issues

## Areas for Contribution

- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🎨 UI/UX enhancements
- ⚡ Performance optimizations
- 🔒 Security improvements
- 📱 Additional API integrations

## Setup Development Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tool
python main.py
```

## Testing

Before submitting a PR, test:
- [ ] Interactive menu mode
- [ ] Command-line mode
- [ ] All scanning options
- [ ] Error handling
- [ ] Report generation

## Questions?

1. Check the README.md
2. Review existing issues/discussions
3. Open a new discussion thread

## License

By contributing, you agree your code will be licensed under the MIT License.

---

**Thank you for contributing to make this tool better!** 🚀
