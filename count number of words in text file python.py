# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:30:18 2023

@author: PASAM
"""

file = open("C:\data.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))
