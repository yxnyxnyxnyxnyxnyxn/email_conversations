# Set up
import os,glob



# Read all plain text file in raw_emails dictionary
# Refactor to function
path = 'raw_emails/*'
emails = []
for fle in glob.glob(path):
    with open(fle,'r') as f:
        data = f.read()
        emails.append(data)

#print emails





