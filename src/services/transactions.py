from decimal import Decimal
from sqlalchemy.orm import Session
from src.models.models import User, Transaction
from src.repositories.balance import update_user_balance, create_transaction

def deposit(db: Session, user: User, amount: Decimal):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    new_balance = user.balance + amount
    with db.begin():
        update_user_balance(db, user, new_balance)
        create_transaction(db, user.id, amount, "deposit")

        db.refresh(user)
        return user.balance
    
def withdraw(db: Session, user: User, amount: Decimal):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    
    if user.balance < amount:
        return None
    new_balance = user.balance - amount

    with db.begin():
        update_user_balance(db, user, new_balance)
        create_transaction(db, user.id, amount, "withdraw")

    db.refresh(user)
    return user.balance

def list_user_transactions(db: Session, user_id: int):
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()