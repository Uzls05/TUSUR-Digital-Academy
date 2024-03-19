book = {'Petr': '546810', 'Katya': '241815'}

inverted_book = {v: k for k, v in book.items()}

print(f'Book = {book}',end='\n\n')
print(f'Inverted Book = {inverted_book}')

input()