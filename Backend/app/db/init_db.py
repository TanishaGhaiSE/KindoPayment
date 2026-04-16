from sqlmodel import SQLModel
from Backend.app.db.database import engine

# IMPORTANT: import all models so they register
from Backend.app.models import registrations
from Backend.app.models import students
from Backend.app.models import transactions
from Backend.app.models import trips


def init_db():
    print("🔥 Creating tables with SQLModel...")

    SQLModel.metadata.create_all(engine)

    print("✅ Tables created!")


if __name__ == "__main__":
    init_db()