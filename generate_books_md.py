import os
import glob
import re

def generate_books_md():
    with open('books.md', 'w') as outfile:
        # Write the intro
        outfile.write("# My Book Reviews\n\n")
        outfile.write("Here are my thoughts on the books I've read. Click on a title to read the full review.\n\n")

        # Generate the table of contents
        outfile.write("## Table of Contents\n\n")
        for filename in glob.glob('books/*.md'):
            with open(filename, 'r') as readfile:
                # Extract the book title from the first line of the file
                title = re.search(r'# (.*)', readfile.readline()).group(1)
                # Write a link to the book review in the table of contents
                outfile.write(f"- [{title}](#{title.replace(' ', '-').lower()})\n")
                # Write links to the sections of the book review
                for line in readfile:
                    match = re.search(r'## (.*)', line)
                    if match:
                        section = match.group(1)
                        outfile.write(f"  - [{section}](#{title.replace(' ', '-').lower()}-{section.replace(' ', '-').lower()})\n")
        outfile.write("\n")

        # Write the book reviews
        for filename in glob.glob('books/*.md'):
            with open(filename, 'r') as readfile:
                # Write a horizontal rule before each book review
                outfile.write("---\n\n")
                # Write the book review
                outfile.write(readfile.read() + '\n\n')

if __name__ == "__main__":
    generate_books_md()
