from admin import Admin

antonio = Admin('antonio', 'berry', 'a_berry', 'a_berry@example.com', 'alaska')
antonio.describe_user()

eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
antonio.privileges.privileges = eric_privileges

print("\nThe admin " + antonio.username + " has these privileges: ")
antonio.privileges.show_privileges()