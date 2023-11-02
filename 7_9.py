sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'cheese', 'pastrami']
finished_sandwiches = []

print("I apologize, we are out of pastrami currently.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Working on your " + current_sandwich + "sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + "sandwich")