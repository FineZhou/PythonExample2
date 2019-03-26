import  pandas

if __name__ == '__main__':
    df = pandas.read_excel("you_chouqu_dianhua_data.xlsx")
    newDf=df["商品"].str.split(' ',1,True)
    newDf.columns=["商品1","商品2"]
    print("拆分前原数据："+"=="*50)
    print(df)
    print("拆分后数据："+("=="*50))
    print(newDf)