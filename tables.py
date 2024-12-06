from sqlalchemy import Table, Column, MetaData, Integer, String, ForeignKey

metadata = MetaData()

users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)

profiles_table = Table(
    'profiles',
    metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),  # TODO `id`
    Column('about', String),
)

posts_table = Table(
    'posts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('text', String),
    Column('date', String),
)
