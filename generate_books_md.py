import os
import glob

def generate_books_md():
    with open('books.md', 'w') as outfile:
        for filename in glob.glob('books/*.md'):
            with open(filename, 'r') as readfile:
                outfile.write(readfile.read() + '\n\n')

if __name__ == "__main__":
    generate_books_md()
