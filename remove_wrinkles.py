from pickle import FALSE
import numpy as np
import trimesh
import pymeshlab
import argparse
import os
from glob import glob



def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mesh_path', type=str, default='THUmans2.0/garments/topwear_front_back/')
    parser.add_argument('--output_path', type=str, default='THUmans2.0/garments/without_wrinkles_topwear/')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_parser() 
    mesh_path = args.mesh_path
    output_path = args.output_path
    os.makedirs(output_path,exist_ok=True)

    names = []
    meshes = glob(mesh_path+"/*")
    for file in meshes: 
        name = file.split('/')[-1].split('.')[0].split('_')[0]
        names.append(name)
        # breakpoint()


        mesh = pymeshlab.MeshSet()
        mesh_path = os.path.join(file) 
        mesh.load_new_mesh(file)        
        mesh.apply_coord_two_steps_smoothing(stepsmoothnum=3)
        mesh.apply_coord_laplacian_smoothing(stepsmoothnum=3,cotangentweight=False)
        mesh.meshing_repair_non_manifold_edges()
        

        output_file = os.path.join(output_path,name+'.obj')
        mesh.save_current_mesh(output_file )

        mesh.clear()