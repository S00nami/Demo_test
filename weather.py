my_str= "Hi "
name= input("What is your name?").capitalize()
weather= input("What is the weather like today? ").lower()

def greeting():
    return f"{my_str} {name}, the weather forcast today is {weather}"

print(greeting())
