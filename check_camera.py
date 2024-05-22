import os
import glob
import matplotlib as plt
from camera_pose_visualizer import CameraPoseVisualizer
# import torch
# from einops import rearrange
import numpy as np


def plot_framewise():
    ''' read your data '''
    # data_path = 'load_path'
    # data = torch.load(data_path)
    
    ''' read extrinsic matrix from your file '''
    # c2w = rearrange(data[0]["cameras"][:,4:], "b (h w) -> b h w", h=4, w=4)

    # conversion_1 = torch.zeros((4, 4), dtype=torch.float32)
    # conversion_1[0, 2] = 1
    # conversion_1[1, 1] = 1
    # conversion_1[2, 0] = 1
    # conversion_1[3, 3] = 1
    
    # c2w = c2w@conversion_1
    
    # conversion_2 = torch.zeros((4, 4), dtype=torch.float32)
    # conversion_2[0, 0] = 1
    # conversion_2[1, 2] = 1
    # conversion_2[2, 1] = 1
    # conversion_2[3, 3] = 1
    
    # c2w = c2w@conversion_2
    
    visualizer = CameraPoseVisualizer([-50, 50], [-50, 50], [-50, 50])
  
    
    for index in range(c2w.shape[0]):
        if index % 50 == 0:
            visualizer.extrinsic2pyramid(np.array(c2w[index]), 'c', 10)
            
    visualizer.show()
    
if __name__ == "__main__":
    plot_framewise()