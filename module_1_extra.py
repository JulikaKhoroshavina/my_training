grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
numbers_a = grades [0]
numbers_b = grades [1]
numbers_j = grades [2]
numbers_k = grades [3]
numbers_s = grades [4]
average_a = sum(numbers_a) / len(numbers_a)
average_b = sum(numbers_b) / len(numbers_b)
average_j = sum(numbers_j) / len(numbers_j)
average_k = sum(numbers_k) / len(numbers_k)
average_s = sum(numbers_s) / len(numbers_s)
dictionary = {'Aaron':average_a, 'Bilbo':average_b, 'Johnny':average_j,'Khendrik': average_k, 'Steve':average_s}
print(dictionary)