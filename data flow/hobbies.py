def get_username():
    username = input("what is your name")
    return username

def get_age(newname):
    age= input(newname + "enter youre age")
    return age

def get_hobbies(othernewname):
    hobbies= []
    for x in range(10):
        hobby= input(othernewname + "enter hobbies")
        hobbies.append(hobby)

#main
global_user = get_username()
print(global_user)

global_age = get_age(global_user)
print(global_age)




    