# TODO Найдите количество книг, которое можно разместить на дискете
size_of_diskette = 1.44
number_of_pages = 100
number_of_lines = 50
number_of_symbols = 25
size_one_symbol = 4
size_of_diskette = size_of_diskette * 1024 * 1024
size_of_book = number_of_pages * number_of_lines * number_of_symbols * size_one_symbol
number_of_books = int (size_of_diskette // size_of_book)
print("Количество книг, помещающихся на дискету:", number_of_books)
