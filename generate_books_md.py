import os
import glob
import re

def generate_books_md():
    # Define the path to the README.md file
    readme_path = 'books/README.md'

    # Read the existing README.md file
    with open(readme_path, 'r') as infile:
        content = infile.read()

    # Generate the book table
    book_table = "\n<!--BOOK_TABLE_START-->\n"
    book_table += "| Title | Author | Started Reading | Finished Reading | Genres | Rating |\n"
    book_table += "| --- | --- | --- | --- | --- | --- |\n"
    for filename in glob.glob('books/*.md'):
        if filename == readme_path:
            continue  # Skip the README.md file
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
            book_table += f"| [{title}]({os.path.basename(filename)}) | {author} | {start_date} | {end_date} | {genres} | {rating} |\n"
    book_table += "<!--BOOK_TABLE_END-->\n"

    # Replace the old book table with the new one
    new_content = re.sub('<!--BOOK_TABLE_START-->.*<!--BOOK_TABLE_END-->', book_table, content, flags=re.DOTALL)

    # Write the new README.md file
    with open(readme_path, 'w') as outfile:
        outfile.write(new_content)

if __name__ == "__main__":
    generate_books_md()
