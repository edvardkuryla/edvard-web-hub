from decimal import Decimal
from src.models.models import User, Transaction

def deposit(db, user: User, amount: Decimal):
    user.balance += amount

    tx = Transaction(user_id=user.id, amount=amount, type="deposit", status="success")

    db.add(tx)
    db.commit()
    db.refresh(user)
    return user.balance

def withdraw(db, user: User, amount: Decimal):
    if user .balance < amount:
        return None
    user.balance -= amount

    tx = Transaction(user_id=user.id, amount=amount, type="withdraw", status="success")
    db.add(tx)
    db.commit()
    db.refresh(user)
    return user.balance