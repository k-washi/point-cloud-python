import open3d as o3d

TestdataPath = "/Users/washizakikai/DevLocal/git/other/Open3D/examples/TestData"

def ex_import_func():
  pcd = o3d.io.read_point_cloud(TestdataPath + "/ICP/cloud_bin_0.pcd")
  print(pcd)

if __name__ == "__main__":
  ex_import_func()