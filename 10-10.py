filenames = ['10-10 txt']

print("<<<Enter 'q' to quit in any time>>>")
for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        print(f"The file: '{filename}' not found.")

    else:
        word = input(f"Enter the word you want to count in the file: \
{filename}\n: ")

        if word == 'q':
            break

        count = contents.lower().count(word)
        print(f"The word '{str(word)}' is used {str(count)} times \
in the file: '{filename}'.")
        print("---")