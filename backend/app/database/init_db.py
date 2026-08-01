from app.database.base import Base
from app.database.session import engine

# Import all models so SQLAlchemy knows about them
from app.models import User


def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")


if __name__ == "__main__":
    init_db()