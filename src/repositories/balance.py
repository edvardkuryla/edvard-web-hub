from sqlalchemy.orm import Session
from src.models.models import User, Transaction

def update_user_balance(db: Session, user: User, new_balance):
    user.balance = new_balance
    db.add(user)

def create_transaction(
    db: Session,
    user_id: int,
    amount,
    operation: str,
    status: str = "success",
):
    tx = Transaction(
        user_id=user_id,
        amount=amount,
        type=operation,
        status=status,
    )
    db.add(tx)
    return tx