import trimesh
import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inp_path', type=str,default='./')


    args = parser.parse_args()
    return args
  

if __name__ == '__main__':
    args = get_parser()
    verts,faces,uvs,vertex_col = args.inp_path

        
    mesh = trimesh.Trimesh(verts,faces,vertex_colors=vertex_col,preprocess=False, maintain_order=True)
    tex = TextureVisuals(uv=uvs)
    mesh.visual = tex
