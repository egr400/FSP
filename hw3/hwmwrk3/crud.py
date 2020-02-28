from datetime import datetime
##CRUD represesnts Create, Read, Update and Delete
#DJ, Saul, Lan, Greg, Brandon, Matt, Kamari, Gabby, Monica
from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Book
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import yaml

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

##Utilized to destroy and renew the books table
def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

##utilized to queiry the book

def load_yaml():
    with session_scope() as s:
        for data in yaml.load_all(open('books.yaml')):
            book = Book(**data)
            s.add(book)


if __name__ == '__main__':
    recreate_database()
    s = Session()
    book = Book(
            title='Deep Learning',
            author='Ian Goodfellow',
            pages=775,
            published=datetime(2016, 11, 18)
    )
    with session_scope() as s:
        s.add(book)

    load_yaml()
    s.commit()
    print(s.query(Book).all())
