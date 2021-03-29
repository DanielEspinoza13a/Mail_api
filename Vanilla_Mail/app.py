import smtplib


message = "any message you want to send"
subject = "any subject"

message = "Subject: {}\n\n{}".format(subject, message)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")

server.sendmail("YOUR EMAIL ADDRESS", "Any Email Address to Send an Email", message)

server.quit()

print("correctly sent")
