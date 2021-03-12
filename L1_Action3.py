import pandas as pd
df=pd.read_csv('car_complain.csv')

#problem列数据拆分
df=df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))

#brand数据清理
def f(x):
    x=x.replace('一汽-大众','一汽大众')
    return x
df['brand']=df['brand'].apply(f)

tags = df.columns[7:]

#计算每个车型总投诉数量
result1=df.groupby(['brand','car_model'])[tags].agg(['sum'])
result1['车型总投诉数']=result1.sum(axis=1)
result1=result1['车型总投诉数']

#计算每个品牌车型数量
result2=result1.groupby(['brand']).agg(['count'])
result2['车型数']=result2['count']
result2=result2['车型数']

#计算每个品牌总投诉量
result3=result1.groupby(['brand']).agg(['sum'])
result3['品牌总投诉数']=result3['sum']
result3=result3['品牌总投诉数']

#打印各车型投诉量并排序
result1=result1.reset_index()
result1=result1.fillna('ffill')
result1=result1.sort_values(by='车型总投诉数',ascending=False)
print('各车型投诉情况：')
print(result1)

#打印各品牌平均车型投诉并排序
result=pd.merge(result2,result3,left_index=True,right_index=True,how='left')
result['平均车型投诉']=result['品牌总投诉数']/result['车型数']
result['平均车型投诉']=result['平均车型投诉'].round(2)
result=result.sort_values('平均车型投诉',ascending=False)
print('各品牌平均车型投诉情况：')
print(result)