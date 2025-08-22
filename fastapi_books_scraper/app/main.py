from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from . import models, schemas, crud
from .database import engine, get_db
from .scraper import scrape_books

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Books Scraper API")


@app.get("/items/{item_id}", response_model=schemas.ItemRead)
def get_item(item_id: UUID, db: Session = Depends(get_db)):
    obj = crud.get_item(db, item_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Item not found")
    return obj


@app.get("/items", response_model=list[schemas.ItemRead])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)


@app.post("/scrape", response_model=list[schemas.ItemRead])
def scrape_and_store(limit: int = 10, db: Session = Depends(get_db)):
    scraped_items = scrape_books(limit=limit)
    saved_items = [crud.create_item(db, item) for item in scraped_items]
    return saved_items


@app.get("/scrape")
def scrape_info():
    return {
        "message": "This is the scrape endpoint. Use POST /scrape with a 'limit' parameter to scrape books."
    }


@app.delete("/items/{item_id}")
def delete_item(item_id: UUID, db: Session = Depends(get_db)):
    success = crud.delete_item(db, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"ok": True}
