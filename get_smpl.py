from glob import glob
import argparse
import shutil
import os

def get_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--inp_path', type=str,default='./mesh_data')
	parser.add_argument('--out_path', type=str,default='./smpls')

	args = parser.parse_args()
	return args


if __name__ == '__main__':
	args = get_parser()
	inp_path = args.inp_path
	out_path = args.out_path
 

	fold_list = glob(inp_path+"/*")
 

	for folder in fold_list:  
		name = folder.split('/')[-1]
		smpl_path = os.path.join(folder,'smpl','smpl_mesh.obj')
		output_smpl_path = os.path.join(out_path,f'{name}_smpl.obj')
		shutil.copy(smpl_path, output_smpl_path)
		
			