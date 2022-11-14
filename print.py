import poplib
from email import parser
import subprocess
import time
import os

server = "MAIL_SERVER"
login = "LOGIN@MAIL_SERVER.COM"
password = "MAIL_ACCT_PASSWORD"
allowed_senders = ["LIST","OF","ACCEPTABLE","SENDER","EMAIL","ADDRESSES"]
#you can get this with lpstat -s:
printer_name = "Deskjet-1010-series"

dir_path = os.path.dirname(os.path.realpath(__file__))

def mail_connection():
    pop_conn = poplib.POP3_SSL(server)
    pop_conn.user(login)
    pop_conn.pass_(password)
    return pop_conn


def fetch_mail(delete_after=True):
    pop_conn = mail_connection()
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    messages = ['\n'.join(map(bytes.decode, mssg[1])) for mssg in messages]
    messages = [parser.Parser().parsestr(mssg) for mssg in messages]
    if delete_after == True:
        delete_messages = [pop_conn.dele(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    pop_conn.quit()
    return messages


def get_attachments():
    allowed_mimetypes = ["application/pdf","application/octet-stream"]
    messages = fetch_mail()
    attachments = []
    for msg in messages:
        if any(substring in msg["From"] for substring in allowed_senders):
            for part in msg.walk():
                if part.get_content_type() in allowed_mimetypes:
                    if ".pdf" in part.get_filename():
                        name = str(round(time.time() * 1000)) + part.get_filename()
                        data = part.get_payload(decode=True)
                        f = open(dir_path + "/3print/" + name,'wb')
                        f.write(data)
                        f.close()
                        attachments.append(name)
                        subprocess.run(["lp", "-d", printer_name, dir_path + "/3print/" + name])
    return attachments

get_attachments()


