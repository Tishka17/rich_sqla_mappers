from sqlalchemy import select, join
from sqlalchemy.orm import registry, relationship, column_property
from sqlalchemy.testing.schema import mapped_column

from models import User, Post, PostFull
from tables import users_table, posts_table, profiles_table, metadata

mapper_registry = registry(metadata=metadata)
mapper_registry.map_imperatively(Post, posts_table)
mapper_registry.map_imperatively(
    PostFull,
    posts_table,
    properties={
        "user": relationship(User)
    }
)

users_query = join(users_table, profiles_table)
mapper_registry.map_imperatively(
    User,
    users_query,
    properties={
        "username":users_table.c.name,
        "id":users_table.c.id,
    }
)
