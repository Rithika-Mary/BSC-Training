#Nested List Comparison
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]

print("Multiplication Table:")
for row in table:
    print(row) 