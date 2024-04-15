import re
def strong_password_check():
    password=input("enter your password:")
    upper_case_check=re.compile(r'[A-Z]+').findall(password)#checks wheather the password contain upper case alphabet
    lower_case_check = re.compile(r'[a-z]+').findall(password)# checks wheather the password contain lower case alphabet
    integer_check = re.compile(r'\d+').findall(password)#checks wheather the password contains integer
    special_character_check = re.compile(r'[!@#$%^&*()_+]+').findall(password)# checks wheather the password contains special character
    if len(upper_case_check)>0 and len(lower_case_check)>0 and len(integer_check)>0 and len(password)>=8 and len(special_character_check)>0:
        print("password is strong")
    else:
        print("password is not strong")
strong_password_check()