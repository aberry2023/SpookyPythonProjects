import re
text = 'Antonio quickly finished his homework with minimal time to spare.'
print(re.findall(r"\b\w{7}\b", text))