import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

addr_from = 'rusinchuk@gmail.com'
addr_to = 'el.piankova@gmail.com'
body = "Text mail from Python"

msg = MIMEMultipart()
msg.attach(MIMEText(body, 'Say hello and then goodbye'))
msg['From'] = addr_from
msg['Subject'] = 'For testing purposes'

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.starttls()
smtp_object.login(addr_from, 'blablabla')
smtp_object.sendmail(from_addr="rusinchuk@gmail.com", to_addrs="el.piankova@gmail.com", msg="It really works!!!")
smtp_object.send_message(msg)
smtp_object.quit()






