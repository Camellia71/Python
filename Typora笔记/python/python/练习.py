import numpy as np

# 创建一个示例掩码数组
npmask = np.array([
    [1, 2, 1],
    [4, 1, 2],
    [2, 4, 1]
])

# 生成二值掩码
Label_1 = npmask.copy()
Label_1[npmask == 1] = 1.
Label_1[npmask == 2] = 0.
Label_1[npmask == 4] = 0.

Label_2 = npmask.copy()
Label_2[npmask == 1] = 0.
Label_2[npmask == 2] = 1.
Label_2[npmask == 4] = 0.

Label_4 = npmask.copy()
Label_4[npmask == 1] = 0.
Label_4[npmask == 2] = 0.
Label_4[npmask == 4] = 1.

# 打印结果
print("Original Mask:\n", npmask)
print("Label_1:\n", Label_1)
print("Label_2:\n", Label_2)
print("Label_4:\n", Label_4)