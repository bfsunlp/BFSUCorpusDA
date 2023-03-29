# -*- coding:utf-8 -*-
"""
Copyright (c) 2022-2023, LIU Dingjia, BFSUNLP Group.
All rights reserved.
Email:
dingjialiu@gmail.com
bfsunlp@gmail.com
"""
# python main.py process_dir -source D:\demo -target D:\Output -regex "\<.*?\>" -replace "" -flag i


import re
import sys
import source.text_proc as tp

if __name__ == "__main__":
    if sys.argv[1] == "process_dir":
        func = tp.process_dir
        source_path = sys.argv[3]
        target_path = sys.argv[5]
        replace = sys.argv[9]
        regex = sys.argv[7]
        flag = sys.argv[11]
        func(source_dir=source_path,
             target_dir=target_path,
             replace=replace,
             regex=regex,
             flag=flag)

    """if sys.argv[] == "--onefile":
        lang = sys.argv[3][2:]
        job = sys.argv[2][2:]
        input_path = sys.argv[5]
        output_path = sys.argv[7]
        if lang == "zh":
            cla.process_file(input_path=input_path,
                             output_path=output_path,
                             job=job,
                             mode="single",
                             pipeline=None)
            print("Job is accomplished! Please check:\n" + output_path)
    elif sys.argv[1] == "--dir":
        lang = sys.argv[3][2:]
        job = sys.argv[2][2:]
        # print(job)
        input_path = sys.argv[5]
        output_path = sys.argv[7]
        if lang == "zh":
            cla.process_dir(input_path=input_path,
                            output_path=output_path,
                            job=job)
    else:
        raise ValueError(sys.argv[1] + " can not be recognized!")"""
