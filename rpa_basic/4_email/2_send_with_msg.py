import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "shinj0127@gmail.com"

# 여러 명에게 메일을 보낼때
#method 1 
# msg["To"] = "shinj0127@gmail.com, shinj0127@gmail.com"

#method 2
# to_list = ["shinj0127@gmail.com","shinj0127@gmail.com"]
# msg["To"] = ", ".join(to_list)

# 참조
# msg["Cc"] = "shinj0127@gmail.com"

#비밀 참조
# msg["Bcc"] = "shinj0127@gmail.com"

msg.set_content("테스트 본문입니다")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)