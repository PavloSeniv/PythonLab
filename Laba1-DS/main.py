<<<<<<< HEAD
# Task NumPy
import numpy as np

f=[1,2,3]

x=np.array(f)

print(type(f))
print(type(x))

print(np.array([range(i,i+5) for i in range(3)]))

a=[0,1,2,3,4,5,6,7,8,9]
b=np.arange(10)

print(a*5)
print(b*5)

# print(a**5)
print(b**5)

# print(a+5)
print(b+5)

# Доробити для списку генератор
print(b%2)

c=np.array([2,2,6,4,5])

# print(b==c)
# print(b<c)
# print(b>c)
print(np.array([2,1,6,4,5])+c)
print([2,3,4,5,6]+c)

print(c>10)
print(c[c>10])

print(b.sum())
print(b.min())
print(b.max())
# Те саме для списку

n1=np.array([2,2,6,4,5])

print(n1.ndim)
print(n1.shape)
print(n1.size)
print(n1.dtype)

b = np.arange(16).reshape(4,4)
print(b.sum(axis = 0)) # Сумма элементов каждого столбца
print(b.sum(axis = 1)) # Сумма элементов каждой строки
print(b.min(axis = 1)) # Минимальный элемент каждой строки
print(b.max(axis = 0)) # Максимальный элемент каждого столбца

n = np.arange(0, 30, 2)
print(n)
n = n.reshape(3, 5)
print(n)
o = np.linspace(0, 4, 9)
print(o)
print(o.resize(3, 3))

#########################################

# Tasks to perform

month=np.array([4,1,0,-2,5,7,-3,0,0,5,0,-1,3,6,9,5,7,11,9,6,0])
zero = month[month<0]
print(zero)
print(np.count_nonzero(zero < 0))

print(month.argmax())

print(np.any(month > 10))
print(np.any(month > 20))
print(np.all(month < 10))

print(zero)

print(np.sort(zero))

#########################################

# Create array

print(np.array([4,6,8,0,9,5]))

print(np.array([1, 2, 3, 4], dtype='float32'))

print(np.zeros(10, dtype=int))

print(np.ones(3))

print(np.zeros((3, 5), dtype=float))

print(np.full((2, 2), 100))

print(np.arange(10, 101, 10))

print(np.linspace(10, 100, num=15))

print(np.random.rand(4))

print(np.random.random((3, 3)))

print(np.random.randint(0, 10, (3, 3)))

print(np.eye(3))

m=[[1,2],[3,4]]
print(m)

n=np.array(m)
print(n)

print(n[1][1])
# or
print(n[1,1])

n[0, 0] = 12
print(n)

#########################################

# Tasks to perform
# Actions with vectors

v = np.array([1, 0])
u = np.array([2, 2])
print(v + u)

print(v - u)

print(2 * v)

from numpy import dot
print(v.dot(u))
# or
dot = np.dot(u,v)
print(dot)

print(np.linalg.norm(v))
# or
from numpy.linalg import norm
len_v = norm(v)
print(len_v)
len_u = norm(u)
print(len_u)

print(norm(v-u))

angle_vectors=dot/(len_v*len_u)
print(angle_vectors)

print(u.shape)

#########################################

# Actions with matrices
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

print(a[2,:])
print(a[:,2])

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.dot(a,b))

v = np.array([1, 0])
a = np.array([3, 0])
print(np.dot(a,v))

m_sqr_mx = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8,9]])
print(m_sqr_mx)

A = np.matrix([ [3, 5], [1, 0]])
B = np.matrix([ [2, -3], [1,2]])
print(A + B)

print(2 * A)

print(A.dot(B))

A_t = A.transpose()
print(A_t)

print(B.T)

# Перевірити, що (AT)T

print(np.linalg.det(A))
print(np.linalg.inv(A))

from numpy.linalg import matrix_rank
mat_rang = matrix_rank(np.eye(4))
print(mat_rang)

a = np.array([[1,5],[2,3]])
print(a)
b = np.array([11,8])
print(b)
x = np.linalg.solve(a,b)
print(x)
print(np.dot(a,x))


a = np.array([[2, 3, 5], [7, 11, 13], [17, 19, 23]])
w,v=np.linalg.eig(a)
print(w,v)


>>>>>>> 22b019313540c418e639a75e9c6ed1a7caa9351a
