import  pandas

if __name__ == '__main__':
    df=pandas.read_excel("you_chouqu_dianhua_data.xlsx")
    photos=df["联系电话"].astype(str)
    print(df)
    yunying=photos.str.slice(0,3)
    quyu=photos.str.slice(3,7)
    haoma=photos.str.slice(7,11)
    print("运营商：",yunying)
    print("区域：",quyu)
    print("号码段:",haoma)