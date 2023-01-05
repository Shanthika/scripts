import numpy as np 
import trimesh
import os



def show(verts = None, faces = None, colors = None):     
    if torch.is_tensor(verts):         
        verts = verts.detach().numpy()     
        
    if torch.is_tensor(faces):         
        faces = faces.detach().numpy()     
        
    all_meshes = []     
    if faces is not None:         
        for i in range(len(verts)):            
            m = trimesh.Trimesh(verts[i], faces[i])             
            if colors is not None:                 
                m.visual.vertex_colors = colors[i]            
            all_meshes.append(m)     
        
    else:         
        for i in range(len(verts)):             
            m = trimesh.PointCloud(verts[i])             
            all_meshes.append(m)     
                    
    scene = trimesh.scene.Scene()    
    for m in all_meshes:        
        scene.add_geometry(m)     
    scene.show('gl')