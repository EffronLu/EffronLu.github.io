import os
from scholarly import scholarly

# Your Google Scholar ID
SCHOLAR_ID = "EyknLkwAAAAJ"
OUTPUT_DIR = "_publications"
NUM_PUBS = 5

# Create output directory if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Fetch author profile
author = scholarly.fill(scholarly.search_author_id(SCHOLAR_ID), sections=["publications"])

for pub in author['publications'][:NUM_PUBS]:
    pub_filled = scholarly.fill(pub)
    title = pub_filled['bib'].get('title', 'No Title')
    venue = pub_filled['bib'].get('venue', 'Unknown Venue')
    year = pub_filled['bib'].get('pub_year', '2024')
    citation = f"{author['name']}, \"{title}\", {venue}, {year}."
    slug = title[:40].replace(' ', '-').replace(':', '').replace(',', '').lower()
    date_str = f"{year}-01-01"

    content = f"""---
title: \"{title}\"
collection: publications
permalink: /publication/{slug}
date: {date_str}
venue: '{venue}'
paperurl: ''
citation: '{citation}'
---
"""
    filename = f"{date_str}-{slug}.md"
    with open(os.path.join(OUTPUT_DIR, filename), "w") as f:
        f.write(content)

print(f"Updated {NUM_PUBS} publications in '{OUTPUT_DIR}' folder.")
