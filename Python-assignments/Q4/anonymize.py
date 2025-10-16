import hashlib
import re
import csv 

def hash_email(email):
    return hashlib.sha256(email.lower().strip().encode()).hexdigest()

# def mask_phone(phone):
#     digits=re.findall(r'\d', phone)
#     if len(digits)<4:
#         return 'X'*len(phone)
#     digits=''.join(digits[-4:])
#     x=len(phone)-4
#     return 'X'*x+digits

def mask_phone(phone):
    digits=re.findall(r'\d',phone)
    if len(digits)<4:
        return re.sub(r'\d','X',phone)
    to_keep=digits[-4:]
    to_mask=len(digits)-4
    masked=''
    count=0 
    for char in phone:
        if char.isdigit():
            if count<to_mask:
                masked+='X'
            else:
                masked+=to_keep[count-to_mask]
            count+=1
        else:
            masked+=char
    return masked

with open("people-100000.csv",'r') as infile:
    reader=csv.reader(infile)
    rows=[]
    for row in reader:
        rows.append(row)
for i in range(1,len(rows)):
    rows[i][1]=hash_email(rows[i][1])  
    rows[i][2]=mask_phone(rows[i][2]) 

with open("anonymized_file.csv",'w',newline='') as outfile:
    writer=csv.writer(outfile)
    for row in rows:
        writer.writerow(row)