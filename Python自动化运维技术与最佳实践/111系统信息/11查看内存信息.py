import psutil

men = psutil.virtual_memory()

men.total,men.used

print(men.total,men.used)
print	(men.total)
print	(men.free)
print(psutil.swap_memory())
