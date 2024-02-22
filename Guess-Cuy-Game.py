import random

welcome_message = "WELCOME TO CUY GAME"
cuy_position = random.randint(1,4)

print("=====================")
print(f"={welcome_message}=")
print("=====================")

username = input("Please enter your name: ")
print(f'''
Hello {username}!!! See the cave below
|_|  |_|  |_|  |_|
''')

while True:
    user_answer = int(input("Guess where cuy is! [1/2/3/4]: "))

    if cuy_position == user_answer:
        print("YOU WIN!")
        break
    else:
        print(f"You wrong! Cuy is in Cave {cuy_position}")
        try_again = input("Try again? [y/n]: ")
        if try_again.lower() == "n":
            break