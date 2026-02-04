import re

def create_slug(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text

def generate_unique_slug(cursor, title):
    base_slug = create_slug(title)
    slug = base_slug
    counter = 1
    while True:
        cursor.execute("SELECT 1 FROM blogs WHERE slug = ? LIMIT 1", (slug,))
        if cursor.fetchone() is None:
            return slug
        slug = f"{base_slug}-{counter}"
        counter += 1