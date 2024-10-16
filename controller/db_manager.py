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


def get_cvs():

    cvs = [cv[0] for cv in session.query(Cv.name).all()]

    return cvs


def unset_current_cv():

    old_current_cv = session.query(Cv).filter_by(current_cv=True).first()

    if old_current_cv:
        old_current_cv.current_cv = False

        session.commit()


def define_cv_to_use(cv_name):
    # Change current cv attribute to True

    try:
        cv = session.query(Cv).filter_by(name=cv_name).first()

        cv.current_cv = True

        session.commit()

    except Exception as e:
        print(e)
