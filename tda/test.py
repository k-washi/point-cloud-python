import open3d as o3d
import numpy as np

"""
data
https://free3d.com/ja/3d-models/obj

https://www.thekerneltrip.com/statistics/topological-data-analysis-tutorial/
"""

def obj_mesh(path):
  return o3d.io.read_triangle_mesh(path)

def draw_mesh(mesh):
  
  mesh.paint_uniform_color([1., 0., 0.])
  mesh.compute_vertex_normals()
  o3d.visualization.draw_geometries([mesh])

def mesh2ply(mesh):
  pcd = o3d.geometry.PointCloud()
  pcd.points = o3d.utility.Vector3dVector(np.asarray(mesh.vertices))
  return pcd

def display_inlier_outlier(cloud, ind):
    inlier_cloud = cloud.select_down_sample(ind)
    outlier_cloud = cloud.select_down_sample(ind, invert=True)

    print("Showing outliers (red) and inliers (gray): ")
    outlier_cloud.paint_uniform_color([1, 0, 0])
    inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])

if __name__ == "__main__":
  path = "/Users/washizakikai/data/obj3d/IronMan.obj"
  mesh = obj_mesh(path)
  #draw_mesh(mesh)


  #print(mesh)
  #print(np.asarray(mesh.vertices))

  pcd = mesh2ply(mesh)
  downpcd = pcd.voxel_down_sample(voxel_size=0.02)
  #o3d.visualization.draw_geometries([downpcd])
  #cl, ind = downpcd.remove_statistical_outlier(nb_neighbors=20,
  #                                                    std_ratio=2.0)
  #display_inlier_outlier(downpcd, ind)

  




