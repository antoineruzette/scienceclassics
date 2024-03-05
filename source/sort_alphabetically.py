import re

# Read the README file
with open('README.md', 'r') as file:
    readme_content = file.read()

# Extract the list of papers
pattern = r'\[(.*?)\]\((.*?)\)'
papers = re.findall(pattern, readme_content)

# Sort papers alphabetically by title
sorted_papers = sorted(papers, key=lambda x: x[0])

# Generate the updated README content
updated_readme = "# List of Papers\n\n"
for title, link in sorted_papers:
    updated_readme += f"- [{title}]({link})\n"

# Write the updated content back to the README file
with open('README.md', 'w') as file:
    file.write(updated_readme)

print("Papers sorted alphabetically and README updated successfully.")
