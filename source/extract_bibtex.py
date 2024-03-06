import os
import re


def extract_papers_from_bibtex(bibtex_file):
    with open(bibtex_file, 'r') as file:
        bibtex_content = file.read()
            
    pattern = re.compile(r'''
        @article{(?P<id>.*?),
        \s*title\s*=\s*{(?P<title>.*?)}.*?,
        \s*author\s*=\s*{(?P<author>.*?)}.*?,
        \s*journal\s*=\s*{(?P<journal>.*?)}.*?,
        \s*volume\s*=\s*{(?P<volume>.*?)}.*?,
        \s*number\s*=\s*{(?P<number>.*?)}.*?,
        \s*pages\s*=\s*{(?P<pages>.*?)}.*?,
        \s*year\s*=\s*{(?P<year>.*?)}.*?,
        \s*doi\s*=\s*{(?P<doi>.*?)}.*?
        ''', re.DOTALL | re.VERBOSE)
    
    papers = []
    for match in pattern.finditer(bibtex_content):
        print(match)
        title = match.group('title').strip()
        author = match.group('author').strip()
        journal = match.group('journal').strip()
        volume = (match.group('volume').strip()
                  if 'volume' in match.groupdict()
                  else '')
        number = (match.group('number').strip() 
                  if 'number' in match.groupdict() 
                  else '')
        pages = (match.group('pages').strip() 
                 if 'pages' in match.groupdict() 
                 else '')
        year = (match.group('year').strip() 
                if 'year' in match.groupdict() 
                else '')
        doi = (match.group('doi').strip() 
               if 'doi' in match.groupdict() 
               else '')
        url = (match.group('url').strip() 
               if 'url' in match.groupdict() 
               else '')
        papers.append((title, author, journal, volume, number, pages, year, doi, url))

    return papers


def convert_to_apa_citation(author, title, journal, year, volume, number, pages):
    citation_parts = []
    
    if author:
        citation_parts.append(f"{author.strip()}.")
    if year:
        citation_parts.append(f"({year.strip()}).")
    if title:
        citation_parts.append(f"{title.strip()}.")
    if journal:
        citation_parts.append(f"_{journal.strip()}_,")
    if volume:
        citation_parts.append(f"{volume.strip()},")
    if number:
        citation_parts.append(f"({number.strip()}),")
    if pages:
        citation_parts.append(f"{pages.strip()}.")
    
    citation = " ".join(citation_parts)
    return citation


# Directory containing BibTeX files
papers_directory = 'papers/'

# List all BibTeX files in the directory
bibtex_files = [os.path.join(papers_directory, file)
                for file in os.listdir(papers_directory)
                if file.endswith('.bib')]

# Extract papers from BibTeX files
all_papers = []
for bibtex_file in bibtex_files:
    print(bibtex_file)
    all_papers.extend(extract_papers_from_bibtex(bibtex_file))
    print(all_papers)

# Sort papers alphabetically by title
sorted_papers = sorted(all_papers, key=lambda x: x[1].strip())

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
for title, author, journal, volume, number, pages, year, _, _ in sorted_papers:
    apa_citation = convert_to_apa_citation(author,
                                           title,
                                           journal,
                                           year,
                                           volume,
                                           number,
                                           pages)
    updated_readme += f"- {apa_citation}\n"

# Write the updated content back to the README file
with open('README.md', 'w') as file:
    file.write(updated_readme)

print("Papers sorted alphabetically and README updated successfully.")
