# 📚 FastAPI Books Scraper

A full-stack demo project that scrapes books from [Books to Scrape](http://books.toscrape.com/)
, stores them in a PostgreSQL database, and exposes a clean FastAPI-powered REST API.
Everything is fully containerized with Docker & Docker Compose 🚀


✨ Features:

* 🔍 Scraping → Titles, descriptions, and URLs from Books to Scrape
  
* 📄 Pagination → Handles multiple pages automatically
  
* 🗄️ Database → PostgreSQL with SQLAlchemy ORM
  
* ⚡ API → CRUD endpoints built with FastAPI
  
* ✅ Validation → Pydantic for request/response schemas
  
* 🐳 Deployment → Ready-to-run with Docker & Docker Compose


🏗️ Project Architecture:

    app/
    ├── config.py       # Environment variables & settings
    ├── crud.py         # Database CRUD operations
    ├── database.py     # SQLAlchemy engine & session
    ├── main.py         # FastAPI app with endpoints
    ├── models.py       # SQLAlchemy models
    ├── schemas.py      # Pydantic schemas
    ├── scraper.py      # Scraping logic (Requests + BeautifulSoup)
    .env                # Environment variables
    docker-compose.yml  # Orchestration of DB + API
    Dockerfile          # API container build
    requirements.txt    # Python dependencies
    README.md           # Project documentation


⚙️ Technologies Used:

* 🐍 Python 3.10+

* ⚡ FastAPI → Web framework

* 🗄️ SQLAlchemy → ORM

* 🐘 PostgreSQL → Database

* 📦 Docker & Docker Compose → Containerization

* 🌐 Requests + BeautifulSoup → Web scraping

* 🛡️ Pydantic → Data validation


🚀 Setup & Run:

  1️⃣ Clone the repo
  
    git clone https://github.com/your-username/fastapi-books-scraper.git
    cd fastapi-books-scraper

  2️⃣ Copy environment file
  
    cp .env.example .env

  3️⃣ Build & run with Docker Compose
  
    docker-compose up --build

API will be available at 👉 http://localhost:8000

Swagger docs 👉 http://localhost:8000/docs


🛠️ API Endpoints:

| Method | Endpoint         | Description                   |
| :----- |:----------------:| -----------------------------:|
| POST   | /scrape          | Scrape new books (with limit) |
| GET    | /items           | List all books                |
| GET    | /items/{item_id} | Get one book by ID            |
| DELETE | /items/{item_id} | Delete a book by ID           |
 

Example POST /scrape (limit = 5):

    [
      {
        "id": "31e60aa0-06b7-4b46-b0f4-0e9e89b3a5b1",
        "title": "A Light in the Attic",
        "description": "This is a sample description…",
        "url": "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
        "created_at": "2025-08-21T18:35:20.123Z"
      }
    ]





