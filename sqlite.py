import sqlite3

def create_slug(text):
    text = text.lower()
    text = text.replace(' ', '-')
    return text


def generate_unique_slug(cursor, title):
    base_slug = create_slug(title)
    slug = base_slug
    counter = 1

    while True:
        cursor.execute(
            "SELECT 1 FROM blogs WHERE slug = ? LIMIT 1",
            (slug,)
        )
        # Check if a slug exists first
        if cursor.fetchone() is None:
            return slug

# if so add numbers behind
        slug = f"{base_slug}-{counter}"
        counter += 1

# Connecting database
conn = sqlite3.connect('./blogs.db')

# Creating a cursor
cursor = conn.cursor()


# connecting the functon
cursor.execute("SELECT id, title FROM blogs WHERE slug IS NULL")

rows = cursor.fetchall()

for blog_id, title in rows:
    slug = generate_unique_slug(cursor, title)
    cursor.execute(
        "UPDATE blogs SET slug = ? WHERE id = ?",
        (slug, blog_id)
    )

conn.commit()

# ------------------
# Fetch & print result
# ------------------
cursor.execute("SELECT id, title, slug FROM blogs")
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()