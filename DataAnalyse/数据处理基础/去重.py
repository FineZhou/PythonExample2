import pandas

if __name__ == '__main__':
    df=pandas.read_excel("you_chongfu_data.xlsx")
    print("去重之前总数：",df.count())
    df=df.drop_duplicates()
    print("去重之后的总数",df.count())


