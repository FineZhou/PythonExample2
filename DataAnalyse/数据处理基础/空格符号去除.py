import pandas

if __name__ == '__main__':
    df=pandas.read_excel("you_kongge_data.xlsx")
    print("去空之前的数据：")
    print("="*50)
    print(df)
    diqu=df["地区"].str.strip()
    df["地区"]=diqu

    print("="*50)
    print("去空之后的数据")
    print(df)