from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/main.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

token = 'your_token'

# Пути для расширений
bots = [
    "Bots.User.user"
]
