from glob import glob
import argparse
import shutil
import os

def get_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--inp_path', type=str,default='./')
	parser.add_argument('--out_path', type=str,default='./')

	args = parser.parse_args()
	return args


if __name__ == '__main__':
	args = get_parser()
	inp_path = args.inp_path
	out_path = args.out_path

	os.makedirs(os.path.join(out_path,'top'),exist_ok=True)
	os.makedirs(os.path.join(out_path,'bottom'),exist_ok=True)

	fold_list = glob(inp_path+"/*")
 

	for folder in fold_list: 
		top_files = glob(os.path.join(folder,'top','*')) 
		for tp in top_files: 
			shutil.copy(tp, os.path.join(out_path,'top'))


		bottom_files = glob(os.path.join(folder,'bottom','*')) 
		for bp in bottom_files: 
			shutil.copy(bp, os.path.join(out_path,'bottom'))

			