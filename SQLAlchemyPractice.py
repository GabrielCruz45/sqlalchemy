# --- BOILERPLATE SETUP ---
import datetime
from sqlalchemy import create_engine, select, func
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# 1. Engine: The connection source. Using in-memory SQLite for this example.
engine = create_engine("sqlite:///:memory:")

# 2. Declarative Base: All models will inherit from this.
Base = declarative_base()

# 3. Models: Define your database tables as Python classes.
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100))
    # This relationship links a User to their Posts.
    # 'back_populates' creates a two-way link so you can also do post.author.
    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    author_id = Column(Integer, ForeignKey("users.id"))
    # This relationship links a Post back to its User.
    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}')>"

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a Session class which will serve as a factory for new Session objects
Session = sessionmaker(bind=engine)

# --- EXERCISES START HERE ---
# Use this 'session' object for all your exercises.
# The 'with' block ensures the session is properly closed.
with Session() as session:
    print("--- Session started. Complete exercises below. ---")

    # Example: Creating and adding two users to start with
    user1 = User(name="Alice", email="alice@example.com")
    user2 = User(name="Bob", email="bob@work.com")
    session.add_all([user1, user2]) # .add_all for multiple
    session.commit() # Save the users to the database

    # 👇 YOUR CODE GOES HERE 👇

    # exercise 1
    new_user = User(name="Charlie", email="charlie_parker@bebop.com")
    session.add(new_user)
    session.commit()
    charlie = session.get(User, 3)
    print(f'Found {charlie}')

    # exercise 2
    print('The user with an id = 1 is ' + (session.get(User, 1)).name)

    # exercise 3
    statement = select(User.name)
    print(str(session.scalars(statement).all()))

    print("\n--- Session finished. ---")