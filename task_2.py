# TODO Найдите количество книг, которое можно разместить на дискете
memory = 1.44
pages = 100
lines = 50
symbols = 25
mem_symbols = 4
memory_bytes = 1.44 * 1024 *1024
books = memory_bytes / (pages * lines * symbols * mem_symbols)
print("Количество книг, помещающихся на дискету:",round(books))
