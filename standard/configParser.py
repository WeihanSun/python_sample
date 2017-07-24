# read and write *.ini file
# get environment parameters
# random

import configparser
import sys
import os
import random


# get 1st environment param and its content
for env in os.environ:
    print(env)
    print(os.environ.get(env))
    break

# random
print(random.random())
print(random.uniform(1, 100))
print(random.randint(1, 100))
print(random.choice('123456789abcdef'))  # hex
sample_list = ['python', 'izm', 'com', 'random', 'sample']
random.shuffle(sample_list)
print(sample_list)

# read and write ini file
fileName = 'config.ini'
inifile = configparser.ConfigParser()
inifile.sections()
inifile.read(fileName)

print(inifile.get('settings', 'host'))
print(inifile['settings']['host'])
# write ini file
print('Enter a new hostname')
inifile['settings']['host'] = sys.stdin.readline()
print(inifile['settings']['host'] + 'is set as hostname')
with open(fileName, 'w') as configFile:
    inifile.write(configFile)



