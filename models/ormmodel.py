from unicodedata import name
from sqlalchemy import Integer, String, ForeignKey, Column, create_engine, select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    email = Column(String(45))
    phone = Column(String(45))
    password = Column(String(45))
    roleid = Column(Integer, ForeignKey("roles.id"))
    avatar = Column(String(45))
    roleinfo = relationship("Roles", cascade="all")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, roleid={self.roleinfo})"

class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    title = Column(String(45))
    # users = relationship("User", back_populates="roles")

    def __repr__(self):
        return f"title={self.title}"

engine = create_engine("mysql+pymysql://root@localhost/test", echo=True, future=True)

with Session(engine) as session:
    print("SESSION CREATED")
    user1 = User(
        name = "Someone",
        email = "someone@gmail.com",
        phone = "1231231232",
        password = "123123",
        roleid = 20,
        avatar = "",
    )

    # session.add(user1)
    # session.commit()
    stmt = select(User)
    # print(stmt)
    for user in session.scalars(stmt):
        print(user.roleinfo.title)
