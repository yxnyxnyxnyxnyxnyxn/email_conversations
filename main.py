# Set up
import os,glob
from datetime import datetime
from n_ary_tree import Node,N_ary_Tree

# Function to parse email info
# Return a key: message-id; infos: dictionary of headers info in emails
def parse_email(f):
    key = ""
    infos = {}
    for line in f:
        if line == '\n':
            break
        else:
            if ':' in line:
                line = line[:-1]
                info = line.split(':',1)
                # use Message-ID as 2d dictionary key
                if info[0] == 'Message-ID':
                    key = info[1]
                # Format Date to compare
                if info[0] == 'Date':
                    time = info[1].split('+',1)[0]
                    infos['Date'] = datetime.strptime(time, ' %d %b %Y %H:%M:%S ')
                # Store other header into map
                else:
                    infos[info[0]] = info[1]
    return [key,infos]


# Function to Read all plain text file in raw_emails dictionary
def read_folder(path):
    infos = {}
    for fle in glob.glob(path):
        with open(fle,'r') as f:
            infos = parse_email(f)
            f.close()
        summary[infos[0]] = infos[1]



# Function to dealing with forward to reply function
def fw_re_email(keyword,subject):
    n = subject.upper().count(keyword)
    sub = subject.rsplit(':',1)[1]
    if 'In-Reply-To' not in info:
        # find parent id
        parent_id = subjects[sub][n]
        # add messahe to same subject
        conversation.add(id,parent_id)
    #Store into map
    subjects[sub][n+1] = id

# Function to output result
def output(conversations,n=1):
    for conv in conversations:
        print ('Conversation%d: ' %n)
        print conv
        n = n+1

def write_result_file(conversations,n=1):
    output = open('result.txt','w+')
    for conv in conversations:
        output.write('Conversation%d:\n ' %n)
        output.write(conv)
        output.write('\n')
        n = n+1
    output.close()

#---------------Main--------------#
if __name__ == '__main__':
    path = 'raw_emails/*'
    # summary: 2d dictionary to store each email's infomation
    # key: email-id value: {In-Reply-To, Subject,  Date}
    summary = {}
    read_folder(path)

    # Sort the email by date
    emails = {}
    summary = sorted(summary.items(),key = lambda kv: kv[1]['Date'])

    # map subject with latest message related to this subject
    subjects = {}

    # map to group same promotion together
    # key: email of the promotion
    # value: id of latest promotion from this email_address
    promotions = {}

    #Group conversation
    conversation = N_ary_Tree()

    for eml in summary:
        id = eml[0]
        info = eml[1]
        subject = info['Subject']
        # Case 1: no "In-Reply-To" && no "Re" in subject -> regard as a start of converation
        # Create a new tree
        if 'In-Reply-To' not in info and 'RE:' not in subject.upper() and 'FW:' not in subject.upper():
            
            #Case 2: promotion email from same address should be in one group
            if 'promotions' in info['From'] :

                eml = info['From'].rsplit(' ',1)[1]
                # Check if this promotion already exist
                # If not exist create new branch
                if eml not in promotions:
                    conversation.add(id)
                else:
                    p_id = promotions[eml]
                    conversation.add(id,p_id)
                promotions[eml] = id

            else:
                conversation.add(id)
                level = {1:id}
                subjects[subject] = level

        else:
            # in-reply-id exist add message
            if 'In-Reply-To' in info:
                in_reply_to = info['In-Reply-To']
                conversation.add(id,in_reply_to)
                if ('RE:' not in subject.upper()):
                    subjects[subject][1] = id
            
            # if message is reply to some message
            if 'RE:' in subject.upper():
                fw_re_email('RE',subject)

            # Dealing with forward message:
            elif 'FW:' in subject.upper():
                fw_re_email('FW',subject)

    # List contains all the conversation
    conversations = conversation.branches(conversation.root)
    
    # Output result in terminal and written to file
    output(conversations)
    write_result_file(conversations)



