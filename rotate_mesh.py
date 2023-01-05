from glob import glob
import argparse
import shutil
import os
import pymeshlab

def get_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--inp_path', type=str,default='./')


	args = parser.parse_args()
	return args


if __name__ == '__main__':
	args = get_parser()
	inp_path = args.inp_path


	fold_list = glob(inp_path+"/*")
 

	for folder in fold_list: 
		mesh_files = glob(folder+'/*.obj') 
		for mesh_file in mesh_files: 
			mesh = pymeshlab.MeshSet()
			mesh.load_new_mesh(mesh_file)

			mesh.transform_rotate(rotaxis=1,angle=100)

			mesh.save_current_mesh(mesh_file)
			mesh.clear()
