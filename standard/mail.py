# send mail

import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

from_address = 'from＠xxx.xx.jp'
to_address   = 'to＠xxx.xx.jp'

charset = 'ISO-2022-JP'
subject = u'メールの件名です'
text    = u'メールの本文です'

msg = MIMEText(text.encode(charset), 'plain', charset)
msg['Subject'] = Header(subject, charset)
msg['From'] = from_address
msg['To'] = to_address
msg['Date'] = formatdate(localtime=True)

smtp = smtplib.SMTP('xxx.xx.jp')
smtp.sendmail(from_address, to_address, msg.as_string())
smtp.close()