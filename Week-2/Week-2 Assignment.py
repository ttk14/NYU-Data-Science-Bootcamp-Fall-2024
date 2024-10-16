import numpy as np
import pandas as pd

# Numpy Questions
# Question 1
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

vertical_stack = np.vstack((A, B))
horizontal_stack = np.hstack((A, B))

print("Array A:\n", A)
print("Array B:\n", B)
print("\nVertical Stack:\n", vertical_stack)
print("\nHorizontal Stack:\n", horizontal_stack)


# Question 2
A = np.array([1, 2, 3, 4, 5, 9])
B = np.array([3, 6, 7, 8, 9, 10])

common_elements = np.intersect1d(A, B)
print("Common elements:", common_elements)


# Question 3
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

lower_bound = 5
upper_bound = 10

numbers_within_range = A[(A >= lower_bound) & (A <= upper_bound)]
print(numbers_within_range)


# Question 4
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

filtered_iris_2d = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]
print(filtered_iris_2d)


# Pandas Questions
# Question 5
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url, sep='\t')
filtered_df = df.loc[::20, ['Manufacturer', 'Model', 'Type']]
print(filtered_df)


# Question 6
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

mean_min_price = df['Min.Price'].mean()
mean_max_price = df['Max.Price'].mean()

df['Min.Price'].fillna(mean_min_price, inplace=True)
df['Max.Price'].fillna(mean_max_price, inplace=True)

print(df[['Min.Price', 'Max.Price']])


# Question 7
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
filtered_rows = df[df.sum(axis=1) > 100]
print(filtered_rows)
