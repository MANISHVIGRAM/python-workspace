username="mv"
password="123"
uname= input()
pword=input()
def validate():
    if (username==uname and password==pword):
        return "correct"
    else:
        return "incorrect"
print(validate())