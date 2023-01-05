import numpy as np
import trimesh


def get_rot_mat(angle):
    rot_mat = [[np.cos(angle),0,np.sin(angle)],[0,1,0],[-np.sin(angle),0, np.cos(angle)]]
    return rot_mat


if __name__ == '__main__':
    bunny_mesh = trimesh.load("bunny.obj",process=False, maintain_order=True)
    bunny = bunny_mesh.vertices

    rot_angle = 320

    R_mat = get_rot_mat(rot_angle)
    rot_bunny = np.matmul(R_mat,bunny.T).T 