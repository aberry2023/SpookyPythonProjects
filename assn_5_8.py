users = ('Becky', 'Cynthia', 'Armando', 'Nate', 'admin')
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hey there " + 'user', "nice to see you here again!")
