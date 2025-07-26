from fastapi import FastAPI, HTTPException
from typing import List
import json
import os

from models import Transaction, TransactionCreate

app = FastAPI(title="Revel TC MVP API")

DB_PATH = os.path.join(os.path.dirname(__file__), "db.json")


def load_db() -> List[Transaction]:
    """Load transactions from the local JSON database."""
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Transaction(**item) for item in data]


def save_db(transactions: List[Transaction]) -> None:
    """Persist transactions to the local JSON database."""
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump([t.dict() for t in transactions], f, indent=2)


@app.get("/transactions/", response_model=List[Transaction])
def list_transactions() -> List[Transaction]:
    """List all stored transactions."""
    return load_db()


@app.get("/transactions/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: int) -> Transaction:
    """Retrieve a single transaction by ID."""
    transactions = load_db()
    for t in transactions:
        if t.id == transaction_id:
            return t
    raise HTTPException(status_code=404, detail="Transaction not found")


@app.post("/transactions/", response_model=Transaction)
def create_transaction(payload: TransactionCreate) -> Transaction:
    """Create a new transaction with provided contract data."""
    transactions = load_db()
    new_id = max((t.id for t in transactions), default=0) + 1
    transaction = Transaction(id=new_id, contract=payload.contract)
    transactions.append(transaction)
    save_db(transactions)
    return transaction