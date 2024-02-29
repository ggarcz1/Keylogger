import re

key_space = re.compile(r'Key.space')
key_enter = re.compile(r'Key.enter')
character = re.compile(r'\b\w{1}\b')
# hex_pattern = re.compile(r'\\x[0-9A-Fa-f]{2}')


hex_pattern = re.compile(r'[0-9A-Fa-f]{2}\b')
string1 = '2021-10-09 14:32:24,396: \x01'
string2 = '2023-05-02 20:04:58,462: \xBB'
string2 = '2023-05-02 20:04:58,462: Kdy.dsadadsater'
print(hex_pattern.findall(string1))
print(hex_pattern.findall(string2))
