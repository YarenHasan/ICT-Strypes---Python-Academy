import logging
import time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from typing import Iterator, Dict, Optional
from .config import settings
from typing import List
from . import schemas

logger = logging.getLogger(__name__)
HEADERS = {"User-Agent": settings.USER_AGENT}


def fetch(url: str) -> BeautifulSoup:
    logger.info("Fetching: %s", url)
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def iter_books(limit: Optional[int] = None) -> Iterator[Dict]:
    """Yield book dicts (title, description, url) from Books to Scrape with automatic pagination."""
    base = settings.SCRAPE_BASE_URL
    page = 1
    count = 0

    while True:
        list_url = urljoin(base, f"catalogue/page-{page}.html") if page > 1 else base
        try:
            soup = fetch(list_url)
        except requests.HTTPError as e:
            logger.info("No more pages or failed to fetch page %d: %s", page, e)
            break

        cards = soup.select("section div ol li article.product_pod h3 a")
        if not cards:
            break  # no more books

        for a in cards:
            if limit is not None and count >= limit:
                return
            book_rel = a.get("href")
            book_url = urljoin(list_url, book_rel)
            title = a.get("title") or a.text.strip()

            time.sleep(settings.REQUEST_DELAY_SEC)

            try:
                detail = fetch(book_url)
            except Exception as e:
                logger.error("Failed to fetch detail %s: %s", book_url, e)
                continue

            desc_tag = detail.select_one("#product_description + p")
            description = desc_tag.text.strip() if desc_tag else None

            yield {
                "title": title,
                "description": description,
                "url": book_url,
            }
            count += 1

        page += 1


def scrape_books(limit: int = 10) -> List[schemas.ItemCreate]:
    """
    Scrape books across multiple pages and return a list of ItemCreate objects.
    Respects the limit, stopping when enough books have been collected or no more pages exist.
    """
    items: List[schemas.ItemCreate] = []

    for book in iter_books(limit=limit):
        items.append(
            schemas.ItemCreate(
                title=book["title"],
                description=book.get("description"),
                url=book["url"],
            )
        )

    return items
