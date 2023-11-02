name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would you choose? "
continue_prompt = "\nWould you like to let someone else respond? (Y/N)"

responses = {}
while True:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

print("\n---Results ---")
for name, place in responses.items():
    print(name.title() + "would like to visit " + place.title() + ".")