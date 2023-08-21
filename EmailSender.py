import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime

# current date
now = str(datetime.now().strftime('%Y-%m-%d')) 

subject = "Search Daily Scan Report"
body = "Kindly find the attached Scan Report for Production URLs, Thanks"
sender_email = ""
#sender_email = ""
receiver_email = ''
#receiver_email = ""
password = ""
#password = ""

# Create a multipart message and set headers
message = MIMEMultipart('alternative')
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
#message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
part = MIMEText(body, "plain")
message.attach(part)

filename = ""  # Path to attachment

#filename = "C:\cygwin64\home\mubeen.gulzar\IRSMDv1.0_Windows\IRSMDv1.0\Output\EmailPDF\CombinedReport2022-06-25.pdf"

# Open file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {'CombinedReport'+now+'.pdf'}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("mail.gandi.net", port=465, context=context) as server:
#with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email.split(','), text)

print("Email has been Sent")
