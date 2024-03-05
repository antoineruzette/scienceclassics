import os
import re

def extract_papers_from_bibtex(bibtex_file):
    with open(bibtex_file, 'r') as file:
        bibtex_content = file.read()
    pattern = re.compile(r'@article{(.*?),(.*?)\}', re.DOTALL)
    papers = pattern.findall(bibtex_content)
    return papers

# Directory containing BibTeX files
papers_directory = 'papers/'

# List all BibTeX files in the directory
bibtex_files = [os.path.join(papers_directory, file) for file in os.listdir(papers_directory) if file.endswith('.bib')]

# Extract papers from BibTeX files
all_papers = []
for bibtex_file in bibtex_files:
    all_papers.extend(extract_papers_from_bibtex(bibtex_file))

# Sort papers alphabetically by title
sorted_papers = sorted(all_papers, key=lambda x: x[0].strip())

# Read the existing README file
with open('README.md', 'r') as file:
    readme_content = file.read()

# Find the index of the double dash
double_dash_index = readme_content.index('--') + 2

# Extract content after the double dash
introduction = readme_content[:double_dash_index]
existing_papers = readme_content[double_dash_index:]

# Generate the updated list of papers
updated_readme = introduction + "\n\n"
for title, _ in sorted_papers:
    updated_readme += f"- {title.strip()}\n"

# Write the updated content back to the README file
with open('README.md', 'w') as file:
    file.write(updated_readme)

print("Papers sorted alphabetically and README updated successfully.")
