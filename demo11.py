import pandas as pd
from numpy.ma.core import inner

student = pd.DataFrame({
    '学号': [202301, 202302, 202303, 202304],
    '姓名': ['张三', '李四', '王五', '赵六'],
    '专业': ['计算机', '会计', '机械', '英语']
})

score = pd.DataFrame({
    '学生学号': [202301, 202302, 202305, 202306],
    '课程名': ['Python', '高数', 'Python', '英语'],
    '分数': [88, 92, 79, 85]
})

print('以学号为链接键，使用merge内连接:\n',pd.merge(student,score,how='inner',left_on='学号',right_on='学生学号'))
print('以学号为链接键，使用merge左连接:\n',pd.merge(student,score,how='left',left_on='学号',right_on='学生学号'))
# print('将score表学生学号重命名为学号，使用join方法左连接:\n',pd.DataFrame.join(student,score,on='学号',how='left',rsuffix='1'))
