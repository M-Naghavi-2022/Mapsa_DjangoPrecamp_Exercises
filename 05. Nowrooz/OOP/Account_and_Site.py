
from hashlib import sha256
import re

class Account(object):

    def __init__(self, username, password, phone_number, email) -> None:
        
        if re.fullmatch(r'[a-zA-Z]+[_][a-zA-Z]+', username):
            self.username = username
        else:
            raise Exception("invalid username")
        
        if re.fullmatch(r'(?=\S*[A-Z])(?=\S*[a-z])(?=\S*\d)\S{8,}', password):
            self.password = sha256(password.encode('utf-8'))
        else:
            raise Exception("invalid password")

        if re.fullmatch('09[0-9]{9}', phone_number):    
            self.phone_number = phone_number
        elif re.fullmatch('[+]989[0-9]{9}', phone_number):
            self.phone_number = '0'+phone_number[3:]
        else:
            raise Exception("invalid phone number")

        if re.fullmatch('([\w.-]+)@([\w.-]+)\.([a-zA-Z]{2,5})', email):
            self.email = email
        else:
            raise Exception("invalid email")
        #print("account created")
        

class Site(object):

    def __init__(self, url):
        self.url = url
        self.register_users = []
        self.active_users = []

    def register(self, account):
        if account not in self.register_users:
            self.register_users.append(account)
            print("register successful")
        else:
            raise Exception("user already registered")
        #print(self.register_users)

    def login(self, username = None, email = None, password = None):
        
        if username and email:
            for i in self.active_users:
                if (i.username == username) and (i.email == email):
                    print("user already logged in")
                    break
            else:
                for j in self.register_users:
                    if (j.username == username) and (j.email == email):
                        if j.password.digest() == sha256(password.encode('utf-8')).digest():
                            self.active_users.append(j)
                            print("login successful")
                            break
                else:
                    print("invalid login")
        
        elif username:
            for i in self.active_users:
                if i.username == username:
                    print("user already logged in")
                    break
            else:
                for j in self.register_users:
                    if j.username == username:
                        if j.password.digest() == sha256(password.encode('utf-8')).digest():
                            self.active_users.append(j)
                            print("login successful")
                            break
                else:
                    print("invalid login")

        elif email:
            for i in self.active_users:
                if i.email == email:
                    print("user already logged in")
                    break
            else:
                for j in self.register_users:
                    if j.email == email:
                        if j.password.digest() == sha256(password.encode('utf-8')).digest():
                            self.active_users.append(j)
                            print("login successful")
                            break
                else:
                    print("invalid login")

        else:
            print("invalid login")
        #print(self.active_users)

    def logout(self, account):
        if account in self.active_users:
            self.active_users.remove(account)
            print("logout successful")
        else:
            print("user is not logged in")
        #print(self.active_users)

    
### tests
a = Account("mohammad_naghavi","AsDf1234","+989145631239","q@w.er")
b = Account("ali_bandari","5678asdF", "09123456789", "a@s.df")
# print(a.username)
# print(b.username)

y = Site("www.zxc.vbn")
z = Site("www.mapsa.hr")

y.register(a)
y.register(b)
y.login(email='q@w.er',password='AsDf1234')
y.login("ali_bandari","a@s.df", password="5678asdF")
y.logout(a)
y.logout(b)
z.register(a)
z.login("mohammad_naghavi","q@w.er","AsDf1234")
# print(y.url,'*****',z.url)
# print(y.register_users,'*****',z.register_users)
# print(y.active_users,'*****',z.active_users)
