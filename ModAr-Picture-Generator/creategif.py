import imageio as iio
import numpy as np
import os

def filesIn(dir, ext = ".png"):
	files_in = list()
	path_in = dir
	root = next(os.walk(dir))[0]
	for file in next(os.walk(dir))[2]:
		if file.endswith(ext):
			files_in.append(os.path.join(root,file))
		else: print(file)
	return files_in

def createGif(path_in, path_out, speed):
	filenames = filesIn(path_in)
	
	with iio.get_writer(path_out, mode='I', duration = speed) as writer:
		for filename in filenames:
			image = iio.imread(filename)
			writer.append_data(image)