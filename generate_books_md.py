import os
import glob
import re

def generate_books_md():
    with open('books.md', 'w') as outfile:
        # Write the intro
        outfile.write("# My Book Reviews\n\n")
        outfile.write("Here are my thoughts on the books I've read. Click on a title to read the full review.\n\n")

        # Write the table header
        outfile.write("| Title | Author | Started Reading | Finished Reading | Genres | Rating |\n")
        outfile.write("| --- | --- | --- | --- | --- | --- |\n")

        # Write the table rows
        for filename in glob.glob('books/*.md'):
            with open(filename, 'r') as readfile:
                # Initialize the book info
                title = author = start_date = end_date = genres = rating = ''
                # Extract the book info from the file
                for line in readfile:
                    if line.startswith('# '):
                        title = line[2:].strip()
                    elif line.startswith('**Author:**'):
                        author = line[11:].strip()
                    elif line.startswith('**Started Reading:**'):
                        start_date = line[19:].strip()
                    elif line.startswith('**Finished Reading:**'):
                        end_date = line[21:].strip()
                    elif line.startswith('**Genres:**'):
                        genres = line[10:].strip()
                    elif line.startswith('| Enjoyability'):
                        rating = line.split('|')[2].strip()
                # Write the book info in the table
                outfile.write(f"| [{title}](books/{os.path.basename(filename)}) | {author} | {start_date} | {end_date} | {genres} | {rating} |\n")

if __name__ == "__main__":
    generate_books_md()
