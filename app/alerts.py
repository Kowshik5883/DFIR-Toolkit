import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(subject, message, recipient_email):
    """Sends an email alert with the provided subject and message."""
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(message, 'plain'))
    
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Alert sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

if __name__ == "__main__":
    test_subject = "Security Alert: Threat Detected"
    test_message = "A potential threat has been detected in the system. Immediate action required."
    test_recipient = "recipient@example.com"  # Replace with the recipient's email
    
    send_email_alert(test_subject, test_message, test_recipient)
