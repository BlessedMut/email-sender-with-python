import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Master:


    def one(self, subject, message,send_to_email):
        try:
            email = 'email@gmail.com'
            password = 'password'

            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = send_to_email
            msg['Subject'] = subject

            # Attach the message to the MIMEMultipart object
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            text = msg.as_string()  # You now need to convert the MIMEMultipart object to a string to send
            server.sendmail(email, send_to_email, text)
            server.quit()
            print("Success: mail sent")
        except:
            print("Failed!!!")



