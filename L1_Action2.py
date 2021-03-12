from pandas import Series, DataFrame
#建立数据表
data = {'Chinese': [68, 95, 98, 90,80], 'Math': [65, 76, 86, 88, 90], 'English': [30, 98, 88, 77, 90]}
df = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])
print(df.describe())