import requests
import pandas as pd
import random
from urllib.parse import quote

# API URL
url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=JOURNAL%3A"Eur%20Heart%20J%20Imaging%20Methods%20Pract"&resultType=core&pageSize=1000&sort=P_PDATE_D desc&format=json'

# Fetch data from the API
print("Fetching data from API...")
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
    exit()

data = response.json()

# Extract relevant articles
articles = data.get('resultList', {}).get('result', [])
print(f"Number of articles fetched: {len(articles)}")

social_media_templates = [
    "'{title}' by {last_name} et al. brings a fresh perspective to #CVImaging. Read it now in #EHJIMP!",
    "Explore '{title}' by {last_name} et al., redefining innovation in cardiovascular research. Discover more in #EHJIMP.",
    "'{title}'—an essential read from {last_name} et al., showcasing cutting-edge science in #EHJIMP!",
    "Innovative research alert: '{title}' by {last_name} et al. is now available in #EHJIMP.",
    "Leading the way in #CVImaging: '{title}' by {last_name} et al., featured in #EHJIMP.",
    "Explore '{title}', the latest in groundbreaking research by {last_name} et al. Read it in #EHJIMP!",
    "Don't miss the study '{title}' by {last_name} et al., a key contribution to cardiovascular science. Now in #EHJIMP!",
    "{last_name} et al. present impactful findings in '{title}'. Read this important study in #EHJIMP.",
    "New in #EHJIMP: '{title}' by {last_name} et al., offering novel insights into imaging science.",
    "Highlighting '{title}'—{last_name} et al. reveal transformative discoveries in #EHJIMP.",
    "Discover how '{title}' by {last_name} et al. is shaping the future of imaging research. Read in #EHJIMP!",
    "Exciting research from {last_name} et al.: '{title}' explores new dimensions in #CVImaging. Featured in #EHJIMP.",
    "Explore the paradigm-shifting study '{title}' by {last_name} et al., now in #EHJIMP!",
    "Revolutionizing #CVImaging: {last_name} et al. unveil '{title}' in #EHJIMP.",
    "Stay at the forefront of cardiovascular science: Read '{title}' by {last_name} et al., now in #EHJIMP!",
    "Discover cutting-edge insights in '{title}'. {last_name} et al. present their latest findings in #EHJIMP!",
    "The latest research by {last_name} et al. explores '{title}'. Dive deeper in #EHJIMP!",
    "Explore the groundbreaking study '{title}' by {last_name} et al., now featured in #EHJIMP.",
    "Exciting developments in #CVImaging: '{title}' by {last_name} et al. Read more in #EHJIMP!",
    "'{title}'—a must-read study by {last_name} et al., pushing the boundaries of knowledge in #EHJIMP!",
    "Delve into the latest advancements in '{title}'. {last_name} et al. share groundbreaking findings in #EHJIMP!",
    "New insights unveiled by {last_name} et al. in '{title}'. Discover the details in #EHJIMP!",
    "Check out the innovative study '{title}' by {last_name} et al., now spotlighted in #EHJIMP.",
    "Significant strides in #CVImaging: '{title}' authored by {last_name} et al. Explore more in #EHJIMP!",
    "'{title}'—a pivotal contribution by {last_name} et al., expanding horizons in #EHJIMP!",
    "Uncover pioneering research in '{title}' by {last_name} et al. Read more in #EHJIMP!",
    "Discover how {last_name} et al. are advancing the field with '{title}', now featured in #EHJIMP!",
    "The study '{title}' by {last_name} et al. offers fresh perspectives in #CVImaging. Explore it in #EHJIMP!",
    "Breaking new ground in imaging science: '{title}' by {last_name} et al., highlighted in #EHJIMP!",
    "Transformative research '{title}' by {last_name} et al. is shaping the future of #CVImaging. Learn more in #EHJIMP!",
    "New research in #EHJIMP: '{title}' by {last_name} et al.",
    "Latest insights: '{title}' by {last_name} et al. in #EHJIMP.",
    "Read '{title}' by {last_name} et al. in #EHJIMP now!",
    "Exciting study! '{title}' by {last_name} et al. in #EHJIMP.",
    "Breakthrough research: '{title}' by {last_name} et al. in #EHJIMP!",
    "Big news! '{title}' by {last_name} et al. just published in #EHJIMP.",
    "Game-changing study: '{title}' by {last_name} et al. in #EHJIMP.",
    "Must-read: '{title}' by {last_name} et al. in #EHJIMP.",
    "Fresh insights! '{title}' by {last_name} et al. in #EHJIMP.",
    "Check out '{title}' by {last_name} et al. in #EHJIMP!",
    "Curious about imaging? Read '{title}' by {last_name} et al. in #EHJIMP.",
    "New perspectives: '{title}' by {last_name} et al. in #EHJIMP.",
    "'{title}' by {last_name} et al. offers key insights—#EHJIMP.",
    "Breaking new ground: '{title}' by {last_name} et al. in #EHJIMP.",
    "Fresh off the press: '{title}' by {last_name} et al. in #EHJIMP.",
    "Latest contribution to #CVImaging: '{title}' by {last_name} et al. in #EHJIMP.",
    "Examining the findings in '{title}' by {last_name} et al., now published in #EHJIMP.",
    "Exciting developments in #CVImaging! '{title}' by {last_name} et al. is now in #EHJIMP.",
    "Major progress in the field! '{title}' by {last_name} et al. is making an impact in #EHJIMP.",
    "A must-read for imaging enthusiasts! '{title}' by {last_name} et al. is now available in #EHJIMP.",
    "Big news in #CVImaging! '{title}' by {last_name} et al. is in #EHJIMP.",
    "Key findings from '{title}' by {last_name} et al. now published in #EHJIMP.",
    "Exciting research ahead! '{title}' by {last_name} et al. is featured in #EHJIMP.",
    "Breakthrough insights: '{title}' by {last_name} et al. is now in #EHJIMP.",
    "Let’s discuss! '{title}' by {last_name} et al. offers key insights in #EHJIMP. Thoughts?",
    "What do you think about '{title}' by {last_name} et al.? Read it now in #EHJIMP and share your views!",
    "Join the conversation on '{title}' by {last_name} et al., now in #EHJIMP. Let’s explore the findings together!"
]

# Prepare data for Excel
article_data = []

for article in articles:
    title = article.get('title', 'No Title')
    abstract = article.get('abstractText', 'No Abstract Available').replace('\n', ' ').strip()
    pmid = article.get('pmid', 'N/A')

    # Extract authors
    authors = article.get('authorList', {}).get('author', [])

    if authors:
        first_author_name = f"{authors[0].get('firstName', '')} {authors[0].get('lastName', '')}".strip()
        last_author_name = f"{authors[-1].get('firstName', '')} {authors[-1].get('lastName', '')}".strip()
        all_authors = "; ".join([f"{author.get('firstName', '')} {author.get('lastName', '')}".strip() for author in authors])

        # Extract last name of first author
        first_author_last_name = authors[0].get('lastName', 'Unknown')

        # Generate author links
        first_author_x = f"https://twitter.com/search?q={quote(first_author_name)}"
        first_author_linkedin = f"https://www.linkedin.com/search/results/people/?keywords={quote(first_author_name)}"
        last_author_x = f"https://twitter.com/search?q={quote(last_author_name)}"
        last_author_linkedin = f"https://www.linkedin.com/search/results/people/?keywords={quote(last_author_name)}"
    else:
        first_author_name = "Unknown"
        last_author_name = "Unknown"
        first_author_last_name = "Unknown"
        all_authors = "Unknown"
        first_author_x = "N/A"
        first_author_linkedin = "N/A"
        last_author_x = "N/A"
        last_author_linkedin = "N/A"

    # Generate DOI link
    doi = article.get('doi', None)
    doi_url = f'https://doi.org/{doi}' if doi else 'N/A'

    # Get PDF download link
    links = article.get('fullTextUrlList', {}).get('fullTextUrl', [])
    pdf_url = next((url['url'] for url in links if url.get('documentStyle') == 'pdf'), 'N/A')

    # Generate social media post with the correct last name
    social_media_post = random.choice(social_media_templates).format(title=title, last_name=first_author_last_name)

    # Append extracted data to list
    article_data.append([
        title, abstract, pmid,
        first_author_name, last_author_name,
        first_author_x, first_author_linkedin,
        last_author_x, last_author_linkedin,
        all_authors, doi_url, pdf_url, social_media_post
    ])

# Convert data to DataFrame
df = pd.DataFrame(article_data, columns=[
    "Title", "Abstract", "PMID",
    "First Author", "Last Author",
    "First Author X Link", "First Author LinkedIn Link",
    "Last Author X Link", "Last Author LinkedIn Link",
    "All Authors", "DOI Link", "PDF Download Link", "Social Media Post"
])

# Save as Excel file
output_file = "EHJIMP_Articles.xlsx"
df.to_excel(output_file, index=False, engine='openpyxl')  # Use 'openpyxl' for .xlsx files

print(f"Excel file '{output_file}' generated successfully!")

