seen=set()
unique=0
inp=['abc@gmail.com','pqr@yahoo.com','abc@gmail.com','mno@gmail.com']
res=[]
for email in inp:
    email=email.strip()
    if email and email not in seen:
        seen.add(email)
        res.append(email)
        unique+=1
print(res)