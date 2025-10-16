import random
import string
domains=['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
with open('mails.txt','w') as f:
    unique=[]
    for i in range(700000):
        username=''.join(random.choices(string.ascii_lowercase+string.digits,k=8))
        domain=random.choice(domains)
        email=f"{username}@{domain}"
        unique.append(email)
        f.write(email+'\n')
    for i in range(300000):
        f.write(random.choice(unique)+'\n')