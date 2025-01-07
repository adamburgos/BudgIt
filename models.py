import uuid
from datetime import datetime

class Expense:
    def __init__(self, category, amount, description):
        self.id          = str(uuid.uuid4()) # generate unique uuid
        self.category    = category
        self.amount      = amount
        self.date        = datetime.now()
        self.description = description

    def __repr__(self):
        return f"Expense(ID={self.id}, Category={self.category}, Amount={self.amount}, Date={self.date}, Description={self.description})"
    