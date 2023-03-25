from email.message import EmailMessage
import ssl
import smtplib


def send_mail(subject, body):
    email_sender = "cbay5122022@gmail.com"
    email_password = "wexhyvexxcjuhwvp"
    email_reciever = "cbay5122022@gmail.com"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject

    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())
    print("Email was sent")