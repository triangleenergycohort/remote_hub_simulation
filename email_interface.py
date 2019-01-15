#functions for interacting with email
#D. Storelli
#9 January 2019
#source code:
#https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/
#https://codehandbook.org/how-to-read-email-from-gmail-using-python/

import smtplib
import imaplib
import email

#send message function
def send_email(message):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    sender_email_id = "tec.remote01@gmail.com"
    sender_email_id_password = "5Wlp&0$#C^1G"
    try:
        s.login(sender_email_id, sender_email_id_password)
        pass
    except Exception as e:
        #** add better error reporting**
        print('login failed')

    # message to be sent
    #message = "Test_message_1"

    # sending the mail
    receiver_email_id = "tec.device01@gmail.com"
    s.sendmail(sender_email_id, receiver_email_id, message)

    # terminating the session
    s.quit()
    return



#recieve message function
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "tec.device01" + ORG_EMAIL
FROM_PWD    = "0dY2!c4szbBQ"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def readmail():
    # mail reading logic will come here !!
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
    except Exception as e:
        print('login failed',e.message)

    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])

    for i in range(latest_email_id,first_email_id, -1):
        typ, data = mail.fetch(str(i), '(RFC822)' )

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode())
                email_subject = msg['subject']
                email_from = msg['from']
                email_body = msg.get_payload()
                print('From : ' + email_from + '\n')
                #if email_from == 'tec.remote01@gmail.com':
                    #print('Body: '+'\n'+email_body+'\n')
                #print('Subject : ' + email_subject + '\n')
    #print(id_list)
    mail.logout()


    return


def main():
    #send_email("testing function")
    readmail()
    return

if __name__ == '__main__':
    main()
