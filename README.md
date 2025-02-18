# Digital Forensics Investigation Tool

## Overview
This project is a Digital Forensics and Incident Response (DFIR) tool that helps in log file analysis, malware detection, file carving, metadata extraction, case management, and AWS integration.

## Features
- Log File Analysis
- Timeline Creation
- File Carving
- Metadata Extraction
- Case Management
- Malware Detection
- Threat Hunting
- Automated Alerts & Reports
- AWS Integration

## Installation
### Prerequisites
- Python 3.x
- pip (Python package manager)
- PostgreSQL (or any preferred database)
- AWS credentials (for AWS integration)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/dfir-tool.git
   cd dfir-tool
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in `.env` file:
   ```env
   AWS_ACCESS_KEY=your-access-key
   AWS_SECRET_KEY=your-secret-key
   DB_HOST=localhost
   DB_USER=admin
   DB_PASSWORD=password
   DB_NAME=forensics_db
   ```
4. Run the setup script:
   ```bash
   bash setup.sh
   ```
5. Start the application:
   ```bash
   python app.py
   ```

## Usage
- Access the web UI at `http://localhost:5000`
- Upload logs, analyze malware, extract metadata, and generate reports

## Contribution
Feel free to submit pull requests or report issues.

