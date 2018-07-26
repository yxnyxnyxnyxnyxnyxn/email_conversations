# Set up
import os,glob
from datetime import datetime


class Node:
    def __init__(self,key, children =None):
        self.key = key
        self.children = children or []

    def __str__(self):
        return str(self.key)


class N_ary_Tree:

    def __init_(self):
        self.root = None
        self.size = 0

    def find_node(self,node,key):
        if node == None or node.key == key:
            return node

        for child in node.children:
            found = self.find_node(child,key)
            if found:
                return found

        return None


def add(self,new_key,parent_key= None):
    new_node =Node(new_key)
    if parent_key == None:
        self.root = new_node
    
    else:
        parent_node = self.find_node(self.root,parent_key)
        parent_node.children.append(new_node)

def print_tree(self,node, str_aux):
    str_aux += str(node) +'('
    for i in range(len(node.children)):
        child =node.children[i]
        end = ',' if i < len(node.children) - 1 else ''
        str_aux= self.print_tree(child,str_aux) + end
    str_aux += ')'
    return str_aux

def __str__(self):
    return self.print_tree(self.root,"")




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
                if info[0] == 'Date':
                    time = info[1].split('+',1)[0]
                    infos['Date'] = datetime.strptime(time, ' %d %b %Y %H:%M:%S ')
                else:
                    infos[info[0]] = info[1]
    return [key,infos]


# Function to Read all plain text file in raw_emails dictionary
def read_folder(path):
    infos = {}
    for fle in glob.glob(path):
        with open(fle,'r') as f:
            infos = parse_email(f)
        summary[infos[0]] = infos[1]






#---------------Main--------------#

path = 'raw_emails/*'
# summary: 2d dictionary to store each email's infomation
# key: email-id value: {In-Reply-To, Subject,  Date}
summary = {}
read_folder(path)
# Sort the email by date
emails = {}
summary = sorted(summary.items(),key = lambda kv: kv[1]['Date'])

# Final Result



#Group conversation

#Case 1: no "In-Reply-To" && no "Re" in subject -> regard as a start of converation
#Case 2: promotion email from same address should be in one group
for eml in summary:
    id = eml[0]
    info = eml[1]
    if 'In-Reply-To' not in info and 'Re' not in info['Subject']:
        #Case 2: promotion email from same address should be in one group
        if 'promotions' in info['From'] and
    else:
        pass
