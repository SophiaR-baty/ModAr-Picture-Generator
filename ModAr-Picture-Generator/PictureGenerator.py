import math
from functions import *
import png
import os.path
from os import system, name
import creategif

def rgb(h, maxv):
	r = 0
	g = 0
	b = 0
	if h <= 60 or h >=300:
		r = maxv
	elif h >= 120 and h <= 240:
		r = 0
	elif h >= 60 and h <= 120:
		r = maxv-maxv*(h-60)/60
	elif h >= 240 and h<= 300:
		r = maxv*(h-240)/60
	if r < 0:
		r = 0
		
	if h >= 60 and h <= 180:
		g = maxv
	elif h >= 240:
		g = 0
	elif h >= 0 and h <= 60:
		g = maxv*h/60
	elif h >= 180 and h <= 240:
		g = maxv-maxv*(h-180)/60
	if g < 0:
		g = 0
		
	if h >= 180 and h <= 300:
		b = maxv
	elif h >= 0 and h <= 120:
		b = 0
	elif h >= 120 and h <= 180:
		b = maxv*(h-120)/60
	elif h >= 300 and h <= 360:
		b = maxv-maxv*(h-300)/60
	if b < 0:
		b = 0
	
	return [r, g, b]


def func(num, function, x, y, i):
	return eval(function)


class Generator:
	
	#algorithm
	def createData(num, modLimLow, modLimUp, height, width, x_0, y_0, fact_x, fact_y, parameter = 1, function = "x*y*i"):
		print("creating image data...")
		mod = []
		for i in range(height):
			for j in range(width):
				try:
					a = func(num, function, (x_0+j)*fact_x, (y_0+i)*fact_y, parameter)%num
					if modLimLow < modLimUp:
						if a >= modLimLow and a <= modLimUp:
							mod.append(a)
						else:
							mod.append(-1)
					else:
						if a >= modLimLow and a <= modLimUp:
							mod.append(-1)
						else:
							mod.append(a)
				except ValueError:
					mod.append(-1)
		return mod
	
	#making image
	def writeImage(mod, num, height, width, col_min, col_sat, inval_col, path_out):
		#creating picture
		pic = list()
		for i in range(height):
			pic.append(list())

		col_co = 360/num

		for i in range(height):
			for j in range(width):
				for k in range(0, 3):
					if mod[i*width+j] >= 0:
						pic[i].append(math.floor(
						
						rgb((col_min + col_co*mod[i*width+j])%360,col_sat)[k]))
					else:
						pic[i].append(inval_col[k])
		cls()
		print("image data created")
		
		#saving
		w = png.Writer(width=width, height=height, greyscale=False)
		f = open(path_out+'.png', 'wb')
		w.write(f, pic)
		f.close()

	def makePicture(num = 500, 
		modLimLow = 0,
		modLimUp = 501,
		col_min = 0, 
		col_sat = 255,
		inval_col = [0, 0, 0],
		height = 500, 
		width = 500, 
		x_0 = 250, 
		y_0 = 250, 
		fact_x = 1, 
		fact_y = 1, 
		parameter = 1,
		function = "prod",
		filename = ""
		):
			
			mod = Generator.createData(num, modLimLow, modLimUp, height, width, x_0, y_0, fact_x, fact_y, parameter, function)
			Generator.writeImage(mod, num, height, width, col_min, col_sat, inval_col, "Output\\"+filename)
	
	def exportTxt(num = 500, 
		modLimLow = 0,
		modLimUp = 501,
		col_min = 0, 
		col_sat = 255,
		inval_col = [0, 0, 0],
		height = 500, 
		width = 500, 
		x_0 = 250, 
		y_0 = 250, 
		fact_x = 1, 
		fact_y = 1, 
		parameter = 1,
		function = "prod",
		filename = ""):
			
			content = ""
			for s in (str(num), str(modLimLow), str(modLimUp), str(col_min), str(col_sat), str(inval_col), str(height), str(width), str(x_0), str(y_0), str(fact_x), str(fact_y), str(parameter), str(function)):
				content += s + ", "
			
			with open("Output/"+filename+".txt", 'w') as f:
				f.write(content)