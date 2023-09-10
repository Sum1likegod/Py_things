set_ex_1 = {-3, -100, 2, 75, 2, 5}
set_ex_2 = set({400, 2130, 59, 860})
print(set_ex_1, '        ', set_ex_2)
print(type(set_ex_2))
print(len(set_ex_1))
set_ex_2.add(4)
print(set_ex_2)
print(len(set_ex_2))
print(sorted(set_ex_2.union(set_ex_1)))
print(len(set_ex_2.union(set_ex_1)))

set_ex=set()
print(set_ex.copy())