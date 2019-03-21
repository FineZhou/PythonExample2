import pandas

if __name__ == '__main__':
    # 默认第一行为文件的列名
    doc = pandas.read_excel("data1.xlsx", sheet_name="data", names=["a", "b", "c", "d"],
                            header=2)
    print(doc)
