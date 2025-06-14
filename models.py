from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///jobs.db")
Session = sessionmaker(bind=engine)

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    link = Column(String, unique=True)
    tags = Column(String)
    __table_args__ = (UniqueConstraint('title', 'company', name='_title_company_uc'),)

Base.metadata.create_all(engine)

def save_jobs_to_db(job_list):
    session = Session()
    for job in job_list:
        if not session.query(Job).filter_by(link=job['link']).first():
            session.add(Job(**job))
    session.commit()
