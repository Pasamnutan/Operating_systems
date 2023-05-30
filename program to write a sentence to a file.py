# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:59:12 2023

@author: PASAM
"""

with open('file.txt', 'w') as f:
	# Define the data to be written
	data = ['This is the first line', 'This is the second line', 'This is the third line']
	# Use a for loop to write each line of data to the file
	for line in data:
		f.write(line + '\n')
		# Optionally, print the data as it is written to the file
		print(line)
