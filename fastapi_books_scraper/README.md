# FastAPI Books Scraper

This project is a FastAPI application that scrapes book data from [Books to Scrape](http://books.toscrape.com/) and stores it in a PostgreSQL database.

## Features
- Scrapes book titles, descriptions, and URLs.
- Provides CRUD API endpoints for stored books.
- Containerized with Docker and Docker Compose.

## Setup
1. Copy `.env.example` to `.env` and modify values if needed.
2. Build and run using Docker Compose:

```bash
docker-compose up --build
