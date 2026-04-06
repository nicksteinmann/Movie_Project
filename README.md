# Movie App 🎬

## Description

This project is a command-line based Movie Application that allows users to manage a movie database.
It was extended to include a full stack of features including:

* SQL database storage (SQLite with SQLAlchemy)
* External API integration (OMDb API)
* Automatic website generation

The goal of this project is to demonstrate working with databases, APIs, and dynamic content generation.

---

## Features

* 📋 List all movies
* ➕ Add movies via OMDb API (only title required)
* ❌ Delete movies
* ✏️ Update movie ratings
* 📊 View statistics (average, median, best, worst)
* 🎲 Get a random movie
* 🔍 Search movies
* 📉 Sort movies by rating
* 🌐 Generate a website with movie data

---

## Technologies Used

* Python 🐍
* SQLite (via SQLAlchemy)
* OMDb API
* HTML & CSS
* python-dotenv

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/movie-app.git
cd movie-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```text
API_KEY=your_omdb_api_key_here
```

---

## Usage

Run the application:

```bash
python main.py
```

Follow the menu in the terminal.

---

## Generate Website

Use menu option:

```text
9. Generate Website
```

This will create:

```text
index.html
```

Open it in your browser to view your movie collection.

---

## Project Structure

```text
movie-app/ 
│ 
├── data/ 
│   └── movies.db 
│ 
├── storage/ 
│   ├── __init__.py 
│   └── movie_storage_sql.py 
│ 
├── static/ 
│   ├── index_template.html 
│   └── style.css 
│ 
├── main.py 
├── movies.py 
├── requirements.txt 
├── README.md 
├── .gitignore 
└── .env (not tracked)
```

---

## Notes

* The application uses real movie data from the OMDb API
* The `.env` file is excluded from Git for security reasons
* The database is stored locally using SQLite

---

## Author

Nick 🚀
