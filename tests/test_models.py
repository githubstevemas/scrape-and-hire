import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.db import Base, Job, Cv


TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(scope="module")
def engine():
    # Create engine for testing, then delete it

    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(engine)

    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def session(engine):
    # Create session for testing

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session
    session.rollback()
    session.close()


def test_create_job(session):
    # Test to create job in test db

    job = Job(title="Python Dev", company="Google",
              description="AI Developpement")
    session.add(job)
    session.commit()

    saved_job = session.query(Job).filter_by(
        title="Python Dev").first()

    assert saved_job.company == "Google"
    assert saved_job.description == "AI Developpement"


def test_create_cv(session):
    # Test to create CV in test db

    cv = Cv(name="John Doe",
            brute_text="Text text text",
            key_words="Python, SQL",
            current_cv=True)
    session.add(cv)
    session.commit()

    saved_cv = session.query(Cv).filter_by(name="John Doe").first()

    assert saved_cv.current_cv is True
    assert saved_cv.key_words == "Python, SQL"
