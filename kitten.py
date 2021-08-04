Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python3


#Defining my variables

#My name
name="Cynthia Orinda"

#my email address
email="orinda.cynthia@gmail.com"

#Slack Username
s_uname="@Orinda"

#My preferred Biostack
biostack="Genomics&Transcriptomics"


#Printing out the output Each on a new line
print("My name is: %s \nEmail: %s \nSlack Username: %s \nBiostack: %s\n" % (name,email,s_uname,biostack))

#Print the output on the same line but tab-separated
print("%s\t%s\t%s\t%s"% (name,email,s_uname,biostack))