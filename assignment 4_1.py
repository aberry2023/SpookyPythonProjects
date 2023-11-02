favorite_pizzas = ('pepperoni', 'bbq', 'supreme')
for pizza in favorite_pizzas:
    print(pizza)

print("\n")
for pizza in favorite_pizzas:
    print("I enjoy " + pizza + "pizza!")

print("\nI enjoy pizza!")

numbers = [num for num in range(1,11)]
print(numbers[:3])
print(numbers[3:6])
print(numbers[-3])

pizzas = ["mushroom", "hawaiian", "teremena"]
friend_pizzas = pizzas[:]
pizzas.append("ham")
friend_pizzas.append("chicken")
print("my favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print("\n")
print("my friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)