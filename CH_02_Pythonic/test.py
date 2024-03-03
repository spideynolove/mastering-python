# try:
#     value = int(user_input)
#     print(value)
# except:
#     print(f"Error at {user_input}")

user_input = input("Pass an integer number?\n")
print(user_input.isdigit())

# while True:
#     user_input = input("Pass an integer number?\n")
#     if not user_input.isdigit():
#         print("not a number")
#         continue 