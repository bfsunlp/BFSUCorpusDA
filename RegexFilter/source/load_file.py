# -*- coding:utf-8 -*-
"""
Copyright (c) 2022-2023, LIU Dingjia, BFSU NLP Team, BFSU Corpus Research Group.
All rights reserved.
Email:
bfsunlp@gmail.com
dingjialiu@gmail.com
"""

import os
import codecs
import chardet


def load_dir_files(dir_path):
    file_names = os.listdir(dir_path)
    file_paths = [os.path.join(dir_path, each_name) for each_name in file_names
                  if os.path.isfile(os.path.join(dir_path, each_name))]
    return file_paths


def detect_encode(file_path):
    try:
        with codecs.open(file_path, "r", "utf-8") as file_obj:
            file_obj.read()
        return "utf-8"
    except UnicodeDecodeError:
        with open(file_path, "rb") as file_obj:
            data = file_obj.read()
            result = chardet.detect(data)["encoding"]
        return result


if __name__ == "__main__":
    pass


