#!/usr/bin/python3
"""Final task"""

from sys import stdin

status_codes = {
	'200': 0,
	'301': 0,
	'400': 0,
	'401': 0,
	'403': 0,
	'404': 0,
	'405': 0,
	'500': 0,
	}
	
total_size = i = 0

def printer():
	"""this function prints the statistic"""
	print(f'File size: {total_size}')
	for key, value in sorted(status_codes.items()):
		if value > 0:
			print('{:s}: {:d}'.format(key, value))
			
try:
	for line in stdin:
		splitted_line = line.split()
		if len(splitted_line) >= 2:
			status = splitted_line[-2]
			total_size += int(splitted_line[-1])
			if status in status_codes:
		i += 1
		
		if i % 10 == 0:
			printer()
		printer()
	except Keyboardinterrupt as e:
		printer
