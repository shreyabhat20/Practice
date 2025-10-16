seen=set()
unique=0
#res=[]
with open('uniquemail.txt','w') as out:
    with open('mails.txt','r') as inp:
        for email in inp:
            email= email.strip()
            if email and email not in seen:
                seen.add(email)
                out.write(email + '\n')
                #res.append(email)
                unique+= 1
print(f"{unique} unique emails")