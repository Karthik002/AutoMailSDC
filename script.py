import smtplib
from tkinter import *

email_address = 'karthikprasad62@gmail.com'
email_password = 'kpagent002'

# Email
def send_email(email_name, email_recipient, email_subject, email_body):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    email_name = name.get()

    smtp.login(email_address, email_password)
    
    subject = email_subject
    body = email_body

    msg = f'Subject: {subject}\n\nDear {email_name},\n\n{body}'

    smtp.sendmail(email_address, email_recipient, msg)


# User Interface

def buttonClick():
    email_name = name.get()
    email_recipient = address.get()
    email_subject = subject.get()
    email_body = body.get()

    send_email(email_name, email_recipient, email_subject, email_body)


window = Tk()

#Title
titleLabel = Label(window, text="Sun Dental Care Automatic Mailing System", font=("Helvetica", 16))
titleLabel.place(x=100, y=10)

# Name
nameLabel = Label(window, text="Recipient Name: ", font=('Helvetica', 12))
nameLabel.place(x=170, y=60)
name = Entry(window, width=40, borderwidth=2)
name.place(x=170, y=90)

# Email
addressLabel = Label(window, text="Recipient Email: ", font=('Helvetica', 12))
addressLabel.place(x=170, y=120)
address = Entry(window, width=40, borderwidth=2)
address.place(x=170, y=150)

# Subject
subjectLabel = Label(window, text="Email Subject: ",  font=('Helvetica', 12))
subjectLabel.place(x=170, y=180)
subject = Entry(window, width=40, borderwidth=2)
subject.place(x=170, y=210)

# Body
bodyLabel = Label(window, text="Email Body: ",  font=('Helvetica', 12))
bodyLabel.place(x=170, y=240)
body = Entry(window, width=40, borderwidth=2)
body.place(x=170, y=270)

# Send Email Button
send_btn = Button(window, text="Send Email", padx=30,pady=10, bg='#77dd77', command=buttonClick)
send_btn.place(x=215, y=350)

window.geometry("600x400+20+40")
window.mainloop()
