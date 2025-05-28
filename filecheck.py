import os
import re

directory = '/home/helloxonie/code/pythonfilecheck/env' //change to your own directory
prefix = 'file'

expected_numbers = set(range(1,6))
pattern = re.compile(rf'{re.escape(prefix)}(\d+)')

found_numbers = set()

for filename in os.listdir('/home/helloxonie/code/pythonfilecheck/env'):
    match = pattern.match(filename)
    if match:
        number = int (match.group(1))
        found_numbers.add(number)

missing_numbers = expected_numbers - found_numbers
if missing_numbers:
    print 

