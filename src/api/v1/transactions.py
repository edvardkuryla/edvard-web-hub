from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.deps import get_current_user
from config.database.database import get_db
from src.services.transactions import deposit, withdraw, list_user_transactions
from src.schemas.schemas import BalanceChange, BalanceResponse
from src.models.models import User

router = APIRouter(prefix="/balance", tags=["balance"])


@router.post("/deposit", response_model=BalanceResponse)
def deposit_money(
    data: BalanceChange,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    try:
        new_balance = deposit(db, user, data.amount)
        return {"balance": new_balance}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/withdraw", response_model=BalanceResponse)
def withdraw_money(
    data: BalanceChange,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    try:
        new_balance = withdraw(db, user, data.amount)
        if new_balance is None:
            raise HTTPException(status_code=400, detail="Not enough funds")
        return {"balance": new_balance}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/transactions")
def get_my_transactions(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return list_user_transactions(db, user.id)