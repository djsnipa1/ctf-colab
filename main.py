import pytextnow
import os

sid = os.environ('TEXTNOW_SID')
csrf = os.environ('TEXTNOW_CSRF')
number = '3172155569'

# Way 1. Include connect.sid and csrf cookie in the constructor
client = pytextnow.Client("djsnipa1", sid_cookie=sid, csrf_cookie=csrf)

with open('~/connect.log') as f:
    contents = f.read()
    print(contents)

# client.send_sms(number, "Hello World!")
client.send_sms(number, contents)


