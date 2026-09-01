# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add(1)
s1.add(2)
s1.update(("Ola Mundo", 1, 2, 3))
# s1.clear()
s1.discard(2)
s1.discard(3)
print(s1)
