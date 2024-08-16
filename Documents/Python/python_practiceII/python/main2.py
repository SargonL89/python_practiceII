from sys import path

path.append('..\\packages')

import extra.iota

print(extra.iota.FunI())

import extra.good.best.sigma as sig
from extra.good.best.tau import FunT

print(sig.FunS())
print(FunT())