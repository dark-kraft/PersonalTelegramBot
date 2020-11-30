from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

job_stores = {
    'default': SQLAlchemyJobStore(url='postgresql://localhost:5432/postgres')
}

executors = {
    'default': ThreadPoolExecutor(10)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BackgroundScheduler(jobstores=job_stores, executors=executors, job_defaults=job_defaults)



