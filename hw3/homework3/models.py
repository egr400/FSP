# This file creates tables for the Postgres database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import MONEY

Base = declarative_base()
# Base is inherited in order to register models with SQA
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)
    price = Column(MONEY)
# Helps define the row of data that will be printed
    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={}, price={})>" \
            .format(self.title, self.author, self.pages, self.published, self.price)