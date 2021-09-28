# -*- coding: utf-8 -*-
# @Author  : sean
# @File    : bdd_helper.py
import os.path
from utils.constant import Constant


class BddHelper(object):

    @staticmethod
    def get_feature_path(path):
        feature_path = Constant.FEATURE_DIR
        return os.path.join(feature_path, path)
