#!/usr/bin/env python3
import os

directory = 'env'
for i in range(1,6):
    filename = f"{directory}/file{i}randomwords.txt"
    with open(filename, 'a'):
        pass

