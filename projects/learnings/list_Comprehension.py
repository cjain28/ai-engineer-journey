print(list(range(5)))

square = []
for x in range(5):
    square.append(x*x)
    print(square)

print(", ".join(str(x*x) for x in range(5)))

square = [x*x for x in range(5)]
print(square)