import os
import logging
from flask import Flask, render_template, request, jsonify
from app.log_analysis import analyze_logs
from app.timeline import create_timeline
from app.file_carving import recover_files
from app.metadata_extraction import extract_metadata
from app.case_management import manage_cases
from app.malware_detection import scan_for_malware
from app.threat_hunting import hunt_threats
from app.report_generator import generate_report
from app.alerts import send_alert
from app.aws_integration import upload_to_s3
from app.user_management import create_user, authenticate_user, delete_user
from app.incident_response import analyze_incident, mitigate_threat

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze-logs', methods=['POST'])
def analyze_logs_endpoint():
    log_data = request.json.get("log_data")
    result = analyze_logs(log_data)
    return jsonify(result)

@app.route('/create-timeline', methods=['POST'])
def create_timeline_endpoint():
    log_data = request.json.get("log_data")
    timeline = create_timeline(log_data)
    return jsonify(timeline)

@app.route('/recover-files', methods=['POST'])
def recover_files_endpoint():
    disk_image = request.json.get("disk_image")
    files = recover_files(disk_image)
    return jsonify(files)

@app.route('/extract-metadata', methods=['POST'])
def extract_metadata_endpoint():
    file_path = request.json.get("file_path")
    metadata = extract_metadata(file_path)
    return jsonify(metadata)

@app.route('/manage-cases', methods=['POST'])
def manage_cases_endpoint():
    case_data = request.json.get("case_data")
    case_response = manage_cases(case_data)
    return jsonify(case_response)

@app.route('/scan-malware', methods=['POST'])
def scan_malware_endpoint():
    file_path = request.json.get("file_path")
    scan_result = scan_for_malware(file_path)
    return jsonify(scan_result)

@app.route('/hunt-threats', methods=['POST'])
def hunt_threats_endpoint():
    network_data = request.json.get("network_data")
    threats = hunt_threats(network_data)
    return jsonify(threats)

@app.route('/generate-report', methods=['POST'])
def generate_report_endpoint():
    case_id = request.json.get("case_id")
    report = generate_report(case_id)
    return jsonify(report)

@app.route('/send-alert', methods=['POST'])
def send_alert_endpoint():
    alert_info = request.json.get("alert_info")
    alert_status = send_alert(alert_info)
    return jsonify(alert_status)

@app.route('/upload-s3', methods=['POST'])
def upload_s3_endpoint():
    file_path = request.json.get("file_path")
    s3_response = upload_to_s3(file_path)
    return jsonify(s3_response)

@app.route('/create-user', methods=['POST'])
def create_user_endpoint():
    user_data = request.json.get("user_data")
    response = create_user(user_data)
    return jsonify(response)

@app.route('/authenticate-user', methods=['POST'])
def authenticate_user_endpoint():
    credentials = request.json.get("credentials")
    response = authenticate_user(credentials)
    return jsonify(response)

@app.route('/delete-user', methods=['POST'])
def delete_user_endpoint():
    user_id = request.json.get("user_id")
    response = delete_user(user_id)
    return jsonify(response)

@app.route('/analyze-incident', methods=['POST'])
def analyze_incident_endpoint():
    incident_data = request.json.get("incident_data")
    response = analyze_incident(incident_data)
    return jsonify(response)

@app.route('/mitigate-threat', methods=['POST'])
def mitigate_threat_endpoint():
    threat_data = request.json.get("threat_data")
    response = mitigate_threat(threat_data)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
