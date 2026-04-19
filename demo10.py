import pandas as pd

df1 = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [18, 19, 18, 20]
}, index=[0, 1, 2, 3])

df2 = pd.DataFrame({
    '班级': ['一班', '二班', '一班', '二班'],
    '成绩': [90, 85, 95, 88]
}, index=[0, 2, 3, 4])

print('横向内连接:\n',pd.concat([df1,df2],axis=1,join='inner'))
print('横向外连接:\n',pd.concat([df1,df2],axis=1,join='outer'))

