# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0] - 2026-02-09

### Added
- ✨ Interactive menu-driven interface
- 🎨 Beautiful ASCII art banner in main display
- 🌍 Five scanning modes (Full OSINT, Port Scan, Quick OSINT, Batch, Help)
- 📁 Batch scanning from file support
- 💾 Automatic timestamped report generation
- 🎯 Real-time progress tracking during port scans
- 📊 Cross-API threat detection verification
- 🔒 Security flags display (VPN, Proxy, Hosting detection)
- ⚙️ Command-line mode for direct scanning
- 🎨 Color-coded output for better readability
- 📚 Built-in help and documentation system

### Changed
- 🔧 Refactored entire codebase for modularity
- 📈 Improved report formatting
- 🎨 Enhanced visual presentation with box drawing
- ⚡ Optimized port scanning performance
- 📝 Better error messages and user feedback

### Fixed
- 🐛 Port range validation improvements
- 🔧 Better handling of network timeouts
- 📱 Improved terminal compatibility
- 🎯 More reliable IP resolution

### Documentation
- 📖 Comprehensive README.md
- 📋 CONTRIBUTING.md for contributors
- 🔒 SECURITY.md policy
- 📝 This CHANGELOG.md
- ⚖️ MIT LICENSE included
- 🔧 .gitignore configured

---

## [1.5] - 2026-01-15

### Added
- 🌐 IPQualityScore API integration
- 🔑 VPNAPI.io API support
- 📊 Multi-API cross-checking for threat detection

### Changed
- 💾 Improved report output formatting

---

## [1.0] - 2026-01-01

### Added
- 🔍 Initial port scanning functionality
- 🌍 IP geolocation lookup
- 📊 Basic OSINT report generation
- 🔴 Threat level assessment

---

## Planned Features (Future Releases)

### [2.1] - Upcoming
- [ ] 📊 Database support for scan history
- [ ] 🔔 Webhook notifications for open ports
- [ ] 📈 Graphical report generation (JSON, PDF)
- [ ] 🌐 Web UI interface
- [ ] ⚙️ Configuration file support
- [ ] 🔐 Encrypted credential storage

### [2.2] - Future
- [ ] 📡 Advanced vulnerability scanning
- [ ] 🔗 DNS enumeration and resolution
- [ ] 🎯 Service version detection
- [ ] 🗺️ Network mapping visualization
- [ ] 📤 Cloud storage export (AWS S3, Azure)
- [ ] 🤖 Automated scan scheduling

### [3.0] - Long-term
- [ ] 🌐 Web-based dashboard
- [ ] 📊 Advanced analytics and reporting
- [ ] 🔌 Plugin system for extensibility
- [ ] 🤖 Machine learning threat detection
- [ ] ☁️ Cloud deployment ready
- [ ] 🔐 Enterprise security features

---

## Version History Summary

| Version | Release Date | Type | Changes |
|---------|-------------|------|---------|
| 2.0 | 2026-02-09 | Major | Complete rewrite with UI & multiple features |
| 1.5 | 2026-01-15 | Minor | API integrations |
| 1.0 | 2026-01-01 | Initial | Basic functionality |

---

## Migration Guide

### From 1.x to 2.0

The 2.0 release is a major update with breaking changes:

**Old Usage:**
```bash
python main.py 8.8.8.8  # Limited options
```

**New Usage:**
```bash
# Interactive mode (recommended)
python main.py

# Or direct mode (same as before, with more control)
python main.py 8.8.8.8
```

**New Features:**
- Menu-driven interface
- Batch processing
- Better reporting

---

## Support for Older Versions

- 🟢 **v2.0** - Current release, actively maintained
- 🟡 **v1.5** - Legacy, limited support
- 🔴 **v1.0** - No longer supported

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## Security

For security issues, see [SECURITY.md](SECURITY.md)

---

*Last Updated: 2026-02-09*
