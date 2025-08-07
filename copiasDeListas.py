# Usa a função copy() para criar uma cópia de uma lista
# e modifica a cópia sem afetar a original
a = [1,5,10]
b = a.copy()
b[0] = 20
print(a)
print(b)

#Cria uma cópia de a, mas não aponta para o mesmo local de memória
c = [10,15,20]
d = c[:]
d[1] = 30
print(c)
print(d)

# F usa o mesmo apontamento de memória que e
e = [1,2,3]
f = e 
f[0] = 4
print(e)
print(f)