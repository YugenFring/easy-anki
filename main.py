from anki.loader import json_loader
from anki.loader import str2time
from anki.loader import time2str
from anki.db import Cards
from anki import algo
from datetime import datetime, timedelta

import time

if __name__ == "__main__":
    cards_db = Cards()

    while True:
        card = cards_db.get_random_card()
        card = dict(card)
        print(f"Q: {card['translated_content']}({card['explanation']})")

        start_time = time.time()
        answer = input('A: ')
        end_time = time.time()
        answer_duration = end_time - start_time

        original_content = card['original_content']
        similarity = algo.compare_sentences(answer, original_content)
        success = 1 if similarity > 0.85 else 0
        card['test_times'] += card['test_times'] + 1
        card['success_times'] += card['success_times'] + success
        print(
            f"R: {original_content}{card['romaji_content']}({similarity * 100:.2f}%)")
        print()

        review_date = datetime.now()
        last_review_date = str2time(card['last_review_date'])
        card['last_review_date'] = time2str(review_date)
        current_strength = card['memory_strength']
        new_memory_strength = algo.calculate_memory_strength(
            review_date, last_review_date, current_strength)
        card['memory_strength'] = round(new_memory_strength, 2)

        ease_factor = card['ease_factor']
        new_ease_factor = algo.update_ease_factor(ease_factor, 10)
        card['ease_factor'] = round(new_ease_factor, 2)

        next_review_date = str2time(card['next_review_date'])
        expected_interval = next_review_date - last_review_date
        real_interval = review_date - last_review_date
        current_interval = expected_interval*0.62 + real_interval*0.38
        current_interval = current_interval.total_seconds() / (24 * 3600)
        success_rate = card['success_times'] / (card['test_times']+0.00001)
        new_interval = algo.calculate_review_interval(
            current_interval, new_ease_factor, new_memory_strength, success_rate)
        new_review_date = next_review_date + timedelta(days=new_interval)
        card['next_review_date'] = new_review_date

        cards_db.update_card(card)
