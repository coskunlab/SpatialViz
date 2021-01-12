import os
import cv2
import numpy as np 
from pathlib import Path
import skimage.io
from skimage import img_as_ubyte
from skimage.transform import rescale


def read_img(ROI: str, data_dir):
    """Read all image from one ROI"""
    dir_ = data_dir / ROI

    # Get images in directory
    dirpath, _, filenames = next(os.walk(dir_))
    img_name = [
        name
        for name in sorted(filenames)
        if "tiff" in name
    ]
    markers = [name.split("_")[-1].split(".")[0] for name in img_name]
    imgs = np.stack(
        [img_as_ubyte(skimage.io.imread(os.path.join(dirpath, name), True)) for name in img_name], axis=0
    )
    return imgs, markers

def create_folder(name, parent_dir):
    '''Create folder based on name and parent_dir path'''
    path_folder = parent_dir / name
    try:
        path_folder.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("Folder is already there")
    else:
        print("Folder was created")
    return path_folder