import logging
import os

from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI

load_dotenv()
logger = logging.getLogger(__name__)
TODOIST_API_KEY = os.getenv("TODOIST_API_KEY")


def get_tasks():
    api = TodoistAPI(TODOIST_API_KEY)
    try:
        tasks = api.get_tasks()
        [
            logger.info(f"Task: {task.content} | Created: {task.created}")
            for task in tasks
        ]
    except Exception as error:
        logger.exception("Error retrieving tasks")


def run():
    logger.info("Hello World")
    get_tasks()
