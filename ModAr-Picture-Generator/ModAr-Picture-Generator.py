import dearpygui.dearpygui as dpg
import PictureGenerator
import os
from functions import *
import clipboard
import time

dpg.create_context()

def show_picture(file):
	time.sleep(1)
	width, height, channels, data = dpg.load_image(file)
	pic = dpg.add_static_texture(width, height, data, parent = "Created Pictures")
	#dpg.configure_item("Created Pictures", show=True)
	with dpg.window(label = file, indent = 3, height = height+36, width = width+16, no_resize = True):
		dpg.add_image(pic)

def pic_save_button_callback():
	user_data = {"mod_num": dpg.get_value(mod_num),
		"mod_lim_low": dpg.get_value(mod_lim_low),
		"mod_lim_up": dpg.get_value(mod_lim_up),
		"col_min": dpg.get_value(col_min),
		"col_sat": dpg.get_value(col_sat),
		"inval_col": dpg.get_value(inval_col)[:3],
		"width": dpg.get_value(size)[0],
		"height": dpg.get_value(size)[1],
		"shift_x": dpg.get_value(shift)[0],
		"shift_y": dpg.get_value(shift)[1],
		"fact_x": dpg.get_value(fact)[0],
		"fact_y": dpg.get_value(fact)[1],
		"function": dpg.get_value(function),
		"parameter": dpg.get_value(parameter),
		"file_name": dpg.get_value(file_name),
		
		"save_txt": dpg.get_value(save_txt),
		"save_pic": dpg.get_value(save_pic)}
	
	#setting filename
	if not os.path.isdir("Output"):
		os.makedirs("Output")
	if user_data["file_name"] == "":
		user_data["file_name"] = "picture"
	if os.path.exists("Output/"+user_data["file_name"]+'.png') or os.path.exists("Output/"+user_data["file_name"]+'.txt'):
		n = 1
		while os.path.exists("Output/"+user_data["file_name"]+"_"+str(n)+'.png') or os.path.exists("Output/"+user_data["file_name"]+"_"+str(n)+'.txt'):
			n += 1
		user_data["file_name"] += "_"+str(n)
	
	#creating picture/text
	if user_data["save_pic"]:
		PictureGenerator.Generator.makePicture(num = user_data["mod_num"], modLimLow = user_data["mod_lim_low"], modLimUp = user_data["mod_lim_up"], col_min = user_data["col_min"], col_sat = user_data["col_sat"], inval_col = user_data["inval_col"], height = user_data["height"], width = user_data["width"], x_0 = user_data["shift_x"], y_0 = user_data["shift_y"], fact_x = user_data["fact_x"], fact_y = user_data["fact_y"], function = user_data["function"], parameter = user_data["parameter"], filename = user_data["file_name"])
		
		#display file
		show_picture("Output/"+user_data["file_name"]+".png")

		#with dpg.window(label = user_data["file_name"]):
	if user_data["save_txt"]:
		PictureGenerator.Generator.exportTxt(num = user_data["mod_num"], modLimLow = user_data["mod_lim_low"], modLimUp = user_data["mod_lim_up"], col_min = user_data["col_min"], col_sat = user_data["col_sat"], inval_col = user_data["inval_col"], height = user_data["height"], width = user_data["width"], x_0 = user_data["shift_x"], y_0 = user_data["shift_y"], fact_x = user_data["fact_x"], fact_y = user_data["fact_y"], function = user_data["function"], parameter = user_data["parameter"], filename = user_data["file_name"])
	
	
def copy_to_clipboard():
	print("not supported yet")
	#a = ""
	#clipboard.copy(a)

def save_preset(user_data):
	with dpg.popup(dpg.last_item(), modal=True, mousebutton=dpg.mvMouseButton_Left, no_move=True):
		dpg.add_text("Save Preset as")
		dpg.add_input_text(label="Name")
		with dpg.group(horizontal=True):
			dpg.add_button(label="OK", width=75, callback=save_preset)
			dpg.add_button(label="Cancel", width=75, callback=save_preset)


def edit_function_presets():
	with dpg.window(label = "Function Presets Editor", tag = "FPE"):
		menu_bar()
		
		presets = get_function_presets()
		items = list(presets.keys())
		
		with dpg.group(horizontal=True):
			dpg.add_listbox(items, width=200, num_items=-1)
			with dpg.group():
				dpg.add_input_text(width=-1)
				dpg.add_button(label="Save as", callback=save_preset)
	dpg.set_primary_window("FPE", True)
	
	
def pic_set_all(**kwargs):
	for arg in kwargs:
		if not arg in ["mod_num", "mod_lim_low", "mod_lim_up", "col_min", "col_sat", "inval_col", "size", "shift", "fact", "function", "parameter"]:
			return
	for arg in kwargs:
		a = kwargs[arg]
		if arg == "mod_num": dpg.set_value(mod_num, a)
		elif arg == "mod_lim_low": dpg.set_value(mod_lim_low, a)
		elif arg == "mod_lim_up": dpg.set_value(mod_lim_up, a)
		elif arg == "col_min": dpg.set_value(col_min, a)
		elif arg == "col_sat": dpg.set_value(col_sat, a)
		elif arg == "inval_col": dpg.set_value(inval_col, a)
		elif arg == "size": dpg.set_value(size, a)
		elif arg == "shift": dpg.set_value(shift, a)
		elif arg == "fact": dpg.set_value(fact, a)
		elif arg == "function": dpg.set_value(function, a)
		elif arg == "parameter": dpg.set_value(parameter, a)

def menu_bar():
	with dpg.menu_bar():
		with dpg.menu(label="File"):
			dpg.add_menu_item(label="Save Picture", callback=lambda:pic_save_button_callback())
			#dpg.add_menu_item(label="Import .txt")
		with dpg.menu(label="Edit"):
			dpg.add_menu_item(label="Reset", callback=lambda:pic_set_all(mod_num=500, mod_lim_low=0, mod_lim_up=99999, col_min=0, col_sat=255, inval_col=[0,0,0], size=(500, 500), shift=(250,250), fact=(1,1), function="x*y*i", parameter=1))
			#dpg.add_menu_item(label="Copy To Clipboard", callback=lambda:copy_to_clipboard())
		with dpg.menu(label="Tools"):
			dpg.add_menu_item(label="Edit Function Presets", callback=edit_function_presets)
		with dpg.menu(label="Window"):
			dpg.add_menu_item(label="Toggle Fullscreen", check=True, callback=lambda:dpg.toggle_viewport_fullscreen())
			dpg.add_menu_item(label="Show Texture Registry", callback=lambda:dpg.configure_item("Created Pictures", show=True))
		with dpg.menu(label="?"):
			pass
	

with dpg.window(label = "TITLE", tag = "Primary Window"):
	#texture registry
	dpg.add_texture_registry(tag="Created Pictures", show=False, label="Created Picture")
	
	menu_bar()
	
	with dpg.collapsing_header(label = "Modulus Number"):
		with dpg.group(horizontal=True):
			mod_num = dpg.add_input_int(width = 200, indent = 10, min_value = 1, max_value = 999999, min_clamped = True, max_clamped = True, default_value = 500)
			dpg.add_text("Modulus Number", tag = "mod_num")
		with dpg.tooltip("mod_num"):
			dpg.add_text("Every pixel of the picture will be assigned the value function(x,y) mod n where n is this Modulus Number", wrap = 200)
		
		with dpg.group(horizontal=True):
			mod_lim_low = dpg.add_input_float(width = 200, indent = 10, min_value = 0, max_value = 999999, min_clamped = True, max_clamped = True, default_value = 0)
			dpg.add_text("Modulus Lower Limit", tag = "mod_lim_low")
		with dpg.tooltip("mod_lim_low"):
			dpg.add_text("Only values between the Modulus Lower and Upper Limit are drawn. Others are treated as \"invalid\". If Modulus Lower Limit > Modulus Upper Limit only values OUTSIDE this range are drawn instead.", wrap = 200)
		
		with dpg.group(horizontal=True):
			mod_lim_up = dpg.add_input_float(width = 200, indent = 10, min_value = 0, max_value = 999999, min_clamped = True, max_clamped = True, default_value = 99999)
			dpg.add_text("Modulus Upper Limit", tag = "mod_lim_up")
		with dpg.tooltip("mod_lim_up"):
			dpg.add_text("Only values between the Modulus Lower and Upper Limit are drawn. Others are treated as \"invalid\". If Modulus Lower Limit > Modulus Upper Limit only values OUTSIDE this range are drawn instead.", wrap = 200)
		
		
	with dpg.collapsing_header(label = "Color"):
		with dpg.group(horizontal=True):
			col_min = dpg.add_input_float(width = 200, indent = 10, min_value = 0, max_value = 360, min_clamped = True, max_clamped = True, default_value = 0)
			dpg.add_text("Minimal Hue", tag = "col_min")
		with dpg.tooltip("col_min"):
			dpg.add_text("Minimum Hue is the hue pixels with value 0 have.", wrap = 200)
		
		with dpg.group(horizontal=True):
			col_sat = dpg.add_input_int(width = 200, indent = 10, min_value = 0, max_value = 255, min_clamped = True, max_clamped = True, default_value = 255)
			dpg.add_text("Color Saturation", tag = "col_sat")
		with dpg.tooltip("col_sat"):
			dpg.add_text("The Saturation of the image. I might be confusing it with brightness though rip...", wrap = 200)
		
		with dpg.group(horizontal=True):
			inval_col = dpg.add_input_intx(width = 200, indent = 10, min_value = 0, max_value = 255, min_clamped = True, max_clamped = True, default_value = (0, 0, 0), size = 3)
			dpg.add_text("Invalid Color (RGB)", tag = "inval_col")
		with dpg.tooltip("inval_col"):
			dpg.add_text("Every pixel that is treated as \"invalid\" will have this color. e.g. when division by 0 occurs or the value would be outside the Modulus Limit. ", wrap = 200)
		
		
	with dpg.collapsing_header(label = "X and Y"):
		with dpg.group(horizontal=True):
			size = dpg.add_input_intx(width = 200, indent = 10, min_value = 10, max_value = 10000, min_clamped = True, max_clamped = True, default_value = (500, 500), size = 2)
			dpg.add_text("Width / Height", tag = "size")
		with dpg.tooltip("size"):
			dpg.add_text("The dimensions of the picture. Note that large pictures might take very long. I suggest not going above 10000x10000 pixels and even that might take a while already...", wrap = 200)
		
		with dpg.group(horizontal=True):
			shift = dpg.add_input_intx(width = 200, indent = 10, min_value = -999999, max_value = 999999, min_clamped = True, max_clamped = True, default_value = (250, 250), size = 2)
			dpg.add_text("X Shift / Y Shift", tag = "shift")
		with dpg.tooltip("shift"):
			dpg.add_text("This value will be added to x/y before the calculation. The exact formula is function( (x_0+x)*f_x, (y_0+y)*f_y ), where x_0, y_0 are the shift and f_x, f_y are the factors.", wrap = 200)
		
		with dpg.group(horizontal=True):
			fact = dpg.add_input_floatx(width = 200, indent = 10, min_value = -9999, max_value = 9999, min_clamped = True, max_clamped = True, default_value = (1, 1), size = 2)
			dpg.add_text("X Factor / Y Factor", tag = "fact")
		with dpg.tooltip("fact"):
			dpg.add_text("x/y will be multiplied with this value before the calculation. The exact formula is function( (x_0+x)*f_x, (y_0+y)*f_y ), where x_0, y_0 are the shift and f_x, f_y are the factors.", wrap = 200)
	
	
	
	
	with dpg.collapsing_header(label = "Function"):
		with dpg.group(horizontal=True):
			function = dpg.add_input_text(indent = 10, default_value = "x*y*i")
			dpg.add_text("Input Function", tag =  "function")
		with dpg.tooltip("function"):
			dpg.add_text("The function with which each pixels value will be calculated. ", wrap = 200)
		
		with dpg.group(horizontal=True):
			parameter = dpg.add_input_float(indent = 10, default_value = 1)
			dpg.add_text("parameter i", tag = "parameter")
		with dpg.tooltip("parameter"):
			dpg.add_text("An additional parameter. If there is no i in the function the parameter does nothing.", wrap = 200)
		
		def select_preset(sender):
			dpg.set_value(function, presets[dpg.get_value(sender)])
		presets = get_function_presets()
		items = list(presets.keys())
		with dpg.group(horizontal=True):
			presets_select = dpg.add_combo(items, indent = 10, callback = select_preset, default_value = "Product")
			dpg.add_text("presets", tag="presets")
		with dpg.tooltip("presets"):
			dpg.add_text("Some preset functions. You can add presets in the function editor (once it's implemented)", wrap = 200)
	
	with dpg.collapsing_header(label = "Save Options"):
		with dpg.value_registry():
			save_txt = dpg.add_bool_value(default_value=False, tag="save_txt")
			save_pic = dpg.add_bool_value(default_value=True, tag="save_pic")
	
		dpg.add_checkbox(label = "save .txt with data", indent = 10, source = "save_txt")
		dpg.add_checkbox(label = "save .png", indent = 10, source = "save_pic")
		file_name = dpg.add_input_text(label = "filename", indent = 10)
	
	dpg.add_button(label="Save", width = 50, height = 20, callback = lambda:pic_save_button_callback())


dpg.create_viewport(title="Modulus Picture Generator", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window("Primary Window", True)

dpg.start_dearpygui()
dpg.destroy_context()