from database import Base
from sqlalchemy import Column, Integer,String,Sequence,ARRAY,LargeBinary

class Users(Base):
    __tablename__ = "users"
    id = Column("id",Integer,Sequence("id sequence",start=1), primary_key=True, nullable=False)
    profile_pic = Column('profile', LargeBinary)
    name = Column("name",String, nullable=False)
    email = Column("email",String, nullable = False)
    password = Column("password",String, nullable= False)
    listings = Column("listings", ARRAY(Integer))

class Listing(Base):
    __tablename__ = "listing"
    id = Column("id",Integer,Sequence("id sequence",start=1), primary_key=True, nullable=False)
    users_id = Column("users_id", Integer, nullable = False, default = 1)
    images = Column("images",ARRAY(LargeBinary),nullable = True)
    title = Column("title", String, nullable = False)
    description = Column("description", String,nullable = True)

class Posts(Base):
    __tablename__ = "posts"
    id = Column("id",Integer,Sequence("id sequence",start=1), primary_key=True, nullable=False)
    data = Column("data", String, nullable = False)
    location = Column()