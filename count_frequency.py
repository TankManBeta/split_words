# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/3/27 15:10
"""
import jieba
import xlwt


def get_content(file_path, file_name):
    with open(file_path+file_name, 'r', encoding="utf-8") as f:
        data = f.read()
        return data


def get_stopwords(file_path, file_name):
    stopwords = []
    with open(file_path+file_name, encoding="utf-8") as f:
        content = f.readlines()
        for line in content:
            stopwords.append(line.strip())
    return stopwords


def save_result(file_path, file_name, save_data):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet(u'sheet1',cell_overwrite_ok=True)
    title = ["序号", "频次", "关键词"]
    for i in range(len(title)):
        sheet.write(0, i, title[i])
    for index, value in enumerate(save_data):
        sheet.write(index+1, 0, index+1)
        sheet.write(index+1, 1, value[1])
        sheet.write(index+1, 2, value[0])
    wb.save(file_path+file_name)


if __name__ == "__main__":
    text = get_content("data/", "result.txt")
    # res_list = jieba.cut(text, cut_all=True)
    res_list = jieba.cut(text, cut_all=False)
    # res_list = jieba.cut_for_search(text)
    stopwords_list = get_stopwords("data/", "stopwords.txt")
    cnt_dict = {}
    for res in res_list:
        if res not in stopwords_list:
            cnt_dict[res] = cnt_dict.get(res, 0)+1
    items = list(cnt_dict.items())
    items.sort(key=lambda x: x[1], reverse=True)
    items = items[:20]
    save_result("result/", u"结果.xlsx", items)