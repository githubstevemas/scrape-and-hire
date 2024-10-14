from sqlalchemy.orm import sessionmaker

from model.db import Job, engine, Cv

Session = sessionmaker(bind=engine)
session = Session()


def insert_job(job_data):
    # With job dict, if title and company not existing insert data in db

    existing_job = session.query(Job).filter_by(
        title=job_data["title"],
        company=job_data["company"]
    ).first()

    if not existing_job:

        new_job = Job(
            title=job_data["title"],
            company=job_data["company"],
            description=job_data["description"]
        )

        session.add(new_job)
        session.commit()

    return


def insert_cv(cv_data):

    new_cv = Cv(
        name=cv_data["name"],
        brute_text=cv_data["brute_text"]
        # key_words=cv_data[""]
    )

    session.add(new_cv)
    session.commit()
