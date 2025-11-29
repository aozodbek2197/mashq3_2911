# 1-mashq
my_tuple = ("a", "b", "c", "d")

yangi_tuple = tuple((i, element) for i, element in enumerate(my_tuple))

print(yangi_tuple)

# 2-mashq
mevalar = ("apple", "banana", "kiwi", "orange", "olim")

yangi_tuple = tuple(soz[::-1] for soz in mevalar)

print(yangi_tuple)
