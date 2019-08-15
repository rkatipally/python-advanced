import numpy as np

arr = np.arange(10)
print(arr)
print(arr.shape)
arr = np.zeros((10, 10))
print(arr)
print(arr.shape)
arr = np.linspace(0, 10, 3)
print(arr)

print(np.linspace(0, 10, 55))

print(np.eye(10))
print(np.random.rand(2))
print(np.random.rand(5, 5))

arr = np.arange(0,10)
print(arr)
slice_of_arr = arr[:5].copy() # Without copy it refers to original array
slice_of_arr[:] = 99
print(slice_of_arr)
print(arr)
print(arr.max())
print(arr.min())
print(arr.argmax())
print(arr.argmin())

arr_2d = np.arange(1,10).reshape(3,3)
print(arr_2d)
print(arr_2d[1:2, 0:])
