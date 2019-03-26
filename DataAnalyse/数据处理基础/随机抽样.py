import pandas
import numpy

if __name__ == '__main__':
    ran=numpy.random.randint(0,10,3)
    print(ran)
    df=pandas.read_excel("suiji_chouqu_data.xlsx")

    cols=df.loc[ran, :]
    print(cols)