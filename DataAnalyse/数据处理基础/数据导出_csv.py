import  pandas

if __name__ == '__main__':
    df=pandas.read_excel("data1.xlsx")
    myexcel=df.to_excel("toExcel.xlsx")
    mycsv=df.to_csv("toCsv.csv",sep=",",header=1,index=True)
    mytxt=df.to_json("tojson.json")
