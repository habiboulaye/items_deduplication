#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    run_deduplication.py

    python run_deduplication.py path/2/image_1 path/2/image_2

"""

import argparse
from iduplicate import Duplicate

## Change the model to use another pre-trained model (the fc layer): use for features generation
# model = ResNet50(weights='imagenet', include_top=False, pooling='avg')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_1', help="input item (image 1)")
    parser.add_argument('image_2', help="input item (image 2)")
    args = parser.parse_args()

    #Instanciate the Duplicate class with the default ResNet model
    objDpl = Duplicate()

    # Compute the duplicate score
    print(objDpl.duplication_score(args.image_1, args.image_2))
