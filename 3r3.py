import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
c = a[:]
d = a.copy()

a[0][0] = 99

print(a)  # [[99, 2], [3, 4]]
print(b)  # [[1, 2], [3, 4]] ← completamente independente
print(c)  # [[99, 2], [3, 4]] ← referência aos mesmos objetos internos
print(d)  # [[99, 2], [3, 4]] ← referência aos mesmos objetos internos