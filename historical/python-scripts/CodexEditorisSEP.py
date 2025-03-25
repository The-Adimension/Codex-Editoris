import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import time
import requests
from urllib.parse import quote
import random
import re

def execute_script(progress_var, complete_callback):
    try:
        # Progress: Start fetching data
        progress_var.set(10)
        time.sleep(1)

        # API URL
        url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AUTH%3A"Petersen%20SE"%20AND%20%28FIRST_PDATE%3A%5B2000%20TO%202025%5D%29&resultType=core&pageSize=1000&sort=P_PDATE_D%20desc&format=json'
        print("Fetching data from API...")
        response = requests.get(url)
        print("Response received with status code:", response.status_code)
        progress_var.set(30)
        time.sleep(1)

        # Parse JSON response
        data = response.json()
        articles = data.get('resultList', {}).get('result', [])
        print(f"Number of articles fetched: {len(articles)}")
        progress_var.set(60)
        time.sleep(1)

        # Define social media post generator
        def generate_social_media_post(title, first_author_lastname):
            templates = [
                f"Proud to share our latest work, '{title}', led by {first_author_lastname} et al. Grateful to be part of this effort:",
                f"Thrilled to see our study, '{title}', now published! Kudos to {first_author_lastname} and the entire team for their hard work:",
                f"Honored to contribute to this publication: '{title}'. Incredible collaboration with {first_author_lastname} et al. Check it out: ",
                f"Excited to share our new paper, '{title}', with {first_author_lastname} et al. Always a pleasure to work with such a great team: ",
                f"Collaborating on '{title}' with {first_author_lastname} et al. has been a rewarding experience. Here's our latest work—check it out: ",
                f"Sharing our latest publication, '{title}', with {first_author_lastname} et al. Proud of what we achieved together: ",
                f"Our new article, '{title}', is finally out! Big thanks to {first_author_lastname} and the coauthors for their dedication & insights: ",
                f"So excited to see our paper, '{title}', in print! A great team effort with {first_author_lastname} et al.: ",
                f"Happy to announce the publication of '{title}', a collaborative effort with {first_author_lastname} and colleagues. Check it out: ",
                f"Our study, '{title}', is now published! Big congratulations to {first_author_lastname} and the team for making this happen: ",
                f"Our new publication '{title}' provides groundbreaking perspectives by {first_author_lastname} and team: ",
                f"Delighted to announce our latest publication '{title}' by {first_author_lastname} et al: ",
                f"Significant research milestone: '{title}' published, demonstrating innovative approaches by {first_author_lastname} & team: ",
                f"Our latest publication '{title}' offers novel methodological insights from {first_author_lastname} et al: ",
                f"Excited to share '{title}', a rigorous investigation led by {first_author_lastname} and team: ",
                f"Breakthrough research '{title}' by {first_author_lastname} & team reshapes scientific understanding: ",
                f"Comprehensive analysis in '{title}' reveals critical findings. Exceptional work by {first_author_lastname}: ",
                f"Exceptional publication '{title}' demonstrates innovative approaches by {first_author_lastname}: ",
                f"Rigorous exploration in '{title}'. Groundbreaking research by {first_author_lastname} & team published: "
            ]
            return random.choice(templates)

        # Generate HTML content
        html_content = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=0.8">
            <title>The Adimension Codex Editoris</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.4;
                    margin: 20px;
                }
                .article {
                    margin: 10px 0;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 0;
                }
                h1 {
                    color: #4f4f4f;
                    margin-bottom: 5px;
                    font-size: 1.8em;
                    font-weight: bold;
                }
                h2 {
                    color: #4f4f4f;
                    margin-bottom: 5px;
                    font-size: 1.2em;
                }
                .button-download {
                    background-color: #b30018;
                    text-decoration: none;
                    color: white;
                    font-size: 0.9em;
                    white-space: nowrap;
                }
                .details, .meta {
                    margin: 5px;
                    font-size: 0.9em;
                    color: #555;
                }
                .meta {
                    display: flex;
                    gap: 15px;
                    flex-wrap: wrap;
                }
                .meta strong {
                    font-weight: bold;
                }
                .author-row {
                    display: inline-flex;
                    align-items: center;
                    gap: 10px;
                    flex-wrap: nowrap;
                    margin-right: 15px;
                }
                .author-name {
                    white-space: nowrap;
                }
                .button {
                    padding: 3px 3px;
                    text-decoration: none;
                    color: black;
                    font-size: 0.9em;
                    white-space: nowrap;
                }
                .linkedin {
                    background-color: #0077b5;
                    color: white;
                }
                .x-button {
                    background-color: #000;
                    color: white;
                }
                .open-access {
                    background-color: #d4edda;
                    color: #155724;
                    padding: 2px 5px;
                    border-radius: 4px;
                    font-size: 0.8em;
                    display: inline-block;
                    margin-right: 5px;
                }
                .copy-button {
                    background-color: #4f4f4f;
                    color: white;
                    font-weight: bold;
                    padding: 5px 5px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                .abstract-header {
                    font-weight: bold;
                    display: inline;
                    margin: 0;
                    color: #000;
                }
                .abstract-content {
                    margin: 0;
                    padding: 0;
                    display: inline;
                    font-size: 0.9em;
                }
                .abstract-container {
                    background-color: #f5f5f5;
                    padding: 5px;
                    margin-top: 10px;
                    font-size: 0.9em;
                }
                .embed-container {
                    display: flex;
                    gap: 15px;
                    margin-top: 10px;
                }
                .embed-container > div {
                    flex: 1;
                    padding: 10px;
                    background-color: #f9f9f9;
                    border: 1px solid #ccc;
                }
                .social-post, .editors-container {
                    background-color: #e6e6e6;
                    padding: 5px;
                    margin-top: 15px;
                    font-size: 1em;
                    color: black;
                    border: 2px dashed #4f4f4f;
                }
                .search-container {
                    margin: 20px 0;
                }
                .search-container input {
                    margin-right: 10px;
                    padding: 5px;
                    font-size: 1em;
                }
                .search-container button {
                    padding: 5px 10px;
                    font-size: 1em;
                    cursor: pointer;
                }
            </style>
            <script>
                function filterArticles() {
                    const keywordInput = document.getElementById('keyword').value.toLowerCase();
                    const startDate = document.getElementById('start-date').value;
                    const endDate = document.getElementById('end-date').value;
                    const articles = document.querySelectorAll('.article');

                    articles.forEach(article => {
                        const abstract = article.querySelector('.abstract-content').textContent.toLowerCase();
                        const keywords = article.querySelector('.details').textContent.toLowerCase();
                        const title = article.querySelector('h2').textContent.toLowerCase();
                        const pubDate = article.querySelector('.meta').textContent.match(/Published on\s([^<]*)/i)?.[1];

                        let matchesKeyword = abstract.includes(keywordInput) || keywords.includes(keywordInput) || title.includes(keywordInput);
                        let matchesDate = true;

                        if (startDate && endDate) {
                            matchesDate = pubDate >= startDate && pubDate <= endDate;
                        }

                        if (matchesKeyword && matchesDate) {
                            article.style.display = '';
                        } else {
                            article.style.display = 'none';
                        }
                    });
                }

                function resetFilters() {
                    document.getElementById('keyword').value = '';
                    document.getElementById('start-date').value = '';
                    document.getElementById('end-date').value = '';
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
            <script async src="https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js"></script>
        </head>
        <body>
            <h1>The Adimension | Codex Editoris R4.2</h1>
            <div class="cc-container"><br>To AÏA | Codex Editoris © The Adimension 2025.<br><br></div>
            <div class="search-container">
                <label for="keyword">Search:</label>
                <input type="text" id="keyword" placeholder="Enter keywords...">
                <label for="start-date">From:</label>
                <input type="date" id="start-date">
                <label for="end-date">To:</label>
                <input type="date" id="end-date">
                <button onclick="filterArticles()">Filter</button>
                <button onclick="resetFilters()">Reset</button>
            </div>
        '''

        # Generate HTML content for each article
        for article in articles:
            # Log all journal titles for debugging
            journal = article.get('journalInfo', {}).get('journal', {}).get('title', '')
            print(f"Journal title fetched: {journal}")

            title = article.get('title', 'No Title')
            abstract = article.get('abstractText', 'No Abstract Available').replace('\n', ' ').strip()
            keywords = ', '.join(article.get('keywordList', {}).get('keyword', []))
            doi = article.get('doi', None)
            doi_url = f'https://doi.org/{doi}' if doi else '#'
            links = article.get('fullTextUrlList', {}).get('fullTextUrl', [])
            issue = article.get('journalInfo', {}).get('issue', 'N/A')
            volume = article.get('journalInfo', {}).get('volume', 'N/A')
            pub_date = article.get('journalInfo', {}).get('printPublicationDate', 'Unknown Date')
            pmid = article.get('pmid', 'N/A')
            pmcid = article.get('pmcid', 'N/A')

            print(f"Processing article: {title}")

            # Check for open access
            is_open_access = article.get('isOpenAccess', 'N') == 'Y'

            # Extract authors
            authors = article.get('authorList', {}).get('author', [])
            first_author_lastname = authors[0].get('lastName', 'Unknown') if authors else 'Unknown'
            author_rows = ""
            for author in authors:
                first_name = author.get('firstName', '')
                last_name = author.get('lastName', '')
                full_name = f"{first_name} {last_name}".strip()
                linkedin_link = f'https://www.linkedin.com/search/results/people/?keywords={quote(full_name)}'
                x_link = f'https://twitter.com/search?q={quote(full_name)}&f=user'

                author_rows += f'''
                <span class="author-row">
                    <span class="author-name">{full_name}</span>
                    <a href="{linkedin_link}" target="_blank" class="button linkedin">In</a>
                    <a href="{x_link}" target="_blank" class="button x-button">X</a>
                </span>
                '''

            # Generate PDF link
            pdf_url = next(
                (url['url'] for url in links if url.get('documentStyle') == 'pdf'), '#'
            )

            # Generate social media post
            social_post = generate_social_media_post(title, first_author_lastname)

            html_content += f'''
            <div class="article">
                <h2>{title}</h2>
                <div class="meta">
                    {'<span class="open-access">Open Access</span>' if is_open_access else ''}
                    <strong>Issue</strong> {issue} <strong>Vol</strong> {volume} <strong>Published on</strong> {pub_date} <strong>PMID</strong> {pmid} <strong>PMCID</strong> {pmcid}
                </div>
                <div class="meta">
                    <a href="{pdf_url}" target="_blank" class="copy-button">Download PDF</a>
                </div>
                <div class="details">
                    <strong>Keywords:</strong> {keywords}<br>
                    <strong>DOI:</strong> <a href="{doi_url}" target="_blank">{doi_url}</a> <button class="copy-button" onclick="copyToClipboard('{doi_url}')">Copy DOI</button>
                </div>
                <div class="details">
                    <strong>Authors:</strong> {author_rows}
                </div>
                <div class="abstract-container">
                    <span class="abstract-header">Abstract:</span>
                    <span class="abstract-content">{abstract}</span>
                </div>
                <div class="social-post">
                    <strong>Social Media Post:</strong><br><br>
                    {social_post} <button class="copy-button" onclick="copyToClipboard(`{social_post}`)">Copy SoMe Post</button>
                </div>
                <div class="embed-container">
                    <div>
                        <span class="__dimensions_badge_embed__" data-pmid="{pmid}" data-legend="always"></span>
                        <script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
                    </div>
                    <div>
                        <div data-badge-details="right" data-badge-type="medium-donut" data-doi="{doi}" data-legend="always" data-condensed="true" data-hide-no-mentions="false" class="altmetric-embed"></div>
                    </div>
                    <div>
                    <a href="https://plu.mx/plum/a/?doi={doi}" data-popup="top" data-badge="true" class="plumx-plum-print-popup" data-site="plum"><strong>PLUM X</strong> Metrics<svg viewBox="0 0 100 100" width="120" height="125"><path fill="#6e1a62" stroke="#6e1a62" stroke-width="1" d="M 36.075524746876404,57.96956599135724 C 47.24224000477168,47.68596460512846 53.05297314616313,51.90770935123954 46.72339182284403,65.70569425459581 L 53.27660817715597,65.70569425459581 C 46.94702685383687,51.90770935123954 54.11916130196383,46.54361327076243 66.73225377367403,64.96794365950129 L 72.33461419729612,47.7256512143974 C 51.300858350195114,55.217457868193435 48.651416263702714,46.662138123559565 61.88240715909315,39.21976840364822 L 56.58074376063895,35.36788447550181 C 53.59123058093537,50.25112330547885 45.221755705838305,50.334127390178 44.7288145302294,30.470688282908622 L 33.05540672336235,38.951915501347315 C 51.79433272187257,45.55887066943854 49.12908117584119,53.493064614593585 34.05046952557818,51.73708687489691 Z"></path><circle fill="#6e1a62" stroke="#6e1a62" stroke-width="1" r="4" cx="32.880982706687234" cy="55.56230589874905"></circle><circle fill="#6e1a62" stroke="#6e1a62" stroke-width="1" r="4" cx="50" cy="68"></circle><circle fill="#c43bf3" stroke="#6e1a62" stroke-width="1" r="11.066089190457772" cx="75.57002555852411" cy="58.30820493714331"></circle><circle fill="none" stroke="#ffffff" stroke-width="1.5" r="9.566089190457772" cx="75.57002555852411" cy="58.30820493714331"></circle><circle fill="#6e1a62" stroke="#6e1a62" stroke-width="1" r="4" cx"60.58013454126452" cy="35.43769410125095"></circle><circle fill="#fd5704" stroke="#6e1a62" stroke-width="1" r="8.807354922057604" cx="35.92280101098581" cy="30.62439782064578"></circle><circle fill="none" stroke="#ffffff" stroke-width="1.5" r="7.307354922057604" cx="35.92280101098581" cy="30.62439782064578"></circle></svg></a></div>
                </div>
            </div>
        '''
        html_content += '''
        <div>To AÏA | Codex Editoris © The Adimension 2025.</div>
        </body>
        </html>
        '''

        # Save HTML file
        output_file = 'Codex-Editoris.html'
        print("Saving the HTML file...")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"HTML file '{output_file}' generated successfully.")

        # Progress: Complete
        progress_var.set(100)
        time.sleep(1)
        complete_callback(output_file)

    except Exception as e:
        # Handle exceptions
        messagebox.showerror("Error", f"An error occurred: {e}")

def run_app():
    def start_script():
        start_button.config(state=tk.DISABLED)
        progress_bar.grid(row=2, column=0, columnspan=2, pady=10)
        threading.Thread(target=execute_script, args=(progress_var, on_complete)).start()

    def on_complete(output_file):
        save_button.grid(row=3, column=0, columnspan=2, pady=10)
        save_button.config(command=lambda: save_file(output_file))

    def save_file(output_file):
        save_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
        if save_path:
            with open(output_file, 'r', encoding='utf-8') as source:
                content = source.read()
            with open(save_path, 'w', encoding='utf-8') as target:
                target.write(content)
            messagebox.showinfo("Saved", "File saved successfully!")

    # Set up GUI
    root = tk.Tk()
    root.title("Codex Editoris")
    root.geometry("400x300")

    logo_label = tk.Label(root, text="[Codex Editoris Logo]", font=("Arial", 16), pady=20)
    logo_label.grid(row=0, column=0, columnspan=2)

    start_button = tk.Button(root, text="Run Codex Editoris", command=start_script, font=("Arial", 14), bg="blue", fg="white")
    start_button.grid(row=1, column=0, columnspan=2, pady=10)

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=300)

    save_button = tk.Button(root, text="Save Your Codex Editoris Page", font=("Arial", 14), bg="green", fg="white")

    root.mainloop()

if __name__ == "__main__":
    run_app()