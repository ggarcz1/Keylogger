
import re

date = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
time = re.compile(r'\b\d{2}:\d{2}:\d{2}\b')
character = re.compile(r'\b\w{1}\b')
key_value = re.compile(r'\bKey.\w{1,10}\b')
key_space = re.compile(r'Key.space')
key_enter = re.compile(r'Key.enter')
key_backspace = re.compile(r'Key.backspace')
# key_ctr_l = (r'Key.ctrl_l')
# key_ctr_l = (r'Key.ctrl_r')
# key_alt_l = (r'Key.alt_l')
# key_alt_r = (r'Key.alt_r')
# key_tab = (r'Key.tab')
# key_cmd = (r'Key.cmd')
# key_ctr_shift = (r'Key.shift')
# key_ctr_lrud = (r'\bKey.{left,right,up,down}\b')
# key_hex = (r'\x{}{}')

# non printable characters:
# https://condor.depaul.edu/sjost/lsp121/documents/ascii-npr.htm

# TODO:
def log(value) -> None:
    f = open('Parse_logs.txt' 'a')
    f.write(value)
    f.close()

output_string = ''
f = open('keylogs.txt', 'r')
for line in f:
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
    # char or numerical value
    elif(len(value) != 0):
        output_string += value[0]
    else:
        # remove new line
        # output_string += line[25:][:-1]
        output_string += line[25:]


print(output_string)