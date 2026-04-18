import pandas as pd
data = {
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New York','Los Angeles','Chicago']
}
df = pd.DataFrame(data)
print('原始 DataFrame:')
print(df)

# new_df=df.drop(labels=1,axis=0)
# print(new_df)
#
# new_df_2=df.drop(index=2)
# print(new_df_2)

df['Gender']='Unknown'
print('添加新列Gender并标量Unknown后为')
print(df)

salary_list=[5000,6000,7000]
df['Salary']=salary_list
print('添加新列Salary后为')
print(df)