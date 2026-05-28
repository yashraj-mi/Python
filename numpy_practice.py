import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("2D Array:\n", arr2d)

print("Shape of 1D Array:", arr.shape)
print("Shape of 2D Array:", arr2d.shape)

print("Data type of 1D Array:", arr.dtype)
print("Data type of 2D Array:", arr2d.dtype)


arr = np.arange(1, 10, 2)
print(arr)

print(arr.size)

arr = np.zeros((2, 3))
print(arr)

arr = np.ones((3, 3))
print(arr)

arr = np.full((3, 3), 5)
print(arr)


arr = np.linspace(0, 1, 5)
print(arr)

arr = np.random.rand(2, 3)
print(arr)

arr = np.random.randint(1, 10, (2, 3))
print(arr)


arr = np.array([10, 20, 30, 40])

print(arr[0])
print(arr[-1])

print(arr[1:3])

arr = np.array([[1, 2, 3], [4, 5, 6]])


print(arr[:, 1])

arr = np.arange(12)
new = arr.reshape(3, 4)

print(new)

print(np.sum(new, axis=0))
print(np.sum(new, axis=1))

ar = new.reshape(4, 3)
print(ar)
arr = new.flatten()

print(arr)
print(ar.T)

print(arr % 2 == 0)
print(arr[arr % 2 == 0])


#  [1  2  3  4]
#  [5  6  7  8]
#  [9 10 11 12]

arr = np.arange(1, 13)
arr = arr.reshape(3, 4)
print(arr)

print(arr[0:2, 2:3])


arr.reshape(3, 4)
print(arr.reshape(-1, 4))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.concatenate([a, b])
c = np.vstack([a, b])
c = np.hstack([a, b])
c = np.column_stack([a, b])
c = np.stack([a, b], axis=0)
c = np.stack([a, b], axis=1)
print(c)


arr = np.arange(1, 17)
# print(np.split(arr, 3))
print(np.array_split(arr, 4))

arr = arr.reshape(4, -1)
print(arr)

print(np.split(arr, 2, axis=1))


import numpy as np

# Exercise 1 — Create Arrays

arr1 = np.arange(1, 11)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr1.shape, arr2.shape, arr3.shape)
print(arr1.ndim, arr2.ndim, arr3.ndim)
print(arr1.size, arr2.size, arr3.size)
print(arr1.dtype, arr2.dtype, arr3.dtype)


# Exercise 2 — Special Functions

arr4 = np.zeros((3, 3))
arr5 = np.ones((4, 4))
arr6 = np.full((5, 5), 7)
arr7 = np.linspace(0, 1, 10)
arr8 = np.arange(10, 50, 5)
print(arr8)


# Exercise 3 — Random Arrays
arr9 = np.random.rand(3, 3)
print(arr9)
arr10 = np.random.randint(1, 100, (3, 3))
print(arr10)

print(np.min(arr9), np.min(arr10))

# Exercise 4 — Indexing

arr = np.arange(1, 17).reshape(4, 4)

print(arr[0], arr[-1], arr[:, 1:2])
print(arr[1:3, 1:3])
print(arr[0::3, 0::3])

# Exercise 5 — Slicing

arr = np.arange(20)

print(arr[0:5], arr[:-6:-1], arr[0::2], arr[::-1], arr[0::3])


# Exercise 6 — Reshape Practice

arr = np.arange(24)
print("**************************************************")
print(arr.reshape(2, 12), arr.reshape(3, 8), arr.reshape(4, 6), arr.reshape(2, 3, 4))

print(arr.reshape(4, 6).flatten())


# Exercise 7 — -1 Reshape

print(arr.reshape(3, -1), arr.reshape(-1, 6), arr.reshape(2, -1, 3))


# Exercise 8 — Scalar Broadcasting

arr = np.arange(9).reshape(3, 3)

arr = arr + 10
arr *= 5
arr **= 2
print(arr)


# Exercise 9 — Vector Broadcasting
print("------------------------------------------------------")
matrix = np.array([[1, 2, 3], [4, 5, 6]])

vector = np.array([10, 20, 30])

print(matrix + vector)


print("==================================================")

# Exercise 10 — Column Broadcasting

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])


print(a[:, np.newaxis] + b)

print("==================================================")

# Exercise 11 — Axis Understanding

arr = np.arange(1, 13).reshape(3, 4)

print(arr)
print(np.sum(arr, axis=1))
print(np.sum(arr, axis=0))

print(np.mean(arr, axis=1))
print(np.mean(arr, axis=0))

print(np.max(arr, axis=1))
print(np.min(arr, axis=0))

print("===============================================")

# Exercise 13 — Filtering

arr = np.arange(1, 21)

print(arr[arr % 2 == 0])
print(arr[arr % 2 != 0])
print(arr[arr % 3 == 0])
print(arr[(arr > 5) & (arr < 15)])


# Exercise 14 — Conditional Replacement

arr = np.array([1, 2, -2, -1, 4, -3, -6, -8, 4, 10, 98, -88])
arr[arr < 0] = 0
print(arr)
print(np.where(arr > 0, arr, 0))


print("=====================================")

# Exercise 15 — Stacking

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# concatenate
# vstack
# hstack
# stack axis=0
# stack axis=1
# column_stack


print(np.concatenate([a, b]))
print(np.vstack([a, b]))
print(np.hstack([a, b]))
print(np.stack([a, b], axis=0))
print(np.stack([a, b], axis=1))
print(np.column_stack([a, b]))


print("====================================")

# Exercise 16 — Splitting


arr = np.arange(16).reshape(4, 4)
print(arr)

print(np.hsplit(arr, 4))
print(np.vsplit(arr, 4))
print(np.split(arr, 4))
print(np.array_split(arr, 3))


print(
    "=============================================================================================="
)


# Exercise 17 — Matrix Operations

A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

# addition
# subtraction
# element-wise multiplication
# matrix multiplication
# transpose
# determinant
# inverse

print(A + B)
print(A - B)
print(A * B)
print(np.matmul(A, B))
print(A.T)
print(np.linalg.det(A))
print(np.linalg.inv(A))

print("============================================================")


arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)

print(arr.strides)
print(arr.flags)
# view() vs copy()
# if use view thenoriginal array will change but id use copy then  original array will  remain unchanges

print(arr)

print(arr.sum(axis=0).shape)
print(arr.sum(axis=0, keepdims=True).shape)  # keepdims preserve shape
