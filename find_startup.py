import os
import subprocess
import getpass

username = getpass.getuser() 
# path = f'C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
path = r'redacted'
# write the following to the target directory

# write a python file to run later on
write_data = 'x = 5\ny = 5\nprint(x + y)'
f = open(path+'run.py', 'w')
f.write(write_data)
f.close()

subprocess.run(['python', 'run.py'])
# os.remove('find_startup.py')