import random
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image, ImageDraw
import io
import base64

# Define color palette
colors = {
    "Dark Red": "#8C1B24",
    "Bright Red": "#BF1F1F",
    "Deep Maroon": "#592323",
    "Dark Charcoal": "#2E2B2B",
    "Warm Gray": "#D9D6D6",
    "Stone Gray": "#B0AFAF",
    "Ivory": "#F0F0F0"
}

# Define the base URL for constructing full links
BASE_URL = "https://link.springer.com"

# Step 1: Fetch and Parse the Website with Pagination
def fetch_articles(base_url):
    articles = []
    current_url = base_url
    
    while current_url:
        print(f"Scraping URL: {current_url}")
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Parse and collect articles
        article_container = soup.find('ol', class_='u-list-reset', attrs={"data-test": "darwin-search"})
        if article_container:
            for item in article_container.find_all('li'):
                title_tag = item.find('h3', class_='app-card-open__heading', attrs={"data-test": "title"})
                title = title_tag.get_text(strip=True) if title_tag else "No title found"
                
                link_tag = item.find('a', class_='app-card-open__link')
                link = BASE_URL + link_tag['href'] if link_tag else None
                doi_link = link.replace("https://link.springer.com/article/", "https://www.doi.org/") if link else "No DOI link"
                
                author_tag = item.find('span', attrs={"data-test": "authors"})
                if author_tag:
                    authors = author_tag.get_text(strip=True).split(", ")
                    first_author = authors[0]
                    last_author = authors[-1] if len(authors) > 1 else "None"
                else:
                    first_author = last_author = "No authors listed"

                image_url = None
                picture_tag = item.find('picture')
                if picture_tag:
                    source_tag = picture_tag.find('source', attrs={"media": "(min-width: 480px)"})
                    if source_tag and 'srcset' in source_tag.attrs:
                        image_url = re.sub(r'w\d+h\d+', 'lw800', source_tag['srcset'].split(", ")[1].split(" ")[0])

                entitlement_tag = item.find('div', class_="app-entitlement__text")
                access = "Open" if entitlement_tag and "open" in entitlement_tag.get_text(strip=True).lower() else "Partial"
                date_tag = item.find('span', class_='c-meta__item', attrs={"data-test": "published"})
                publication_date = date_tag.get_text(strip=True) if date_tag else "No date available"

                keywords = []
                if re.search(r'\b(Echocardiography|Echo|Cardiac Echo)\b', title, re.IGNORECASE):
                    keywords.append("Echo")
                if re.search(r'\b(CT|Computed Tomography|Cat Scan)\b', title, re.IGNORECASE):
                    keywords.append("CT")
                if re.search(r'\b(PET|Nuclear|MPI|SPECT)\b', title, re.IGNORECASE):
                    keywords.append("MPI/SPECT")
                if re.search(r'\b(CMR|Cardiac MRI|MRI)\b', title, re.IGNORECASE):
                    keywords.append("CMR")

                articles.append({
                    'title': title,
                    'link': link,
                    'doi_link': doi_link,
                    'first_author': first_author,
                    'last_author': last_author,
                    'image_url': image_url,
                    'access': access,
                    'keywords': ', '.join(keywords) if keywords else "None",
                    'publication_date': publication_date,
                    'first_author_last_name': first_author.split()[-1] if first_author else "Unknown"
                })
        
        next_button = soup.find('a', class_='eds-c-pagination__link', rel='next')
        if next_button and 'href' in next_button.attrs:
            current_url = BASE_URL + next_button['href']
        else:
            print("No more pages to scrape.")
            current_url = None

    return articles

# Step 2: Prepare Post Text with varied introductory phrases
def prepare_post_text(article):
    title = article['title']
    first_author_last_name = article['first_author_last_name']
    doi_link = article['doi_link']
    
    # Map keywords to topic-specific hashtag
    if any(keyword in article['keywords'] for keyword in ["Echo", "Echocardiography", "Cardiac Echo", "Ultrasound"]):
        topic_hashtag = "#EchoFirst"
    elif any(keyword in article['keywords'] for keyword in ["CT", "Computed Tomography", "Cat Scan", "CT Scan"]):
        topic_hashtag = "#YesCCT"
    elif any(keyword in article['keywords'] for keyword in ["PET", "Nuclear", "Nuclear Medicine", "MPI", "SPECT", "Myocardial Perfusion", "Myocardial Perfusion Imaging"]):
        topic_hashtag = "#ThinkPET #CVNuc"
    elif any(keyword in article['keywords'] for keyword in ["CMR", "Cardiac MRI", "MRI", "Magnetic Resonance", "Cardiac Magnetic Resonance"]):
        topic_hashtag = "#WhyCMR"
    else:
        topic_hashtag = "#CVImaging"
    
    twitter_handles = ("@ The #IJCVI ⭐ @chrisgraeni @RaberLorenz @domcbenz @AnnaGiuliaPavon "
                       "@SheilaHegde @ShehabAnwer @CE_Guerreiro @ARrosendael @isaacshiri "
                       "@MarcoGuglielmo @EdoardoConte16 @BFoldyna @albcipri6 #CardioX")
    
    first_line_templates = [
        f"🚀 Exploring {title} - {first_author_last_name} et al. provide insights on:",
        f"🔍 {title} by {first_author_last_name} et al. highlights:",
        f"🌟 Discover key findings in {title} - presented by {first_author_last_name} et al.:",
        f"📊 New perspectives in {title}, shared by {first_author_last_name} et al.:",
        f"💡 {first_author_last_name} et al. on {title}:"
    ]
    post_message = f"{random.choice(first_line_templates)} {doi_link}"
    post_footer = f"{topic_hashtag} {twitter_handles}"
    post_text = f"{post_message}\n\n{post_footer}"

    return post_text

# Step 3: Generate Color Palette Image and Encode to Base64
def generate_palette_image():
    width, height = 800, 400
    section_height = height // len(colors)
    palette_image = Image.new("RGB", (width, height), colors["Ivory"])
    draw = ImageDraw.Draw(palette_image)
    
    y_start = 0
    for color_name, hex_code in colors.items():
        draw.rectangle([0, y_start, width, y_start + section_height], fill=hex_code)
        label_color = colors["Ivory"] if color_name in ["Dark Red", "Bright Red", "Deep Maroon", "Dark Charcoal"] else colors["Dark Charcoal"]
        draw.text((10, y_start + section_height // 2 - 10), f"{color_name} ({hex_code})", fill=label_color)
        y_start += section_height
    
    buffered = io.BytesIO()
    palette_image.save(buffered, format="PNG")
    base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{base64_image}"

def generate_html(articles, base64_image):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>The #IJCVI Codex Operum</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
            .post {{ margin: 20px 0; padding: 15px; border: 1px solid #ccc; border-radius: 8px; }}
            .post img {{ max-width: 100%; margin-top: 10px; }}
            .post-text {{ font-size: 16px; margin-top: 10px; color: blue; }}
            h3, h4 {{ margin: 10px 0; font-size: 1.1em; }}
            p {{ margin: 5px 0; }}
            .button-row {{ display: flex; gap: 10px; margin-top: 10px; }}
            .copy-button {{ background-color: #4CAF50; color: white; padding: 5px 10px; border: none; cursor: pointer; border-radius: 5px; }}
            .copy-button:hover {{ background-color: #45a049; }}
        </style>
        <script>
            function copyToClipboard(content, message) {{
                navigator.clipboard.writeText(content).then(function() {{
                    alert(message + ' copied to clipboard!');
                }}).catch(function(err) {{
                    console.error('Could not copy text: ', err);
                }});
            }}
        </script>
    </head>
    <body>
        <h1>The #IJCVI Codex Operum</h1>
        <div><img src="{base64_image}" alt="Color Palette"></div>
    """
    
    for idx, article in enumerate(articles):
        post_text = prepare_post_text(article)
        first_author_linkedin = f"https://www.linkedin.com/search/results/people/?keywords={article['first_author'].replace(' ', '%20')}"
        last_author_linkedin = f"https://www.linkedin.com/search/results/people/?keywords={article['last_author'].replace(' ', '%20')}"
        first_author_x = f"https://x.com/search?q={article['first_author'].replace(' ', '%20')}&f=user"
        last_author_x = f"https://x.com/search?q={article['last_author'].replace(' ', '%20')}&f=user"

        html_content += f"""
        <div class="post">
            <h3>Information</h3>
            <p><strong>Access:</strong> {article['access']}</p>
            <h4>Category</h4>
            <p>{article['keywords']}</p>
            <h4>Date</h4>
            <p>{article['publication_date']}</p>
            <h4>First Author</h4>
            <p>{article['first_author']}</p>
            <div class="button-row">
                <button class="copy-button" onclick="window.open('{first_author_linkedin}', '_blank')">First Author LinkedIn</button>
                <button class="copy-button" onclick="window.open('{first_author_x}', '_blank')">First Author X</button>
            </div>
            <h4>Last Author</h4>
            <p>{article['last_author'] if article['last_author'] else 'None'}</p>
            <div class="button-row">
                <button class="copy-button" onclick="window.open('{last_author_linkedin}', '_blank')">Last Author LinkedIn</button>
                <button class="copy-button" onclick="window.open('{last_author_x}', '_blank')">Last Author X</button>
            </div>
            <h4>The Post</h4>
            <div class="post-text" id="postText{idx}">{post_text}</div>
            <div class="button-row">
                <button class="copy-button" onclick="copyToClipboard(document.getElementById('postText{idx}').innerText, 'Post Text')">Copy Post Text</button>
                <button class="copy-button" onclick="copyToClipboard('{article['doi_link']}', 'DOI Link')">Copy DOI Link</button>
            </div>
            <img src="{article['image_url']}" alt="Article Image">
            <div class="button-row">
                <button class="copy-button" onclick="copyToClipboard('{article['image_url']}', 'Media Link')">Copy Media Link</button>
            </div>
        </div>
        """
    
    html_content += "</body></html>"
    
    with open("generated_posts.html", "w") as file:
        file.write(html_content)
    print("HTML file 'generated_posts.html' has been generated successfully.")

# Main function
def main():
    base_url = 'https://link.springer.com/search?new-search=true&facet-journal-id=10554&query=*&content-type=article&date=custom&dateFrom=2024&dateTo=&sortBy=newestFirst'
    articles = fetch_articles(base_url)
    base64_image = generate_palette_image()
    generate_html(articles, base64_image)

main()