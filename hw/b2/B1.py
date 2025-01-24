import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [18, 19, 20, 21],
    'Marks': [80, None, 90, None]
}

df = pd.DataFrame(data)

averageAge = df['Age'].mean()
print("Độ tuổi trung bình:", averageAge)

df = df.drop(columns=['Age'])
print("\nDataFrame sau khi xóa cột 'Age':")
print(df)

averageMarks = df['Marks'].mean()
df['Marks'] = df['Marks'].fillna(averageMarks)
print("\nDataFrame sau khi điền điểm trung bình vào các ô thiếu:")
print(df)
