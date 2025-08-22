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


🔄 Data Workflow:

* 🌐 Scraper → Fetches books with Requests & BeautifulSoup

* 🛡️ Validation → Pydantic ensures clean data

* 🗄️ Database → SQLAlchemy stores records in PostgreSQL

* ⚡ API → FastAPI exposes CRUD endpoints

* 📡 Client → Consumes results via JSON


🧩 Example Use Case:

* Archive book data 📚

* Compare books across multiple pages 🔄

* Build a search/filter system 🔎

* Learn modern stack → FastAPI + PostgreSQL + Docker 🚀


🧑‍💻 Development:

Run locally without Docker:

    uvicorn app.main:app --reload

Run tests (if added):

    pytest


📸 Screenshots:

* Swagger UI demo (/docs)
<img width="1913" height="955" alt="Screenshot 2025-08-20 155324" src="https://github.com/user-attachments/assets/5f47597f-f1c7-49d7-adff-96c3705e1f08" />
<img width="1136" height="734" alt="Screenshot 2025-08-20 155854" src="https://github.com/user-attachments/assets/c5cb1027-d7ab-4c10-be42-2526e37a65cb" />
<img width="1054" height="687" alt="Screenshot 2025-08-20 155907" src="https://github.com/user-attachments/assets/823ffc8f-4884-417a-bbc5-2bf6e1ac6efd" />
<img width="1110" height="804" alt="Screenshot 2025-08-20 155925" src="https://github.com/user-attachments/assets/a6f64b48-0068-4ed9-ac56-9c01417f56e4" />
<img width="1064" height="747" alt="Screenshot 2025-08-22 165116" src="https://github.com/user-attachments/assets/e23a4cfb-dd01-4806-8a1a-ab84216e3874" />


* Example JSON response
<img width="1054" height="629" alt="Screenshot 2025-08-22 165417" src="https://github.com/user-attachments/assets/8f8948fe-7075-4dc4-bbd1-c6908c78fa95" />
<img width="1056" height="852" alt="Screenshot 2025-08-22 165644" src="https://github.com/user-attachments/assets/20d3da23-8842-4a8d-a767-5473e5411cd0" />
<img width="1055" height="635" alt="Screenshot 2025-08-22 165800" src="https://github.com/user-attachments/assets/3ac7754e-89a8-4619-9169-e97158b0211e" />
<img width="1053" height="568" alt="Screenshot 2025-08-22 165855" src="https://github.com/user-attachments/assets/c630daf4-8f00-4e87-80ad-ea993910e4bd" />
<img width="1053" height="589" alt="Screenshot 2025-08-22 165945" src="https://github.com/user-attachments/assets/93f765ff-f84f-43a1-a04e-c3c692abc5a0" />


💡 Conclusion:

* This project demonstrates an end-to-end workflow:
* from scraping external data → validating → storing in a database → exposing via API.
* It’s simple, extensible, and a great starting point for more advanced scraping + API projects.

✨ Made with ❤️ using FastAPI + PostgreSQL + Docker ✨
