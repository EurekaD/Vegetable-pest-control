import pandas as pd
import string
df = pd.read_csv("蔬菜病虫害.csv")

counts = df.shape[0]

def query(vegetablesKind_, faq_):
    '''by vegetablesKind and faq  query method '''
    for i in range(counts):
        if df.VegetablesKind[i] == vegetablesKind_ and df.FAQ[i] == faq_:
            return df.Method[i]
    return '未找到'

if __name__ == '__main__':
    veg = input("请输入蔬菜名:")
    faq = input("请输入病虫害名:")
    print("防治方法:")
    print(query(veg, faq))
# print(query('青菜', '大大虫'))
# print(query('青菜', '蚜虫'))