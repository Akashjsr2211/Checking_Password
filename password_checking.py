import re

def checking_password(password):
    if not re.search(r'[A-Z]',password):
        print("Atleast one uppercase letter must.")
        return False
    
    if not re.search(r'[a-z]',password):
        print("Atleast one lowercase letter must.")
        return False
    
    if not re.search(r'[0-9]',password):
        print("Numerical value is must.")
        return False
    
    if not re.search(r'[!@#$%^&*_\+\-=:;"<>?/\\|~`.]',password):
        print("Special character is must.")
        return False

    else:
        return True
    

while(True):
    password = input("Enter your password: ")
    if not checking_password(password):
        print("Weak password !")
    else:
        print("Strong password ! Ready to use.")
    print("Press 'q' for quit.")
    if password=='q':
        break
