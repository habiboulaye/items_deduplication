#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Run Unittests of Duplicate class:
        python iducplicate_tests.py
'''

from iduplicate import Duplicate
import os
import unittest

# Paths to images
pth_dpl = os.path.join('..', "images", "duplicate_ads")
pth_ndpl = os.path.join('..', "images", "non_duplicate_ads")

### Change the model to use another pre-trained model (the fc layer): use for features generation
#from keras.applications.resnet_v2 import ResNet50V2
#model = ResNet50V2(weights='imagenet', include_top=False, pooling='avg')

# Intance of Duplicate class
objDPL = Duplicate()

class TestDuplicate(unittest.TestCase):
    """
    Unittests for class Duplicate
    """

    def test_duplicated(self):
        img_path_1 = os.path.join(pth_dpl, "60_1936494496.jpg")
        img_path_2 = os.path.join(pth_dpl, "60_1936494496.jpg")
        self.assertEqual(objDPL.duplication_check(img_path_1, img_path_2), True, "Test should be True (threshold:95)")

    def test_not_duplicated(self):
        img_path_1 = os.path.join(pth_dpl, "59_1918146649.jpg")
        img_path_2 = os.path.join(pth_dpl, "60_1936494496.jpg")
        self.assertEqual(objDPL.duplication_check(img_path_1, img_path_2), False, "Test should be False")

    def test_tbd_duplicated(self):
        img_path_1 = os.path.join(pth_dpl, "29_1742048333.jpg")
        img_path_2 = os.path.join(pth_ndpl, "65_1302116323.jpg")
        self.assertEqual(objDPL.duplication_check(img_path_1, img_path_2, sim_threshold=95), False, "Test should be False (threshold:95)")

    def test_tbd_duplicated(self):
        img_path_1 = os.path.join(pth_dpl, "29_1742048333.jpg")
        img_path_2 = os.path.join(pth_ndpl, "65_1302116323.jpg")
        self.assertEqual(objDPL.duplication_check(img_path_1, img_path_2, sim_threshold=85), True, "Test should be True (threshold:85)")


if __name__ == '__main__':
    unittest.main()
    #unittest.main(argv=['first-arg-is-ignored'], exit=False) #in jupyter