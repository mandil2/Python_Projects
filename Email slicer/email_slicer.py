email=input('Enter your email: ')
lst=email.split('@')
username=lst[0]
domain_name=lst[1]
print('Username is',username,'and domain name is',domain_name)