import smtplib
from account import *

#heads up for this code to work might need to configure gmail setting to allow access for 
#less safe apps.. to do that watch nado coding 7:48 of 활용편4
#this method also wont work for Korean or Japanese languages etc. To do that see 2_send_with_msg.py
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() #연결이 잘  수립되는지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "test mail" #메일 제목
    body = "mail body"

    msg = f"Subject: {subject}\n{body}"
    #sender and receiver email, message
    smtp.sendmail(EMAIL_ADDRESS, "shinj0127@gmail.com", msg) 
    
