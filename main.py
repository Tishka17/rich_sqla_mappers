from datetime import datetime

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from mapper import mapper_registry
from models import User, PostFull, Post


def main():
    engine = create_engine("sqlite:///file.db", echo=True)
    mapper_registry.metadata.create_all(engine)

    sm = sessionmaker(bind=engine)

    with sm() as session:
        user1 = User(id=None, username="hello", about="world")
        user2 = User(id=None, username="hello", about="world")
        post1 = PostFull(
            id=None,
            text="lorem ipsum",
            created_at=datetime.now(),
            author=user1,
        )
        session.add_all([user1, user2, post1])
        session.commit()

    with sm() as session:
        posts = session.execute(select(Post)).all()
        print(posts)


if __name__ == "__main__":
    main()
