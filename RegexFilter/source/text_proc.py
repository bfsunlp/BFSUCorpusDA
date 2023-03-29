# -*- coding:utf-8 -*-
"""
Copyright (c) 2022-2023, LIU Dingjia, BFSUNLP Group.
All rights reserved.
Email:
dingjialiu@gmail.com
bfsunlp@gmail.com
"""

import os
import codecs
import source.load_file as lf
import re


def match_and_replace(regex=None, string=None, replace=None, flag=0):
    if flag == "i":
        flag = re.I
    elif flag == "m":
        flag = re.M
    elif flag == "s":
        flag = re.S
    else:
        flag = 0
    pattern = re.compile(regex, flags=flag)
    result = pattern.sub(repl=replace, string=string)
    return result


def process_file(source_path, target_path, replace, regex, flag):
    encoding = lf.detect_encode(source_path)
    with codecs.open(source_path, "r", encoding=encoding) as source_obj:
        with codecs.open(target_path, "w", encoding=encoding) as target_obj:
            while True:
                line = source_obj.readline()
                if line:
                    target_obj.write(match_and_replace(regex=regex, string=line, replace=replace, flag=flag))
                else:
                    break
    return True


def process_dir(source_dir, target_dir, replace, regex, flag):
    source_paths = lf.load_dir_files(source_dir)
    for each_path in source_paths:
        target_path = os.path.join(target_dir, os.path.split(each_path)[-1])
        process_file(source_path=each_path,
                     target_path=target_path,
                     replace=replace,
                     regex=regex,
                     flag=flag)
        print(each_path, "Done!")
    return True


if __name__ == "__main__":
    process_file(source_path=r"D:\Demo\EN_WXEC5L_F0066.txt",
                 target_path=r"d:\output\result.txt",
                 replace="",
                 regex="\<.*?\>",
                 flag="i")
