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

DEFAULT_CHANNELS = (1,2,3,4,5,6,7,8)
RGB_MAP = {
    4: {
        'rgb': np.array([255,0,0]),
        'range': [0, 255]
    },
    1: {
        'rgb': np.array([0,255,0]),
        'range': [0, 150]
    },
    3: {
        'rgb': np.array([0,0,255]),
        'range': [0, 255]
    },
    6: {
        'rgb': np.array([102,205,170]),
        'range': [0, 255]
    },
    2: {
        'rgb': np.array([253, 164, 0]),
        'range': [0, 255]
    },
    5: {
        'rgb': np.array([75,0,130]),
        'range': [0, 100]
    }
    ,7: {
        'rgb': np.array([255, 21, 240]),
        'range': [0, 255]
    }
    ,8: {
        'rgb': np.array([255, 255, 100]),
        'range': [0, 255]
    }
}

def convert_to_rgb(t, channels=DEFAULT_CHANNELS, vmax=255, rgb_map=RGB_MAP):
    """
    Converts and returns the image data as RGB image
    Parameters
    ----------
    t : np.ndarray
        original image data
    channels : list of int
        channels to include
    vmax : int
        the max value used for scaling
    rgb_map : dict
        the color mapping for each channel
        See rxrx.io.RGB_MAP to see what the defaults are.
    Returns
    -------
    np.ndarray the image data of the site as RGB channels
    """
    dim1,dim2,_ = t.shape
    colored_channels = []
    for i, channel in enumerate(channels):
        x = (t[:, :, channel-1] / vmax) / \
            ((rgb_map[channel]['range'][1] - rgb_map[channel]['range'][0]) / 255) + \
            rgb_map[channel]['range'][0] / 255
        x = np.where(x > 1., 1., x)
        x_rgb = np.array(
            np.outer(x, rgb_map[channel]['rgb']).reshape(dim1,dim2, 3),
            dtype=int)
        colored_channels.append(x_rgb)
    im = np.array(np.array(colored_channels).sum(axis=0), dtype=int)
    im = np.where(im > 255, 255, im)
    im = im.astype(np.uint8)
    return im

def one_channel(t, channel, vmax=255, rgb_map=RGB_MAP):
    """
    Converts and returns the image data as RGB image
    Parameters
    ----------
    t : np.ndarray
        original image data
    channels : list of int
        channels to include
    vmax : int
        the max value used for scaling
    rgb_map : dict
        the color mapping for each channel
        See rxrx.io.RGB_MAP to see what the defaults are.
    Returns
    -------
    np.ndarray the image data of the site as RGB channels
    """
    dim1,dim2,_ = t.shape
    colored_channels = []
    x = (t[:, :, 0] / vmax) / \
        ((rgb_map[channel]['range'][1] - rgb_map[channel]['range'][0]) / 255) + \
        rgb_map[channel]['range'][0] / 255
    x = np.where(x > 1., 1., x)
    x_rgb = np.array(
        np.outer(x, rgb_map[channel]['rgb']).reshape(dim1,dim2, 3),
        dtype=int)
    colored_channels.append(x_rgb)
    im = np.array(np.array(colored_channels).sum(axis=0), dtype=int)
    im = np.where(im > 255, 255, im)
    im = im.astype(np.uint8)
    return im