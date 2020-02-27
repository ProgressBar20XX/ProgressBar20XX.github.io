# use python to send gmail
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "ProgressBar20XX@gmail.com"  # Enter your address
receiver_email = "240155787@qq.com"  # Enter receiver address
#password = input("Type your password and press enter: ")
password="kzoyvjckjltatdgt"

# to send just a plain text
message = """\
Subject: Hi there

This message is sent from Python."""


message = MIMEMultipart("alternative")
message["Subject"] = "The ultimate ProgressBar"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

html="""
Dear Mr./Mrs.,<br> <h3> there are 310 days left before 2020 ends </h3> <br> Welcome to join my email list.<br> Hope you enjoy it!
<br> from<br> ProgressBar20XX ( written by RadishMeeting ) <br> Wed Feb 26 23:28:49 UTC 2020

<img alt="Qries" src="https://github.com/ProgressBar20XX/ProgressBar20XX.github.io/raw/master/static/progressbar/jpg/percentage100.jpg"
         width=100%" height="70">
"""


# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
# message.attach(part1)
message.attach(part2)


context_ssl = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context_ssl) as server:
    print('login...')
    server.login(sender_email, password)
    print('sending...')
    server.sendmail(sender_email, receiver_email, message.as_string() )


print("done")
