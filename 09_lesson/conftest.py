import os
import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from database import metadata

load_dotenv()  # подхватит .env в корне проекта, если есть

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError()

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, future=True)


@pytest.fixture(scope="session", autouse=True)
def prepare_db():
    """
    Создаёт таблицы перед запуском сессии тестов.
    """
    metadata.create_all(engine)
    yield
    # При желании можно удалить таблицы после тестов:
    # metadata.drop_all(engine)


@pytest.fixture()
def db_session():
    """
    Обычная сессия: коммитит изменения в БД.
    тесты сами будут удалять созданные данные в конце теста.
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except SQLAlchemyError:
        # Откат при ошибках SQLAlchemy
        session.rollback()
        raise
    except Exception:
        # Откат при любых других ошибках (не используем bare except)
        session.rollback()
        raise
    finally:
        session.close()


@pytest.fixture()
def tx_session():
    """
    Транзакционная сессия: открывает транзакцию для каждого теста
    и откатывает её в конце.
    Это гарантирует, что тесты не оставят данных в БД.
    """
    connection = engine.connect()
    trans = connection.begin()
    Session = sessionmaker(bind=connection, future=True)
    session = Session()

    try:
        yield session
    finally:
        session.close()
        trans.rollback()
        connection.close()