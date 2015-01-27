import configparser
import os
from os.path import join as join

# =========================
# globals
# =========================
env_config = None
loc_config = None
#log_file = None

working_pictures = None
curr_index = None

# =========================
# useful get list or strings
# =========================
def get_files(dir):
	for root, dirs, files in os.walk(os.getcwd()):
		files.sort()
		return files

def get_pictures(dir):
	files = get_files(dir)
	filetypes = env_config['settings']['filetypes'].split(',')
	files = [f for f in files if os.path.splitext(f)[1] in filetypes]
	return files

def get_current():
	global working_pictures, curr_index
	working_pictures = get_pictures(loc_config['paths']['working'])
	curr_index = working_pictures.indexOf(env_config['environment']['current'])
	#if (curr):

	# if not(curr in files):
	# 	if len(files) > 0:
	# 		env_config['environment']['current'] = files[0]
	# 	else:
	# 		env_config['environment']['current'] = '.'
	# return env_config['environment']['current']

def get_prev():
	None

def get_next():
	None

def get_undo():
	None

# =========================
# make/load files
# =========================
def mk_env_default():
	mk_env('.', ','.join(['.jpg', '.jpeg', '.png', '.bmp', '.gif']))

def mk_loc_default():
	testbed = join(os.getcwd(), 'testbed')
	mk_loc(
		join(testbed, 'organize'),
		join(testbed, 'working'),
		join(testbed, 'overflow'),
		join(testbed, 'transfer'),
		[])

def mk_log_default():
	# global log_file
	log_file = open('log.dat', 'w')
	# flush and close

def mk_env(current, filetypes):
	global env_config
	env_config = configparser.ConfigParser()

	env_config['environment'] = {}
	env_config['environment']['current'] = current

	env_config['settings'] = {}
	env_config['settings']['filetypes'] = filetypes

	with open('environment.ini', 'w') as configfile:
		env_config.write(configfile)

def ld_env():
	None

def mk_loc(organize, working, overflow, transfer, macro_lst):
	global loc_config
	loc_config = configparser.ConfigParser()

	loc_config['paths'] = {}
	loc_config['paths']['organize'] = organize
	loc_config['paths']['working'] = working
	loc_config['paths']['overflow'] = overflow
	loc_config['paths']['transfer'] = transfer

	loc_config['macros'] = {}
	for i in range(len(macro_lst)):
		macro_id = 'macro' + str(i)
		loc_config['macros'][macro_id] = macro_lst[i]

	with open('locations.ini', 'w') as configfile:
		env_config.write(configfile)

def ld_loc():
	None

def ap_log(entry):
	None

def rm_log():
	None

# =========================
# info commands
# =========================
def do_current():
	None

def do_count():
	return len(get_pictures(loc_config['paths']['working']))

# =========================
# action commands
# =========================
def do_show():
	None

def do_move(dest):
	None

def do_next():
	None

def do_prev():
	None

def do_undo():
	None

# =========================
# main
# =========================
def main():
	print("===ImageOrganizer===")
	mk_env_default()
	#mk
	#mk_config_default()

	print(get_files(os.getcwd()))
	print(get_pictures(os.getcwd()))

	# for root, dirs, files in os.walk(os.getcwd()):
	# 	files.sort()
	# 	print(files)
	# 	break

	# for root, dirs, files in os.walk("."):
	# 	for name in files:
	# 		print(os.path.join(root, name))
	# 	for name in dirs:
	# 		print(os.path.join(root, name))

	# config = configparser.ConfigParser()
	# config['DEFAULT'] = {'STUFF': 1, 'THING': 2, 'BLEH': 3}

	# with open('init.ini', 'w') as configfile:
	# 	config.write(configfile)



if __name__ == "__main__":
    main()