from app import app 
from models import db, Album
from datetime import date, datetime, timedelta
import random


def seed_unique_release_dates():
    with app.app_context():  # Ensure the context covers all operations
        albums = Album.query.all()  # Fetch all albums
        used_dates = set()  # To avoid duplicate dates

        for album in albums:
            while True:
                # Generate a random date between 1980 and 2025
                random_date = date.fromtimestamp(
                    random.randint(
                        int(datetime(1980, 1, 1).timestamp()),
                        int(datetime(2025, 1, 1).timestamp())
                    )
                )
                if random_date not in used_dates:  # Ensure the date is unique
                    used_dates.add(random_date)
                    album.release_date = random_date
                    break

        db.session.commit()  # Save changes to the database
        print(f"Seeded {len(albums)} albums with random unique release dates.")

if __name__ == "__main__":
    seed_unique_release_dates()
