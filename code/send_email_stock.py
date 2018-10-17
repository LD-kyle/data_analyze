import smtplib
import mimetypes
import pathlib
#import getpass
from email.message import Message
#from email.mime.message import MIMEMessage
from email.message import EmailMessage
from email.headerregistry import Address

def create_message(from_addr, to_addrs, subject, text, paths):
    #msg = MIMEMessage(Message())
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = ', '.join(to_addrs)
    msg.set_content(text)
    for path in paths:
      try:
        ctype, encoding = mimetypes.guess_type(path)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        with open(path, 'rb') as fp:
            msg.add_attachment(fp.read(),
                               maintype=maintype,
                               subtype=subtype,
                                 filename=pathlib.Path(path).name)
      except Exception as e:
          print(path)
    return msg


def send(host, user, password, message):
    s = smtplib.SMTP_SSL(host)
    s.login(user, password)
    s.send_message(message)
    s.quit()


def main(text,files):
    msg = create_message('kaili17@mails.jlu.edu.cn', ['2630582744@qq.com'],
                         'lk_stock', text,
                         files)
    #password = getpass.getpass('lk15131416')
    send('mails.jlu.edu.cn','kaili17@mails.jlu.edu.cn','lk15131416', msg)


if __name__ == '__main__':
    main('更新',[])