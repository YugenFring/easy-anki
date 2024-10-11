import sqlite3
from datetime import datetime


class Cards:
    def __init__(self, db_name='memory_cards.db'):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self._create_database()

    def _create_database(self):
        create_sql = """
            CREATE TABLE IF NOT EXISTS cards
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                original_content TEXT,
                romaji_content TEXT,
                translated_content TEXT,
                explanation TEXT,
                test_times INTEGER,
                success_times INTEGER,
                last_review_date TIMESTAMP,
                memory_strength REAL,
                ease_factor REAL,
                next_review_date TIMESTAMP,
                inserted_date TIMESTAMP);
            """
        self.cursor.execute(create_sql)
        self.conn.commit()

    def insert_cards(self, cards):
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_sql = f"""
            INSERT INTO cards (
                type, original_content, romaji_content, translated_content,
                explanation, test_times, success_times, last_review_date,
                memory_strength, ease_factor, next_review_date, inserted_date
                )
            VALUES (?, ?, ?, ?, ?, 0, 0, '{current_date}', 1, 1.3,
            '{current_date}', '{current_date}');
            """
        self.cursor.executemany(insert_sql, cards)
        self.conn.commit()

    def get_random_card(self):
        select_sql = """
            SELECT * FROM(
                SELECT * 
                FROM cards 
                ORDER BY next_review_date 
                LIMIT 3
            )
            ORDER BY RANDOM()
            LIMIT 1;
        """
        self.cursor.execute(select_sql)
        card = self.cursor.fetchone()

        return card

    def update_card(self, card):
        set_clause = ', '.join([f"{key} = ?" for key in card.keys()])
        where_clause = f"id = {card['id']}"

        update_sql = f"UPDATE cards SET {set_clause} WHERE {where_clause};"
        card_values = list(card.values())
        self.cursor.execute(update_sql, card_values)
        self.conn.commit()

    def close(self):
        self.conn.close()
