import pandas as pd
import numpy as np

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [18, 19, 20, 21],
    'Marks': [80, None, 90, None]
}

dataFrame = pd.DataFrame(data)

ndArrayData = dataFrame.to_numpy()
print("Dữ liệu dưới dạng ndarray:")
print(ndArrayData)

rotatedArray = np.rot90(ndArrayData, k=-1)
print("\nMa trận sau khi xoay 90 độ:")
print(rotatedArray)

maxAge = dataFrame['Age'].max()
oldestPerson = dataFrame.loc[dataFrame['Age'] == maxAge, 'Name'].iloc[0]
print("\nTên của người lớn tuổi nhất:", oldestPerson)
