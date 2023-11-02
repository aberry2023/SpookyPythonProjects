filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you enjoy programming? ")
    responses.append(response)

    continue_poll = input("Anything else (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")