import re

key_space = re.compile(r'Key.space')
key_enter = re.compile(r'Key.enter')

string1 = '2021-10-09 14:32:24,396: Key.space'
string2 = '2023-05-02 20:04:58,462: Key.enter'
string2 = '2023-05-02 20:04:58,462: Kdy.dsadadsater'
print(key_space.findall(string1))
print(key_enter.findall(string2))
