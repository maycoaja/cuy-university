import random

welcome_message = "WELCOME TO CUY GAME"
cuy_position = random.randint(1,4)

print("=====================")
print(f"={welcome_message}=")
print("=====================")

username = input("Please enter your name: ")

cave_shape = "|_|"

cave_empty = [cave_shape] * 4

cave_cuy = cave_empty.copy()
cave_cuy[cuy_position - 1] = "|˙Ⱉ˙|"

cave_empty = ' '.join(cave_empty)
cave_cuy = ' '.join(cave_cuy)

print(f'''
Hello {username}!!! See the cave below
{cave_empty}
''')

user_answer = int(input("Guess where cuy is! [1/2/3/4]: "))
verification = input("Are you sure for the answer? [y/n]")
if verification.lower() == "y":
    if cuy_position == user_answer:
        print(f"You're right, I'm here \n{cave_cuy}")
    else:
        print(f"You're wrong, I'm here \n{cave_cuy}")
else:
    exit()