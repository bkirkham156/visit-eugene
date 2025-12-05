**Visit Eugene - Personalized Local Guide**
_A Streamlit web app for exploring food, activities, and hidden gems in Eugene, Oregon_

**Overview**

Visit Eugene is a data-driven web application built with Python, Streamlit, and SQLite.
The goal is to give students, locals, and visitors an easy way to explore the best places to eat, study, hang out, and enjoy Eugene’s unique culture.

This project was created for CS 407 Seminar (Winter 2025) at the University of Oregon and serves as a hands-on introduction to software product development, database design, and interactive web apps.

**Features**

- _Explore Eugene_: Browse from restaurants, cafes, parks, hikes, bars, and more
   - Places are stored in a structured SQLite database and loaded into the web application with Pandas. 
- _Filter & Recommend_: Filter by interests (e.g., Food, Coffee, Nature, Nightlife), budget ($, $$, $$$), and vibe (chill, lively, scenic, etc.).
   - "Top Picks" section ranks places by rating.
   - Query results update automatically based on user selections.
- _Vibe Quiz_:
   - What kind of energy are you looking for?
   - What is your budget?
   - What do you want to do?
   - Quiz answers are mapped to internal filters and used to generate a tailored set of spot so that users don't need to adjust manual filters.

**Project Structure**

app/main.py              # Main Streamlit interface

data/eugene.db           # SQLite database

data/places_seed.csv     # Seed data

scripts/seed_db.py       # Reseeds the database

utils.py                 # Filtering & loading helpers

requirements.txt         # Dependencies

**Getting Started**

1. Clone the repo:
   - git clone https://github.com/YOUR-USERNAME/visit-eugene.git
   - cd visit-eugene
2. Install dependencies:
   - pip install -r requirements.txt
3. Seed the database:
   - python scripts/seed_db.py
4. Run the app
   - streamlit run app/main.py

**Technologies Used**
- Python 3
- CSS
- HTML
- Streamlit -> interactive web UI
- SQLite -> local databse for places and metadata
- Pandas -> data loading and filtering
- Plotly -> charts for insights

**Future Improvements**
- Add more places and richer tags (time of day, study-friendly, size of group)
- Improve graphics and color scheme + add photos for each location
- Refine itinerary logic
- Add simple username + password so users can save favorite spots/itineraries

**Brynn Kirkham**

_University of Oregon_

CS 407 Seminar - Fall 2025
