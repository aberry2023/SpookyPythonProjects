current_users = ('tobias', 'joel', 'ben', 'steph', 'admin')
new_users = ('Tobias', 'Joel', 'christa', 'talon', 'allie')
current_users_lower = (user.lower() for user in current_users)
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print ("My apologies " + new_user + ", that name is unavailable.")
    else:
        print("Good, "+ new_user + ", that name is available.")