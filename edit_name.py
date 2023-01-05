from glob import glob
import argparse



def get_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--inp_path'. type='str',default='./')

	args = parser.parse_args()
	return args


if __name__ == '__main__':
	args = get_parser()
	inp_path = args.inp_path


    img_files = glob(inp_path+"/*")

    for file in img_files:
    	name = file.split('/')[-1].split('.')[0].split()