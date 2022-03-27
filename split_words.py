# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2020/9/22 10:13
"""


# 该函数从data.conll文件中提取出data.dict并输出到文件中
def get_dict(file_path):
    content_dict = []
    with open(file_path, "r", encoding="UTF-8") as f:
        line = f.readline()
        while line:
            line_list = line.split()
            if len(line_list) >= 2:
                content_dict.append(line_list[1])
            line = f.readline()
    f_out = open("data/data.dict", "w", encoding="UTF-8")
    for item in content_dict:
        f_out.write(item + '\n')
    f_out.close()
    return content_dict


# 该函数将data.conll中的文件修改文本格式
def get_text(temp_list):
    out_text = "".join(temp_list)
    return out_text


# 该函数进行前向最大匹配分词
def split_words(standard_list, text, maxsize):
    start = 0
    temp_length = maxsize
    end = len(text)
    result = []
    while start < end:
        if start == end - 1:
            result.append(text[start])
            break
        if (start + temp_length - 1) < end:
            if text[start:start + temp_length] in standard_list:
                result.append(text[start:start + temp_length])
                start += temp_length
                temp_length = maxsize
            else:
                temp_length -= 1
                if temp_length == 1:
                    result.append(text[start])
                    start += temp_length
                    temp_length = maxsize
        else:
            temp_length -= 1
    return result


if __name__ == "__main__":
    data_dict = get_dict("data/data.conll")
    data_txt = get_text(data_dict)
    print("==分词中，请稍候==")
    results = split_words(data_dict, data_txt, 4)
    print("标准字典为:", data_dict)
    print("分词结果为:", results)
    # 该部分用于计算与评价
    print("==计算评价值中，请稍候==")
    count_right = 0
    for i in results:
        if i in data_dict:
            count_right += 1
    precision = count_right / len(results)
    recall = count_right / len(data_dict)
    f_value = precision * recall * 2 / (precision + recall)
    print("正确率为：", precision, "召回率为：", recall, "F值为:", f_value)