import pandas

if __name__ == '__main__':

    df=pandas.read_excel("queshizhi_data.xlsx")
    print(df)
    df=df.dropna()
    print("*"*50)
    print(df)