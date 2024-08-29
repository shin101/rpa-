from imap_tools import MailBox
from account import *


# mailbox = MailBox("imap.gmail.com",993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# above code needs to be ended with mailbox.logout()


#below "with" method you dont need to do mailbox.logout() at the end
with MailBox("imap.gmail.com",993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(UNSEEN)',limit=5, reverse=True): #읽지 않은 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #   for msg in mailbox.fetch('(FROM shinj0127@gmail.com)', limit=3, reverse=True): #특정인이 보낸 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))  

    # 작은 따옴표로 먼저 감싸고, 실제 TEXT 부분은 큰 따옴표로 감싸주세요
    #   for msg in mailbox.fetch('(TEXT "food")'): #어떤글자 포함하는 메일(제목, 본문)
    #     print("[{}] {}".format(msg.from_, msg.subject))  

    #   for msg in mailbox.fetch('(SUBJECT "food")'): #어떤글자 포함하는 메일(제목만!)
    #     print("[{}] {}".format(msg.from_, msg.subject))  

    # # Use Code below if you want to search non-English words like Korean.
    #     for msg in mailbox.fetch(limit=5, reverse=True)): 
    #         if "테스트" in msg.subject:
    #             print("[{}] {}".format(msg.from_, msg.subject))  

    #   for msg in mailbox.fetch('(SENTSINCE 17-JAN-2022)', reverse=True, limit=5): #특정 날짜 이후의 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))  

    #   for msg in mailbox.fetch('(ON 27-JAN-2020)', reverse=True, limit=5): #특정 날짜에 온 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))  

    #     #2가지 이상의 조건을 모두 만족하는 메일
    #   for msg in mailbox.fetch('(ON 27-JAN-2019 SUBJECT "birthday")', reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))  

        #2가지 이상의 조건중 하나라도 만족하는 메일
      for msg in mailbox.fetch('(OR ON 27-JAN-2019 SUBJECT "birthday")', reverse=True, limit=5): 
        print("[{}] {}".format(msg.from_, msg.subject))   