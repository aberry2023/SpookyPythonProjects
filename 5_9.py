usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, do you want to view the updated status report?")
        else:
            print("Hello " + username + '. thank you for logging in again!')
else:
    print("We need to find some users!")
