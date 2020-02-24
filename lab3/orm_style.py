from datetime import datetime
import os

import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from sqlalchemy import Column, Integer, String


EntityBase = sqlalchemy.ext.declarative.declarative_base()


class Comment(EntityBase):
    __tablename__ = "Comment"
    id = Column("id", Integer, primary_key=True)
    text = Column("text", String, nullable=False)
    published = Column(sqlalchemy.DateTime, nullable=False, default=datetime.now)
    post_id = Column(sqlalchemy.ForeignKey("Post.id"))


class Post(EntityBase):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    published = Column(sqlalchemy.DateTime, nullable=False, default=datetime.now)

    comments = sqlalchemy.orm.relationship("Comment")


class ORM:
    engine = None
    db_conn_string = None
    db_path = None
    db_metadata = None
    session_factory = None

    def __init__(self):
        ORM.init_engine()

    @staticmethod
    def init_engine():
        if ORM.engine is not None:
            return

        print("Creating ORM engine...")

        ORM.db_path = os.path.abspath("data/blog_orm.sqlite_db")
        #os.remove(ORRM.db_path)
        ORM.db_conn_string = "sqlite:///{0}".format(ORM.db_path).replace("\\", "/")  # yes, even on Windows.
        ORM.engine = sqlalchemy.create_engine(ORM.db_conn_string, echo=True)

        ORM.session_factory = sqlalchemy.orm.sessionmaker(bind=ORM.engine)


    @classmethod
    def create_session(cls):
        return ORM.session_factory()

    @classmethod
    def init_metadata(cls):
        EntityBase.metadata.create_all(ORM.engine)

    @classmethod
    def add_base_data(cls):

        session = ORM.create_session()
        row_count = session.query(Post).count()
        if row_count:
            print("Data already committed, exiting ({0} rows)".format(row_count))
            return

        post1 = Post(title="First post", content="Coming soon")
        post2 = Post(title="Second post", content="Coming soon")
        post3 = Post(title="Funny post", content="This will make you laugh")
        post4 = Post(title="Funny funny post", content="This will make you laugh, LOL")

        session.add(post1)
        session.add(post2)
        session.add(post3)
        session.add(post4)

        print(session.new)

        session.commit()


    @classmethod
    def update_lol_post(cls):
        session = ORM.create_session()

        lol_post = session.query(Post). \
            filter(Post.title == "Funny funny post"). \
            one()

        if not lol_post:
            print("WHOA didn't find lol post")
            return

        lol_post.content = "This will make you LOL dude!"
        session.commit()

    @classmethod
    def show_data(cls):
        session = ORM.create_session()

        posts = (
            session.query(Post).
            filter(Post.title.like('%Funny%')).
            order_by(Post.published.desc())
        )

        for p in posts:
            print(p.title, p.published)

    @classmethod
    def add_comments(cls):
        session = ORM.create_session()

        post = (
            session.query(Post).
            filter(Post.title.like('%Funny%')).
            order_by(Post.published.desc())
        ).first()

        if post.comments:
            print("Comments already exist, not adding more...")
        else:
            comment = Comment()
            comment.text = "Whoa, that did make me LOL!"
            post.comments.append(comment)
            comment = Comment()
            comment.text = "Yeah, me too!"
            post.comments.append(comment)

            session.commit()

        session = ORM.create_session()
        post = (
            session.query(Post).
            options(sqlalchemy.orm.joinedload(Post.comments)).
            filter(Post.title.like('%Funny%')).
            order_by(Post.published.desc())
        ).first()

        print("Title: {0}".format(post.title))
        for c in post.comments:
            print("   {0}".format(c.text))


def run():
    the_orm = ORM()
    the_orm.init_metadata()
    the_orm.add_base_data()
    the_orm.update_lol_post()
    the_orm.show_data()
    the_orm.add_comments()
