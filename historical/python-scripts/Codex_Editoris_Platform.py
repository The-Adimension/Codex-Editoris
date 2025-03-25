import requests
from urllib.parse import quote
import random
import re

# API URL
url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=JOURNAL:"Europace"&resultType=core&pageSize=500&sort=P_PDATE_D desc&format=json'

# Fetch data from the API
print("Fetching data from API...")
response = requests.get(url)
print("Response received with status code:", response.status_code)
data = response.json()

# Extract relevant article details
articles = data.get('resultList', {}).get('result', [])
print(f"Number of articles fetched: {len(articles)}")

def generate_social_media_post(title, first_author_lastname):
    """
    Generate an engaging, professional, and scientific social media post.

    Args:
        title (str): The title of the article.
        first_author_lastname (str): The last name of the first author.

    Returns:
        str: A generated social media post.
    """
    templates = [
        f"'{title}' by {first_author_lastname} et al. brings a fresh perspective to #CVImaging. Read it now in #Europace!",
        f"Explore '{title}' by {first_author_lastname} et al., redefining innovation in cardiovascular research. Discover more in #Europace.",
        f"'{title}'—an essential read from {first_author_lastname} et al., showcasing cutting-edge science in #Europace!",
        f"Innovative research alert: '{title}' by {first_author_lastname} et al. is now available in #Europace.",
        f"Leading the way in #CVImaging: '{title}' by {first_author_lastname} et al., featured in #Europace.",
        f"Explore '{title}', the latest in groundbreaking research by {first_author_lastname} et al. Read it in #Europace!",
        f"Don't miss the study '{title}' by {first_author_lastname} et al., a key contribution to cardiovascular science. Now in #Europace!",
        f"{first_author_lastname} et al. present impactful findings in '{title}'. Read this important study in #Europace.",
        f"New in #Europace: '{title}' by {first_author_lastname} et al., offering novel insights into imaging science.",
        f"Highlighting '{title}'—{first_author_lastname} et al. reveal transformative discoveries in #Europace.",
        f"Discover how '{title}' by {first_author_lastname} et al. is shaping the future of imaging research. Read in #Europace!",
        f"Exciting research from {first_author_lastname} et al.: '{title}' explores new dimensions in #CVImaging. Featured in #Europace.",
        f"Explore the paradigm-shifting study '{title}' by {first_author_lastname} et al., now in #Europace!",
        f"'Revolutionizing #CVImaging: {first_author_lastname} et al. unveil '{title}' in #Europace.",
        f"Stay at the forefront of cardiovascular science: Read '{title}' by {first_author_lastname} et al., now in #Europace!"
        f"Discover cutting-edge insights in '{title}'. {first_author_lastname} et al. present their latest findings in #Europace!",
        f"The latest research by {first_author_lastname} et al. explores '{title}'. Dive deeper in #Europace!",
        f"Explore the groundbreaking study '{title}' by {first_author_lastname} et al., now featured in #Europace.",
        f"Exciting developments in #CVImaging: '{title}' by {first_author_lastname} et al. Read more in #Europace!",
        f"'{title}'—a must-read study by {first_author_lastname} et al., pushing the boundaries of knowledge in #Europace!",
        f"Delve into the latest advancements in '{title}'. {first_author_lastname} et al. share groundbreaking findings in #Europace!",
        f"New insights unveiled by {first_author_lastname} et al. in '{title}'. Discover the details in #Europace!",
        f"Check out the innovative study '{title}' by {first_author_lastname} et al., now spotlighted in #Europace.",
        f"Significant strides in #CVImaging: '{title}' authored by {first_author_lastname} et al. Explore more in #Europace!",
        f"'{title}'—a pivotal contribution by {first_author_lastname} et al., expanding horizons in #Europace!",
        f"Uncover pioneering research in '{title}' by {first_author_lastname} et al. Read more in #Europace!",
        f"Discover how {first_author_lastname} et al. are advancing the field with '{title}', now featured in #Europace.",
        f"The study '{title}' by {first_author_lastname} et al. offers fresh perspectives in #CVImaging. Explore it in #Europace!",
        f"Breaking new ground in imaging science: '{title}' by {first_author_lastname} et al., highlighted in #Europace.",
        f"Transformative research '{title}' by {first_author_lastname} et al. is shaping the future of #CVImaging. Learn more in #Europace!",
        f"New research in #Europace: '{title}' by {first_author_lastname} et al.",
        f"Latest insights: '{title}' by {first_author_lastname} et al. in #Europace",
        f"Read '{title}' by {first_author_lastname} et al. in #Europace now!",
        f"Latest #Europace findings in '{title}' by {first_author_lastname} et al.",
        f"Exciting study! '{title}' by {first_author_lastname} et al. in #Europace.",
        f"Breakthrough research: '{title}' by {first_author_lastname} et al. in #Europace!",
        f"Big news! '{title}' by {first_author_lastname} et al. just published in #Europace.",
        f"Don’t miss '{title}' by {first_author_lastname} et al., now in #Europace!",
        f"Game-changing study: '{title}' by {first_author_lastname} et al. in #Europace.",
        f"Just in: '{title}' by {first_author_lastname} et al. in #Europace!",
        f"Must-read: '{title}' by {first_author_lastname} et al. in #Europace.",
        f"Fresh insights! '{title}' by {first_author_lastname} et al. in #Europace.",
        f"Check out '{title}' by {first_author_lastname} et al. in #Europace!",
        f"Curious about imaging? Read '{title}' by {first_author_lastname} et al. in #Europace.",
        f"New perspectives: '{title}' by {first_author_lastname} et al. in #Europace.",
        f"How will '{title}' by {first_author_lastname} et al. impact imaging? Read in #Europace.",
        f"'{title}' by {first_author_lastname} et al. offers key insights—#Europace.",
        f"New advances in imaging: '{title}' by {first_author_lastname} et al. in #Europace.",
        f"Discover new perspectives in '{title}' by {first_author_lastname} et al.—#Europace.",
        f"'{title}' by {first_author_lastname} et al. challenges norms. Read in #Europace!",
        f"Let’s discuss '{title}' by {first_author_lastname} et al. in #Europace!",
        f"Thoughts on '{title}' by {first_author_lastname} et al.? Read in #Europace.",
        f"Join the conversation: '{title}' by {first_author_lastname} et al. in #Europace.",
        f"Share your views on '{title}' by {first_author_lastname} et al. in #Europace!",
        f"What do you think of '{title}' by {first_author_lastname} et al.? #Europace.",
        f"New in #Europace: '{title}' by {first_author_lastname} et al.",
        f"Read '{title}' by {first_author_lastname} et al. in #Europace.",
        f"Now in #Europace: '{title}' by {first_author_lastname} et al.",
        f"Major update! '{title}' by {first_author_lastname} et al. in #Europace.",
        f"Breaking new ground: '{title}' by {first_author_lastname} et al. #Europace.",
        f"Key findings alert! '{title}' by {first_author_lastname} et al. #Europace.",
        f"Big strides in imaging: '{title}' by {first_author_lastname} et al. #Europace.",
        f"Now published: '{title}' by {first_author_lastname} et al. #Europace.",
        f"Fresh off the press: '{title}' by {first_author_lastname} et al. #Europace."
        f"New research alert: '{title}' by {first_author_lastname} et al. brings valuable insights to #Europace.",
        f"The latest contribution to #CVImaging: '{title}' by {first_author_lastname} et al. in #Europace.",
        f"'{title}', authored by {first_author_lastname} et al., is now available in #Europace. A significant step forward!",
        f"Examine the groundbreaking findings in '{title}' by {first_author_lastname} et al., now published in #Europace.",
        f"Exciting developments in #CVImaging! '{title}' by {first_author_lastname} et al. is now in #Europace.",
        f"Don't miss this transformative study: '{title}' by {first_author_lastname} et al. Read it in #Europace!",
        f"Major progress in the field! '{title}' by {first_author_lastname} et al. is making an impact in #Europace.",
        f"A must-read for imaging enthusiasts! '{title}' by {first_author_lastname} et al. is now available in #Europace.",
        f"Looking for the latest in #CVImaging? '{title}' by {first_author_lastname} et al. is now in #Europace!",
        f"What’s new in imaging? '{title}' by {first_author_lastname} et al. is now live in #Europace—check it out!",
        f"Curious about the future of #CVImaging? '{title}' by {first_author_lastname} et al. is a must-read in #Europace!",
        f"Here's an exciting read for you! '{title}' by {first_author_lastname} et al. just dropped in #Europace.",
        f"How will '{title}' by {first_author_lastname} et al. reshape #CVImaging? Explore in #Europace!",
        f"Advancing the frontier: '{title}' by {first_author_lastname} et al. paves new paths in #CVImaging. Read in #Europace.",
        f"'{title}' by {first_author_lastname} et al. presents findings that could change the way we see #CVImaging. Dive in via #Europace!",
        f"Another leap in #CVImaging research: '{title}' by {first_author_lastname} et al. is a must-read in #Europace.",
        f"Big news in #CVImaging! '{title}' by {first_author_lastname} et al. is in #Europace.",
        f"Key findings from '{title}' by {first_author_lastname} et al. now published in #Europace.",
        f"Exciting research ahead! '{title}' by {first_author_lastname} et al. is featured in #Europace.",
        f"Breakthrough insights: '{title}' by {first_author_lastname} et al. is now in #Europace.",
        f"Let’s discuss! '{title}' by {first_author_lastname} et al. offers key insights in #Europace. Thoughts?",
        f"What do you think about '{title}' by {first_author_lastname} et al.? Read it now in #Europace and share your views!",
        f"Join the conversation on '{title}' by {first_author_lastname} et al., now in #Europace. Let’s explore the findings together!"
    ]
    return random.choice(templates)

html_content = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=0.8">
    <title>The Adimension Codex Editoris | Europace</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.2;
            margin: 5px;
            padding: 15px;
        }
        .article {
            margin-top: 15px;
            margin-bottom: 15px;
            padding: 20px;
            border-radius: 0;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5), -5px -5px 15px rgba(255, 255, 255, 0.7);
        }
        h1 {
            color: #006989;
            padding: 0px;
            margin-bottom: 10px;
            font-size: 1.8em;
            font-weight: bold;
        }
        h2 {
            color: #006989;
            margin: 0;
            padding: 10px;
            font-size: 1.2em;
        }
        .button-download {
            margin: 10px;
            background-color: #b30018;
            margin: 5px;
            padding: 5px;
            border-radius: 0;
            text-decoration: none;
            color: white;
            font-size: 0.9em;
            white-space: nowrap;
            cursor: pointer;
        }
        .details, .meta {
            margin: 10px;
            font-size: 0.9em;
            color: #555;
            padding: 5px;
        }
        .meta {
            display: flex;
            padding: 5px;
            gap: 15px;
            flex-wrap: wrap;
        }
        .meta strong {
            font-weight: bold;
        }
        .author-row {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            flex-wrap: nowrap;
            padding: 5px;
            margin: 5px;
        }
        .author-name {
            white-space: nowrap;
        }
        .button {
            background-color: #b30018;
            padding: 5px;
            text-decoration: none;
            color: black;
            font-size: 0.9em;
            white-space: nowrap;
            cursor: pointer;
        }
        .linkedin {
            background-color: #0077b5;
            padding:5px;
            color: white;
            cursor: pointer;
        }
        .x-button {
            background-color: #000;
            padding: 5px;
            color: white;
            cursor: pointer;
        }
        .open-access {
            background-color: #d4edda;
            color: #155724;
            padding: 5px;
            border-radius: 4px;
            font-size: 0.8em;
            display: inline-block;
            margin: 5px;
        }
        .copy-button {
            background-color: #b30018;
            color: white;
            font-weight: bold;
            padding: 5px;
            border: none;
            cursor: pointer;
        }
        a {
            color: #b30018;
            text-decoration: underline;
        }
        .abstract-header {
            font-weight: bold;
            display: inline;
            margin: 0;
            color: #006989;
        }
        .abstract-content {
            margin: 10px;
            padding: 10px;
            display: inline;
            font-size: 0.8em;
        }
        .abstract-container {
            background-color: #f5f5f5;
            padding: 10px;
            margin-top: 10px;
            font-size: 0.8em;
        }
        .cc-container {
            background-color: transparent;
            margin-top: 20px;
            margin-bottom: 20px;
            font-size: 0.7em;
        }
        .embed-container {
            display: flex;
            gap: 5px;
            margin: 5px;
        }
        .embed-container > div {
            flex: 1;
            padding: 5px;
            background-color: transparent;
        }
        .social-post {
            background-color: transparent;
            padding: 10px;
            margin: 5px;
            font-size: 1em;
            color: #006989;
            border: 1px gray;
            font-weight: bold;
            transition: transform 0.8s ease-in-out; /* smooth transition for scaling */
        }
        .social-post:hover {
            transform: scale(1.01);
        }
        .full-container {
            background-color: transparent;
            padding: 20px;
            margin: 15px;
            font-size: 1em;
            color: #006989;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5), -5px -5px 15px rgba(255, 255, 255, 0.7);
        }
        .editors-container {
            background-color: transparent;
            padding: 20px;
            margin: 15px;
            font-size: 1em;
            color: #006989;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5), -5px -5px 15px rgba(255, 255, 255, 0.7);
            transition: transform 0.8s ease-in-out; /* smooth transition for scaling */
        }
        .editors-container:hover {
            transform: scale(1.01);
        }
        .search-container {
            margin: 10px;
        }
        .search-container input {
            margin: 3px;
            padding: 5px;
            font-size: 1em;
        }
        .search-container button {
            margin-top: 10px;
            margin-bottom: 10px;
            background-color: #006989;
            padding: 5px;
            font-size: 0.9em;
            color: white;
            font-weight: bold;
            cursor: pointer;
            border: none;
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
    <script type="text/javascript" src="//cdn.plu.mx/widget-popup.js"></script>
</head>
<body>
    <h1>The Adimension Codex Editoris | Europace </h1>
    <p><strong>To AïA</strong> | S. Anwer - Codex Editoris © The Adimension 2025.<br></p>
    <div><br>Watch <strong><a href="https://www.theadimension.ch/Codex-Editors/EHJ-VideoGuide.html" target="_blank">the Adimension Codex Editoris video guide.</a></strong><br>
    <div class="article">Thanks to <strong>@Iva @Alex @Aldo @HyloMorph @Ender  @Ali @Chris @Boldi @Edoardo @Ruben @Steffen @Victoria @Robert @Ayman @Valeria @Mahmoud @Amidos @Hany @William @Helmut @Lutz @Nazar @Diana @Bohdan @Alexey @Julia @Milena @Lavinia @Alessia @Alexandros @Georgia & @Ioulia.</strong></div>
    <div class="article"><strong>Disclaimer:</strong> <br>Digital metrics badges copyrights<br> Dimensions.ai © 2025 Digital Science & Research Solutions Inc.    |    Altmetrics © 2024 Altmetric Limited.    |    PlumX © 2025 Plum Analytics.
    </div>
    <div class="article">
        <p id="x-accounts-editors">#Epeeps @EuropaceEiC @BorianiGiuseppe @EHRAPresident @purerfellner @escardio @ESC_Journals @OUPMedicine</p>
        <button class="copy-button" onclick="copyToClipboard(document.getElementById('x-accounts-editors').textContent)">Copy Editors @ X</button>
    </div>
    <div class="article">
        <p id="LIN-accounts-editors">@breitensteinale @BoldiKovacsMD @AndreasMetzner7 @ASaguner @GerdHindricks @AndreasRillig @AndyZhangMD @AstridHermans @BehrElijah @BetzKonstanze @CarolRemme @ChristianHeeger @DanielScherr3 @DavidDuncker @Dominik_Linz @Drdevignair @EmmaSvennberg @FraSantoroMD @GiulioConte9 @HFA_President @HRSonline @HaranBurri @JordiHeijman @KantersjK @LAHRSonline1 @LuigiDiBiaseMD @MBergonti @MMOliveira50 @MaastrichtUMC @NazemAkoum @OdeningLab @Phiso_de @PrashSanders @S_NarayanMD @True_EP @UCPH_Research @UliSchotten @VivekReddyMD @atulverma_md @fleurtjong @ftrae @gasperettimd @joselmerino @kvernooy @laura_rottner @livio81 @marcovitoloMD @natale_md @netta_doc @simovicst</p>
        <button class="copy-button" onclick="copyToClipboard(document.getElementById('LIN-accounts-editors').textContent)">Copy add'l accounts @ X</button>
    </div>
        <div class="article">
        <p id="LIN-accounts-editors">EHRA President - Helmut Pürerfellner - Breitenstein Alexander - Dr. med. Boldizsar Kovacs MSc - Ruben Casado Arroyo - Angelo Auricchio - Christian-H. Heeger - Maxim Didenko, MD - Giuseppe Uccello - Khaled Al-Otaibi - Petr Peichl - Andi Haziq - Philipp Sommer - K.R. Julian Chun - Roland Tilz - Christian Veltmann - Andreas Metzner - Andreas Rillig - Paulus Kirchhof - Dr. Sebastian Feickert - Laura Rottner - Sabine Ernst - Dominik Linz - Cheryl Teres MD, PhD - Michiel Rienstra - Harry Crijns - Tom De Potter - Prof. Dr. Thorsten Hanke - Tiny Jaarsma - Prashanthan Sanders - Emma Svennberg - Vassil Traykov - Stylianos Tzeis - Prof. Dr. David Duncker - Evgeny Lyan - Daniel Steven - Arian Sultan - Borislav Dinov - Serge Boveda - Carlo Pappone - Fengwei Zou - Luigi Di Biase, MD, PhD, FACC, FHRS - Xiaodong Zhang - Vito Grupposo - Francis MISCHLER - Julia Vogler - Helmut Weber - Simon Kraler - Bart Maesen - Patricia Kennedy - Dr. Amir Esfandi - Lucia Osoro - Jan de Pooter - Stephan Ensminger - Prof. Dr. Ingo Eitel - Calvanese Raimondo - Dr. Devi G Nair, MD, FACC, FHRS - Henry Huang - Christian Sticherling - Laurent Roten - Graziana Viola - Laura Perrotta - Kars Neven MD PhD - Alexandre Almorad - Gian Battista Chierchia - Jakub Baran - PD Dr. Shibu Mathew - Sergio Conti - Dhiraj Gupta - Daniel Scherr - Yvonne Greipl - Frank Eiben - Prof. Dr. Gerhard Hindricks - PD Dr. Nikolaos Dagres - Mark Petrie - Frederic Sacher - Raphael MARTINS - Antonio Frontera - Finn Gustafsson - Matteo Pagnesi - Philippe Maury - Marta deRiva - Marisa Crespo-Leiro - Ovidiu Chioncel - Antoni Bayes-Genis - Thomas Deneke - Offer Amir - Susana Santos Iglesias - Adam Danish - Giulio Conte MD, PhD - Giuseppe Boriani - Nicolas Schärli </p>
        <button class="copy-button" onclick="copyToClipboard(document.getElementById('LIN-accounts-editors').textContent)">Copy accounts @ LinkedIn</button>
    </div>
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
        x_link = f'https://twitter.com/search?q={quote(full_name)}'

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
        <div>
            <a href="{pdf_url}" target="_blank" class="button-download">Download PDF if PMCID is assigned</a>
        </div>
        <div class="meta">
            {'<span class="open-access">Open Access</span>' if is_open_access else ''}
            <strong>Issue</strong> {issue} <strong>Vol</strong> {volume} <strong>Published on</strong> {pub_date} <strong>PMID</strong> {pmid} <strong>PMCID</strong> {pmcid}
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
            <strong>Social Media Post:</strong><br>
            {social_post} <button class="copy-button" onclick="copyToClipboard(`{social_post}`)">Copy Text</button>
        </div>
        <div class="embed-container">
            <div>
                <span class="__dimensions_badge_embed__" data-pmid="{pmid}" data-legend="always"></span>
                <script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
            </div>
            <div>
                <div data-badge-details="right" data-badge-type="medium-donut" data-doi="{doi}" data-legend="always" data-condensed="true" data-hide-no-mentions="false" class="altmetric-embed"></div>
            </div>
            <div class="embed-container">
            <a href="https://plu.mx/plum/a/?doi={doi}" data-popup="top" data-badge="true" class="plumx-plum-print-popup" data-site="plum"><svg viewBox="0 0 100 100" width="75" height="75"><path fill="#6e1a62" stroke="#6e1a62" stroke-width="1" d="M 36.075524746876404,57.96956599135724 C 47.24224000477168,47.68596460512846 53.05297314616313,51.90770935123954 46.72339182284403,65.70569425459581 L 53.27660817715597,65.70569425459581 C 46.94702685383687,51.90770935123954 54.11916130196383,46.54361327076243 66.73225377367403,64.96794365950129 L 72.33461419729612,47.7256512143974 C 51.300858350195114,55.217457868193435 48.651416263702714,46.662138123559565 61.88240715909315,39.21976840364822 L 56.58074376063895,35.36788447550181 C 53.59123058093537,50.25112330547885 45.221755705838305,50.334127390178 44.7288145302294,30.470688282908622 L 33.05540672336235,38.951915501347315 C 51.79433272187257,45.55887066943854 49.12908117584119,53.493064614593585 34.05046952557818,51.73708687489691 Z"></path><circle fill="#6e1a62" stroke="#6e1a62" stroke-width="1" r="4" cx="32.880982706687234" cy="55.56230589874905"></circle><circle fill="#6e1a62" stroke="#6e1a62" stroke-width="1" r="4" cx="50" cy="68"></circle><circle fill="#c43bf3" stroke="#6e1a62" stroke-width="1" r="11.066089190457772" cx="75.57002555852411" cy="58.30820493714331"></circle><circle fill="none" stroke="#ffffff" stroke-width="1.5" r="9.566089190457772" cx="75.57002555852411" cy="58.30820493714331"></circle><circle fill="#6e1a62" stroke="#6e1a62" stroke-width="1" r="4" cx="60.58013454126452" cy="35.43769410125095"></circle><circle fill="#fd5704" stroke="#6e1a62" stroke-width="1" r="8.807354922057604" cx="35.92280101098581" cy="30.62439782064578"></circle><circle fill="none" stroke="#ffffff" stroke-width="1.5" r="7.307354922057604" cx="35.92280101098581" cy="30.62439782064578"></circle></svg><strong>PLUM X</strong> Metrics</a>
            </div>
        </div>
    </div>
    '''

html_content += '''
</body>
</html>
'''

# Save to an HTML file
output_file = 'Codex_Editoris_Europace.html'
print("Saving the HTML file...")
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f"HTML file '{output_file}' generated successfully.")