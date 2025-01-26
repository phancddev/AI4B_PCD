import numpy as np

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

tensor1 = np.array(matrix1)
tensor2 = np.array(matrix2)

add_result = tensor1 + tensor2
sub_result = tensor1 - tensor2
mul_result = tensor1 * tensor2
div_result = tensor1 / tensor2

matmul_result = np.dot(tensor1, tensor2)

transpose1 = np.transpose(tensor1)
transpose2 = np.transpose(tensor2)

print("a) Tensor 1:\n", tensor1)
print("   Tensor 2:\n", tensor2)

print("\nb) Cộng:\n", add_result)
print("   Trừ:\n", sub_result)
print("   Nhân:\n", mul_result)
print("   Chia:\n", div_result)

print("\nc) Phép nhân ma trận:\n", matmul_result)

print("\nd) Ma trận chuyển vị của ma trận 1:\n", transpose1)
print("   Ma trận chuyển vị của ma trận 2:\n", transpose2)