
import re

date = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
time = re.compile(r'\b\d{2}:\d{2}:\d{2}\b')
character = re.compile(r'\b\w{1}\b')
key_value = re.compile(r'\bKey.\w{1,10}\b')
key_space = re.compile(r'Key.space')
key_enter = re.compile(r'Key.enter')
key_backspace = re.compile(r'Key.backspace')
# 2021-05-20 17:25:10,743: 'h'
# 2021-05-20 17:25:16,344: '\x01'
# 2021-05-20 17:25:16,679: Key.backspace

# non printable characters:
# https://condor.depaul.edu/sjost/lsp121/documents/ascii-npr.htm

# TODO:
# how to add the Key.??? or the \x01 in??
# could hardcode each Key.??? since they are limited

output_string = ''
f = open('keylogs.txt', 'r')
for line in f:
    # value = character.findall(line)
    # print()
    # matches = character.findall(line)
    try:
        value = character.findall(line)
        space_search = key_space.findall(line)
        enter_search = key_enter.findall(line)
        backspace_search = key_backspace.findall(line)

        # space
        if (len(space_search) != 0):
            output_string += ' '
        # enter
        elif(len(enter_search) != 0):
            output_string += '\n'
        # backspace
        elif(len(backspace_search) != 0):
            output_string += '<BSPACE>'
        # char value
        elif(len(value) != 0):
            output_string += value[0]
        # else:
        #     output_string += 'UNKNOWN\n'
            
    except:
        continue

print(output_string)