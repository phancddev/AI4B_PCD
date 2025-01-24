import pandas as pd

df = pd.read_csv('student_scores.csv')

math_mean = df['Math'].mean()
above_average_math = df[df['Math'] > math_mean]
print("Học sinh có điểm Toán trên trung bình:")
print(above_average_math)

df['Average_Score'] = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean(axis=1)
df['Status'] = df['Average_Score'].apply(lambda x: 'Pass' if x > 60 else 'Fail')

df.to_csv('student_scores_processed.csv', index=False)


