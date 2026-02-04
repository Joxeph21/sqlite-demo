import sqlite3
from util import generate_unique_slug

def main():
    print("--- Create a Blog Post ---")

    title = input("Title: ").strip()
    content = input("Content: ").strip()
    author = input("Author: ").strip()

    try:
        conn = sqlite3.connect('./blogs.db')
        cursor = conn.cursor()

# Generae the slug using fnc
        slug = generate_unique_slug(cursor, title)

        cursor.execute(
            "INSERT INTO blogs (title, content, author, slug) VALUES (?, ?, ?, ?)",
            (title, content, author, slug)
        )
        conn.commit()

        # Fetch and print all blogs
        cursor.execute("SELECT id, title, slug, author, created_at FROM blogs")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"Failed to create post, {e}")

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()
