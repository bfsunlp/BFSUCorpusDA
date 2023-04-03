"""
Copyright (c) 2022-2023, LIN Miaoru, BFSUNLP Group.
Email: linmiaoru@bfsu.edu.cn; bfsunlp@gmail.com
"""

from pyhanlp import HanLP as hlp

def BFSU_Chinese_MATTR_bytxt(filename, window_size):
    """
    :param filename:  传入的txt名字
    :param window_size:  所需的窗口大小
    :return: 一段中文文本的MATTR值,结果保留txt
    """
    # 获取全部文本
    file = open(filename, encoding='utf-8')
    all_line = file.readlines()
    all_line = [i.strip() for i in all_line]
    text = ''.join(all_line)
    file.close()

    # 使用HanLP包进行分词
    word_list = hlp.segment(text.strip())
    all_word = []
    # 获得所有内容列表，并删除标点符号
    for i in range(len(word_list)):
        if str(word_list[i]).split('/')[0] not in ['，', '、', '\n', '\t', '。', '！', '（', '）', '；', '：', '？']:
            all_word.append(str(word_list[i]).split('/')[0])

    # 进行每固定窗口的计算
    res_list = []

    for i in range(1, len(all_word) - (window_size - 1)):
        count_set = set()
        do_list = all_word[i - 1:i + (window_size - 1)]
        for each in do_list:
            count_set.add(each)
        res_list.append(len(count_set) / window_size)

    # 计算数值
    res = sum(res_list) / len(res_list)
    save_name = 'MATTR' + filename
    save_f = open(save_name, 'w')
    save_f.write(str(res))


if __name__ == '__main__':
    # test更改为具体文件名
    BFSU_Chinese_MATTR_bytxt('test.txt', 1000)


