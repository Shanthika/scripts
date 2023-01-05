import numpy as np 
import argparse
import cv2
from glob import glob
from PIL import Image
import os
import matplotlib.pyplot as plt
import pdb


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inp_path', type=str, default='./')



    args = parser.parse_args()
    return args



if __name__ == '__main__':
    args = get_parser()

    inp_path = args.inp_path


    img_files = glob(inp_path+"/*")
    # pdb.set_trace()

    for file in img_files:
    	name = file.split('/')[-1].split('.')[0]
    	img = Image.open(file)
    	img = np.array(img)
    	mask = img[..., -1]
    	mask = Image.fromarray(mask)

    	out_path = os.path.join(inp_path, name+"_mask.png")
    	mask.save(out_path)


