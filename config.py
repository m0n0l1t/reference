from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from loguru import logger

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="1 week", compression='zip')
engine = create_engine('sqlite:///db/main.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

token = 'your_token'
owner = [
    281704253146398722
]

# Пути для расширений
bots = [
    "Bots.User.user"
]
