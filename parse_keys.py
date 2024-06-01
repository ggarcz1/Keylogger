import re

date = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
time = re.compile(r'\b\d{2}:\d{2}:\d{2}\b')
# character = re.compile(r'\b\w{1}\b')
character = re.compile(r'\b\w\b')

key_value = re.compile(r'\bKey.\w{1,10}\b')
key_space = re.compile(r'Key.space')
key_enter = re.compile(r'Key.enter')
key_backspace = re.compile(r'Key.backspace')
key_shift = re.compile(r'Key.shift')
key_tab = re.compile(r'Key.tab')
key_cmd = re.compile(r'Key.cmd')
key_l = re.compile(r'Key.left')
key_r = re.compile(r'Key.right')
key_u = re.compile(r'Key.up')
key_d = re.compile(r'Key.down')


# key_ctr_l = re.compile(r'Key.ctrl_l')
# key_ctr_l = re.compile(r'Key.ctrl_r')
# key_alt_l = re.compile(r'Key.alt_l')
# key_alt_r = re.compile(r'Key.alt_r')
# key_hex = (r'\x{}{}')

# non printable characters:
# https://condor.depaul.edu/sjost/lsp121/documents/ascii-npr.htm

# TODO:
def log(data) -> None:
    f_write = open('Parse_logs.txt', 'w')
    f_write.write(data)
    f_write.close()


output_string = ''
f = open('keylogs.txt', 'r')
for line in f:
    value = character.findall(line)
    space_search = key_space.findall(line)
    enter_search = key_enter.findall(line)
    backspace_search = key_backspace.findall(line)
    shift_search = key_shift.findall(line)
    tab_search = key_tab.findall(line)
    cmd_search = key_cmd.findall(line)
    left_search = key_l.findall(line)
    right_search = key_r.findall(line)
    up_search = key_u.findall(line)
    down_search = key_d.findall(line)

    # if len(KEYNAME_search) != 0:
    #     output_string += 'value_to_id_key'
    # space
    if len(space_search) != 0:
        output_string += ' '
    # enter
    elif len(enter_search) != 0:
        output_string += '\n'
    # tab
    elif len(tab_search) != 0:
        output_string += '<TAB>'
    # cmd
    elif len(cmd_search) != 0:
        output_string += '<CMD>'
    # backspace
    elif len(backspace_search) != 0:
        output_string += '<BSPACE>'
    # shift
    elif len(shift_search) != 0:
        output_string += '<SHIFT>'
    # up
    elif len(up_search) != 0:
        output_string += '<UP>'
    # down
    elif len(down_search) != 0:
        output_string += '<DOWN>'
    # left
    elif len(left_search) != 0:
        output_string += '<LEFT>'
    # right
    elif len(right_search) != 0:
        output_string += '<RIGHT>'
    # char or numerical value
    elif len(value) != 0:
        output_string += value[0]
    else:
        # remove new line
        # output_string += line[25:][:-1]
        output_string += line[25:]

log(output_string)
print(output_string)
