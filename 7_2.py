group_size = input("How many people are in your group?")
group_size = int(group_size)

if group_size > 8:
    print("We apologize, you will have a waiting period for your servicing.")
else:
    print("Your table is ready.")