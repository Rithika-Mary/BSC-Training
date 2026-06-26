# Generator for even numbers
def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

gen = even_numbers(10)

for num in gen:
    print(num) 