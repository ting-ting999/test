import pandas as pd

# 读取CSV文件
df = pd.read_csv('data3.csv')

# 查看数据的基本信息，包括缺失值情况
print(df.info())

# 只对数值列计算均值
numeric_columns = df.select_dtypes(include=['number'])

# 使用数值列的均值填充缺失值
df[numeric_columns.columns] = numeric_columns.fillna(numeric_columns.mean())

# 查看补充缺失值后前五行的数据
print(df.head())

# 保存补充缺失值后的数据到新的CSV文件
df[numeric_columns.columns].to_csv('data3_filled.csv', index=False)