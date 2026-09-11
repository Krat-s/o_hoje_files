from datetime import datetime, time
import os
import sys

from shared.scheduling.daily_task_random_time import daily_task_loop
from departments.commercial.bot_clicking.boost_ad import click_task

if __name__ == "__main__":
    daily_task_loop(click_task)