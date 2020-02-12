# point-cloud-python
open3D and topology data analysis 

# Setup

```bash
conda create -n o3d python=3.6
conda activate o3d
conda install -c open3d-admin open3d==0.8
```

open3dの最新バージョンはMacOsX 10.13, 10.14でコンパイルエラーが見つかっている。
+ [Open3D 0.9 installed using pip does not work in OSX 10.14 ](https://github.com/intel-isl/Open3D/issues/1421)

# test data

test data is include git of [open3D](https://github.com/intel-isl/Open3D/tree/v0.7.0).


# reference

@article{Zhou2018,
    author    = {Qian-Yi Zhou and Jaesik Park and Vladlen Koltun},
    title     = {{Open3D}: {A} Modern Library for {3D} Data Processing},
    journal   = {arXiv:1801.09847},
    year      = {2018},
}

