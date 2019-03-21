import pandas

if __name__ == '__main__':
    data = pandas.read_table("data.txt", names=["序号", "日期", "购买用户数", "广告费", "渠道数"], sep=",", encoding="utf-8")
    print(data)
