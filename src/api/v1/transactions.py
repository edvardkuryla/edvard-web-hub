from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.deps import get_current_user
from config.database.database import get_db
from src.repositories.balance import deposit, withdraw
from src.schemas.schemas import BalanceChange, BalanceResponse

transaction = APIRouter(prefix="/transaction", tags=["transaction"])

@transaction.post("/deposit", response_model=BalanceResponse)
def deposit_money(
    data: BalanceChange,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    new_balance = transaction(db, user, data.amount)
    return {"balance": new_balance}

@transaction.post("/withdraw", response_model=BalanceResponse)
def withdraw_money(
    data: BalanceChange,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    new_balance = withdraw(db, user, data.amount)
    if new_balance is None:
        raise HTTPException(400, "Not enough funds")
    return {"balance": new_balance}

@transaction.get("/me", response_model=BalanceResponse)
def get_my_balance(user = Depends(get_current_user)):
    return {"balance": user.balance}