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












