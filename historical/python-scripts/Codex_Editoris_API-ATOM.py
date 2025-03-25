
# Dependencies
import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote
import random

# API URL for arXiv
arxiv_url = ('http://export.arxiv.org/api/query?'
             'search_query=all:%22ahmed+khalifa%22+AND+cat:cs*'
             '&start=0&max_results=200&sortBy=submittedDate&sortOrder=descending')

# Fetch data from the arXiv API
print("Fetching data from arXiv API...")
response = requests.get(arxiv_url)
print("Response received with status code:", response.status_code)

if response.status_code == 200:
    # Parse the XML response
    root = ET.fromstring(response.content)
    namespace = {'atom': 'http://www.w3.org/2005/Atom'}  # Define the namespace for parsing

    # Extract relevant article details
    entries = root.findall('atom:entry', namespace)
    print(f"Number of articles fetched: {len(entries)}")

    def generate_social_media_post(title, first_author):
        """
        Generate an engaging, professional, and scientific social media post.
        """
        templates = [
            f"Proud to share our latest work, '{title}', led by {first_author} et al. Grateful to be part of this effort:",
            f"Thrilled to see our study, '{title}', now published! Kudos to {first_author} and the entire team for their hard work:",
            f"Honored to contribute to this publication: '{title}'. Incredible collaboration with {first_author} et al. Check it out: ",
            f"Proud to share our latest work, '{title}', led by {first_author} et al. Grateful to be part of this effort:",
            f"Thrilled to see our study, '{title}', now published! Kudos to {first_author} and the entire team for their hard work:",
            f"Honored to contribute to this publication: '{title}'. Incredible collaboration with {first_author} et al. Check it out: ",
            f"Excited to share our new paper, '{title}', with {first_author} et al. Always a pleasure to work with such a great team: ",
            f"Collaborating on '{title}' with {first_author} et al. has been a rewarding experience. Here's our latest work—check it out: ",
            f"Sharing our latest publication, '{title}', with {first_author} et al. Proud of what we achieved together: ",
            f"Our new article, '{title}', is finally out! Big thanks to {first_author} and the coauthors for their dedication & insights: ",
            f"So excited to see our paper, '{title}', in print! A great team effort with {first_author} et al.: ",
            f"Happy to announce the publication of '{title}', a collaborative effort with {first_author} and colleagues. Check it out: ",
            f"Our study, '{title}', is now published! Big congratulations to {first_author} and the team for making this happen: "
            f"Our new publication '{title}' provides groundbreaking perspectives by {first_author} and team: ",
            f"Delighted to announce our latest publication '{title}' by {first_author} et al: ",
            f"Significant research milestone: '{title}' published, demonstrating innovative approaches by {first_author} & team: "
        ]
        return random.choice(templates)

    # Generate HTML content for each article
    html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Codex Editoris | ArXiv Edition</title>
    <script>
        function filterArticles() {
            const query = document.getElementById('search').value.toLowerCase();
            const articles = document.querySelectorAll('.article');

            articles.forEach(article => {
                const title = article.querySelector('h2')?.textContent.toLowerCase() || '';
                const summary = article.querySelector('p:nth-of-type(2)')?.textContent.toLowerCase() || '';

                if (title.includes(query) || summary.includes(query)) {
                    article.style.display = '';
                } else {
                    article.style.display = 'none';
                }
            });
        }

        function resetFilter() {
            document.getElementById('search').value = '';
            const articles = document.querySelectorAll('.article');
            articles.forEach(article => {
                article.style.display = '';
            });
        }

        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => {
                alert('Copied to clipboard!');
            });
        }
    </script>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        #search-bar {
            margin: 20px;
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        #search {
            padding: 10px;
            font-size: 16px;
            width: 300px;
        }
        #search-btn, #reset-btn {
            padding: 10px;
            font-size: 16px;
            cursor: pointer;
        }
        .article {
            border: 1px solid #ccc;
            padding: 15px;
            margin: 10px;
            border-radius: 5px;
            box-shadow: 2px 2px 5px #aaa;
        }
    </style>
</head>
<body>
    <h1>Codex Editoris | ArXiv Edition: Ahmed Khalifa</h1>

    <!-- Search Bar -->
    <div id="search-bar">
        <input type="text" id="search" placeholder="Search articles by title or summary...">
        <button id="search-btn" onclick="filterArticles()">Search</button>
        <button id="reset-btn" onclick="resetFilter()">Reset</button>
    </div>
    '''

    for entry in entries:
        title = entry.find('atom:title', namespace).text
        authors = entry.findall('atom:author/atom:name', namespace)
        first_author = authors[0].text if authors else 'Unknown'
        summary = entry.find('atom:summary', namespace).text
        pdf_link = entry.find('atom:link[@title="pdf"]', namespace).attrib.get('href', '#')

        # Generate social media post
        social_post = generate_social_media_post(title, first_author)

        html_content += f'''
        <div class="article">
            <h2>{title}</h2>
            <p><strong>First Author:</strong> {first_author}</p>
            <p><strong>Summary:</strong> {summary}</p>
            <p><a href="{pdf_link}" target="_blank">Download PDF</a></p>
            <p><strong>Social Media Post:</strong> {social_post}<br>{pdf_link} </p><button class="copy-button" onclick="copyToClipboard(`{social_post} {pdf_link}`)">Copy SoMe Post</button>
        </div>
        </div>
        '''

    html_content += '''
    </body>
    </html>
    '''

    # Save to an HTML file
    output_file = 'arxiv_results.html'
    print("Saving the HTML file...")
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"HTML file '{output_file}' generated successfully.")
else:
    print("Failed to fetch data from the arXiv API.")
