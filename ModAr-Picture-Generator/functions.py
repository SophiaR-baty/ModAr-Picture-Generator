import math
import png
import os.path
from os import system, name
import json

#clear screen
def cls():
	# for windows os
	if name == 'nt': 
		_ = system('cls') 
  
	# for mac and linux os(The name is posix)
	else: 
		_ = system('clear')

def get_function_presets():
	presets = dict()
	
	if os.path.exists("presets.json"):
		with open("presets.json") as f:
			presets = json.load(f)
	return presets

def append_presets(name, function):
	presets = get_function_presets()
	if not name in list(presets.keys()):
		presets[name] = function
		with open("presets.json") as f:
			json.dump(presets, f)

def delete_preset(name):
	presets = get_function_presets()
	if name in list(presets.keys()):
		presets.pop(name)
		with open("presets.json") as f:
			json.dump(presets, f)

# Constants and Functions from Math
e = math.e
pi = math.pi
def sin(x):
	return math.sin(x)
def sinh(x):
	return math.sinh(x)
def asin(x):
	return math.asin(x)
def asinh(x):
	return math.asinh(x)
def cos(x):
	return math.cos(x)
def cosh(x):
	return math.cosh(x)
def acos(x):
	return math.acos(x)
def acosh(x):
	return math.acosh(x)
def tan(x):
	return math.tan(x)
def tanh(x):
	return math.tanh(x)
def atan(x):
	return math.atan(x)
def atanh(x):
	return math.atanh(x)
def exp(x):
	return math.exp(x)
def m_sum(list):
	return math.fsum(list)
def m_prod(list):
	return math.prod(list)
def gamma(x):
	return math.gamma(x)
def lgamma(x):
	return math.lgamma(x)
def ln(x):
	return math.log(x)
def log(x, b):
	return math.log(x, b)
def sqrt(x):
	return math.sqrt(x)
def root(x, n):
	return x**(1/n)
def floor(x):
	return math.floor(x)
def ceil(x):
	return math.ceil(x)
def ign(x,ign,ret=1):
	if x == ign:
		return ret
	else:
		return x
def grt(a,b):
	if a > b:
		return a
	else:
		return b
def lss(a,b):
	if a < b:
		return a
	else:
		return b
def sign(x):
	if x >= 0:
		return 1
	else:
		return -1
def rowAdd(a, b):
	#print(a, b)
	#print()
	if a == b:
		return a
	if a == -b or b == a-1:
		return 0
	if a == 0:
		return (b**2 + b)/2
	else:
		c = min([a, b])
		return c - c*(a-b) - rowAdd(0, -(a-c)) + rowAdd(0, (b-c))