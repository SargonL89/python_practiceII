from sys import path
import os

path.append('..\\module')
# Alternative: path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module')))

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))