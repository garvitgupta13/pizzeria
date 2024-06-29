import traceback
from typing import Type

from redis import Redis
from rq.job import Job


def report_failure(
    job: Job,
    connection: Redis,
    exc_type: Type[Exception],
    exc_value: Exception,
    traceback: traceback,
) -> None:
    """
    Print job details on failure.

    Refer : https://stackoverflow.com/questions/12774085/dealing-with-exception-handling-and-re-queueing-in-rq-on-heroku
    """
    print(f"Job failed: {job.id}, data: {job.data}, metadata: {job.meta}")
    if job.retries_left:
        return

    print(f"Maximum retries exceeded for job_id: {job.id}")
