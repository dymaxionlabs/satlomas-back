import os
import subprocess
import zipfile

import numpy as np
import rasterio
from django.contrib.gis.geos import GEOSGeometry
from rasterio.windows import Window
from shapely.geometry import box
from skimage import exposure
from tqdm import tqdm


def run_subprocess(cmd):
    print(cmd)
    subprocess.run(cmd, shell=True, check=True)


def unzip(zip_name, extract_folder=None, delete_zip=True):
    if extract_folder is None:
        extract_folder = os.path.dirname(zip_name)
    resultzip = zipfile.ZipFile(zip_name)
    resultzip.extractall(extract_folder)
    resultzip.close()
    if delete_zip:
        os.remove(zip_name)


def sliding_windows(size, width, height):
    """Slide a window of +size+ pixels"""
    for i in range(0, height, size):
        for j in range(0, width, size):
            yield Window(j, i, min(width - j, size), min(height - i, size))


def write_rgb_raster(bands=[], *, src_path, dst_path, in_range):
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with rasterio.open(src_path) as src:
        profile = src.profile.copy()
        profile.update(count=3,
                       dtype=np.uint8,
                       compress='deflate',
                       tiled=True,
                       nodata=0)
        height, width = src.shape[0], src.shape[1]
        if not bands:
            bands = range(1, src.count + 1)
        with rasterio.open(dst_path, 'w', **profile) as dst:
            windows = list(sliding_windows(1000, width, height))
            for window in tqdm(windows):
                img = np.dstack([src.read(b, window=window) for b in bands])
                new_img = np.dstack([
                    exposure.rescale_intensity(img[:, :, i],
                                               in_range=in_range[i],
                                               out_range=(1, 255)).astype(
                                                   np.uint8)
                    for i in range(img.shape[2])
                ])
                for i in range(3):
                    dst.write(new_img[:, :, i], i + 1, window=window)


def get_raster_extent(path):
    with rasterio.open(path) as src:
        return GEOSGeometry(box(*src.bounds).wkt)
