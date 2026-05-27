import sqlite3


class DatabaseManager:

    def __init__(self, db_name="data.db"):

        self.conn = sqlite3.connect(db_name)

        self.cursor = self.conn.cursor()

    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            views INTEGER,
            likes INTEGER,
            dislikes INTEGER,
            userId INTEGER
        )

        """)

        self.conn.commit()

    def insert_posts(self, posts):

        query = """

        INSERT OR REPLACE INTO posts(

            id,
            title,
            content,
            views,
            likes,
            dislikes,
            userId

        )

        VALUES (?, ?, ?, ?, ?, ?, ?)

        """

        values = [
            (
                post["id"],
                post["title"],
                post["content"],
                post["views"],
                post["likes"],
                post["dislikes"],
                post["userId"],
            )
            for post in posts
        ]

        self.cursor.executemany(query, values)

        self.conn.commit()

    def fetch_all_posts(self):

        self.cursor.execute("""

        SELECT * FROM posts

        """)

        return self.cursor.fetchall()

    def close(self):

        self.conn.close()
