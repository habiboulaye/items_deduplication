#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    run_deduplication.py

    python run_deduplication.py ../images/duplicate_ads ../images/non_duplicate_ads --thres=85

"""
import os
import argparse
from iduplicate import Duplicate

## Change the model to use another pre-trained model (the fc layer): use for features generation
# model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

objDpl = Duplicate()


def detect_duplicated_items(items_dir1, items_dir2, sim_threshold):
    """
    Detect duplicated items (images)

    :param items_dir1: path 1 -> eg. new images path (eg. to check with references)
    :param items_dir2: path 2 -> existing images path (eg. already published in the bon coin)
    :param sim_threshold:
    :return:
    """
    # Get the list of images' names in both directories
    list_ads_1 = [f for f in os.listdir(items_dir1) if os.path.isfile(os.path.join(items_dir1, f))]
    list_ads_2 = [f for f in os.listdir(items_dir2) if os.path.isfile(os.path.join(items_dir2, f))]
    # Loop on images and check duplicate
    for img1 in list_ads_1:
        img1_path = os.path.join(items_dir1, img1)
        for img2 in list_ads_2:
            img2_path = os.path.join(items_dir2, img2)
            if objDpl.duplication_check(img1_path, img2_path, sim_threshold):
                print("  >> duplicated items:", img1, img2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('new_images_dir', help="new images in the marketplace (to check if already exist )")
    parser.add_argument('ref_images_dir', help="ref images in the marketplace (already validated)")
    parser.add_argument('--threshold', action="store",dest="thresh", default=95, type=int, help="threshold on similarity score")
    args = parser.parse_args()
    # detect all duplicated items new vs. ref images
    detect_duplicated_items(args.new_images_dir, args.ref_images_dir, sim_threshold=args.thresh)

