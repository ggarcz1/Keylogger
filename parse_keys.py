
import re

date = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
time = re.compile(r'\b\d{2}:\d{2}:\d{2}\b')
character = re.compile(r'\b\w{1}\b')
# 2021-05-20 17:25:10,743: 'h'
# 2021-05-20 17:25:16,344: '\x01'
# 2021-05-20 17:25:16,679: Key.backspace


# TODO:
# how to add the Key.??? or the \x01 in??
# could hardcode each Key.??? since they are limited

output_string = ''
f = open('keylogs.txt', 'r')
for line in f:
    # matches = character.findall(line)
    try:
        output_string += character.findall(line)[0]
    except:
        continue

# matches = date.findall(value)
# print(matches)
# matches = time.findall(value)
# print(matches)
# matches = character.findall(value)
# print(matches[0])
print(output_string)