
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "ProgressBar20XX@gmail.com"  # Enter your address
receiver_email = "240155787@qq.com"  # Enter receiver address
#password = input("Type your password and press enter: ")
password="kzoyvjckjltatdgt"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    print('login...')
    server.login(sender_email, password)
    print('sending...')
    server.sendmail(sender_email, receiver_email, message)


print("done")
