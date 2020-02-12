import open3d as o3d
import numpy as np

TestdataPath = "/Users/washizakikai/DevLocal/git/other/Open3D/examples/TestData"

def ex_import_func():
  pcd = o3d.io.read_point_cloud(TestdataPath + "/ICP/cloud_bin_0.pcd")
  print("Point Cloud: ", pcd)
  o3d.io.write_point_cloud("./data/cCloudBin0.pcd", pcd)

  mesh = o3d.io.read_triangle_mesh(TestdataPath + "/knot.ply")
  print("Mesh:", mesh)
  o3d.io.write_triangle_mesh("./data/cKnot.ply", mesh)

def ex_pc_operation():
  pcd = o3d.io.read_point_cloud(TestdataPath + "/fragment.ply")
  print(pcd)
  print(np.asarray(pcd.points)[:10])
  #o3d.visualization.draw_geometries([pcd])

  print("ダウンサンプリング")
  downpcd = pcd.voxel_down_sample(voxel_size=0.05)
  #o3d.visualization.draw_geometries([downpcd])

  print("ダウンサンプリング後のポイントクラウドの直交推定")
  downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(
        radius=0.1, max_nn=30))
  #o3d.visualization.draw_geometries([downpcd])

  print("0th ポイント　直交ベクトル")
  print(downpcd.normals[0])
  print("最初の10個の直交ベクトル")
  print(np.asarray(downpcd.normals)[:10, :])
  print("")

  print("椅子のポリゴン取得")
  vol = o3d.visualization.read_selection_polygon_volume(
      TestdataPath + "/Crop/cropped.json")
  chair = vol.crop_point_cloud(pcd)
  #o3d.visualization.draw_geometries([chair])
  print("")

  print("色の変更")
  chair.paint_uniform_color([1, 0.706, 0])
  o3d.visualization.draw_geometries([chair])
  print("")


if __name__ == "__main__":
  #ex_import_func()
  ex_pc_operation()