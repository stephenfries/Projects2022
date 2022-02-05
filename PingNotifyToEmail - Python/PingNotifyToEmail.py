import smtplib, ssl, time                                                               # Built-in
from ping3 import ping                                                                  # pip install ping3

###################### EMAIL INITAL SETUP ######################                        # https://realpython.com/python-send-email/
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "sendersemail@gmail.com"
receiver_email = ["receiversemail1@gmail.com", "receiversemail2@gmail.com"]
to = ", ".join(receiver_email)
password = input("Type your password and press enter:")
message = """\
Subject: The Host Device is Offline

The Host device is unable to be reached and is offline."""

##################### FUNCTION TO SEND EMAIL #####################
def sendEmail():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

########### PING ADDRESS IF FAILS 120 TIMES SEND EMAIL #############
pingAttempts = 0

try:
    while True:
        pingStatus = ping('1.1.1.1')                                                        # PINGS ADDRESS RETURNS response time if successful, and FALSE or NONE if failed. 
        if(pingStatus == False or pingStatus == None):                                      # https://stackoverflow.com/a/47926378 (HOW TO PING WITH PING3)
            pingAttempts += 1
            if(pingAttempts == 120):
                sendEmail()                                                                 # SENDS EMAIL AFTER 120 FAILED PINGS
                print('Email was sent successfully.')
            print("the host is unable to be reached (Attempt #" + str(pingAttempts) + ')')
            time.sleep(1)
        else:                                                                               # PING WAS SUCCESSFUL
                pingAttempts = 0
                print('the host is online')
                time.sleep(10)
except SMTPAuthenticationError:                                                             # RESTARTS SCRIPT IF SMTP AUTHENTICATION ERRORS OUT
    print('UNABLE TO SEND EMAIL - SMTP SERVER ERROR: RESTARTING SCRIPT')
    pass                        
