import textemails, re

# email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # username
    @                  # at symbol
    [a-zA-Z0-9.-]+     # domain name
    (\.[a-zA-Z]{2-4})  #dot-something
    )''', re.VERBOSE)

# find matches in clipboard text
text = str(textemails.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy results to the clipboard
if len(matches) > 0:
    textemails.copy('\n'.join(matches))
    print ('Copied to clipboard:')
    print ('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')