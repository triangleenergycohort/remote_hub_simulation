#script to accept payment from mobile device01

import smtplib
import imaplib
import email
import re

#parse data from email body
def parse_payment_data(text):
    #print(text)
    data = []
    m = re.search('customer name: ([a-z]+ ?[a-z]+?)',text.lower())
    if m:
        data.append(m.group(1))
    m = re.search('payment type: ([a-z]+ ?[a-z]+? ?[a-z]+?)',text.lower())
    if m:
        data.append(m.group(1))
    m = re.search('payment amount: \$(\d*\.?\d*?)',text.lower())
    if m:
        data.append(m.group(1))
    if len(data) == 3:
        return data


#check email for payment message
def check_for_payment_message():
    #init
    invoices = []
    ORG_EMAIL   = "@gmail.com"
    FROM_EMAIL  = "tec.remote01" + ORG_EMAIL
    FROM_PWD    = "5Wlp&0$#C^1G"
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT   = 993
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
                #print('From : ' + email_from + '\n')

                if email_from == 'ebldevice2@gmail.com' and re.search('Payment from',email_subject):
                    hit = parse_payment_data(email_body[0].as_string())
                    if hit:
                        invoices.append(hit)

    mail.logout()
    return invoices


#edit csv using customer data
def edit_account_balance(invoices):

    return


def main():
    i=check_for_payment_message()
    print(i)
    return


if __name__ == '__main__':
    main()
