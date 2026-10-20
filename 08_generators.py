# 1. Write a Python generator function even_numbers(n) that yields all even numbers from 0 up to, but not including, n.

def even_numbers(n):
  for i in range(n):
      if i%2 == 0:
        yield i
  

result = even_numbers(10)

try:
  print(next(result))
  print(next(result))
  print(next(result))
  print(next(result))
  print(next(result))
  print(next(result))
except StopIteration:
  print("Exceeded Iteration limit")

# 2. Write a generator that reads numbers lazily, filters even numbers, squares them, and returns only the first k results.
# pipeline(range(1, 1000000), 3) should produce 4, 16, 36.

def lazy_sequence(_range):
  for i in _range:
    if i%2 == 0:
      yield i**2

def pipeline(_range, k):
  sequence = lazy_sequence(_range)
  for i in range(k):
    yield next(sequence)

result = pipeline(range(1,100000), 3)
print(next(result))
print(next(result))
print(next(result))

# 3. Create a generator that yields overlapping windows of size k. 
# list(sliding_window([1, 2, 3, 4, 5], 3))
# [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

def sliding_window(ls, k):
    length = len(ls) - k+1
    if length < 0:
        return 
    for i in range(length):
        yield tuple(ls[i:i+k])

res = sliding_window([1, 2, 3, 4, 5], 3)
print(next(res))
print(next(res))


