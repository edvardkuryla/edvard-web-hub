from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.deps import get_current_user
from config.database.database import get_db
from src.repositories.balance import deposit
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