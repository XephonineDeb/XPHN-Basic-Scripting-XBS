#cd "/sdcard/python/XPHN/py/src/geeksforgeeks.org/"
#python xphn-alpha.py tests.py
from lexer import *
from parser import *
from exec import *
from sys import argv

lexer = BasicLexer() 
parser = BasicParser() 
env = {} 
f=open(argv[-1],"r")
d=f.readlines()
f.close()
for text in d:
	tree = parser.parse(lexer.tokenize(text)) 
	BasicExecute(tree, env)
