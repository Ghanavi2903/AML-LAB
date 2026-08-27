import numpy as np

x = np.arange(1, 25)

a = x.reshape(4, 6)
b = x.reshape(6, 4)
c = x.reshape(2, 3, 4)

print(a)
print("Shape:", a.shape)
print("ndim:", a.ndim)

print(b)
print("Shape:", b.shape)
print("ndim:", b.ndim)

print(c)
print("Shape:", c.shape)
print("ndim:", c.ndim)