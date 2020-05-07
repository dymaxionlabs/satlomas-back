#!/bin/bash
set -xeu -o pipefail

uploads_dir=media
rasters_dir=$uploads_dir/rasters
tiles_dir=$uploads_dir/tiles

## VI
function vi_ndvi {
	for p in $(ls $rasters_dir/ndvi/); do
		src=$rasters_dir/ndvi/$p/ndvi.tif
		dst=$tiles_dir/ndvi/$p/
		script/gdal2tilesp.py -e -w leaflet -n -z 6-13 $(pwd)/$src $(pwd)/$dst
	done
}

function vi_vegetation {
	for p in $(ls $rasters_dir/vegetation/); do
		src=$rasters_dir/vegetation/$p/vegetation.tif
		dst=$tiles_dir/vegetation/$p/
		script/gdal2tilesp.py -e -w leaflet -n -z 6-13 $(pwd)/$src $(pwd)/$dst
	done
}

function vi_cloud {
	for p in $(ls $rasters_dir/cloud/); do
		src=$rasters_dir/cloud/$p/cloud.tif
		dst=$tiles_dir/cloud/$p/
		script/gdal2tilesp.py -e -w leaflet -n -z 6-13 $(pwd)/$src $(pwd)/$dst
	done
}

## Lomas

# S2 RGB
function s2 {
	for p in $(ls $rasters_dir/s2/); do
		src=$rasters_dir/s2/$p/s2.tif
		dst=$tiles_dir/s2/$p/
		script/gdal2tilesp.py -e -w leaflet -n -z 6-14 $(pwd)/$src $(pwd)/$dst
	done
}

# S1 RGB
function s1 {
	for p in $(ls $rasters_dir/s1/); do
		src=$rasters_dir/s1/$p/s1.tif
		dst=$tiles_dir/s1/$p/
		script/gdal2tilesp.py -e -w leaflet -n -z 6-14 $(pwd)/$src $(pwd)/$dst
	done
}

# Lomas mask
function loss {
	for p in $(ls $rasters_dir/loss/); do
		src=$rasters_dir/loss/$p/loss.tif
		dst=$tiles_dir/loss/$p/
		script/gdal2tilesp.py -e -w leaflet -n -z 6-14 $(pwd)/$src $(pwd)/$dst
	done
}

#s2
#s1
loss