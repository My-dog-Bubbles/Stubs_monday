import os
import random
from datetime import datetime


# ============================================================
# INSTRUCTIONS
# ============================================================
# Each function below has a dependency problem.
# It reaches out to something external that your test cannot control.
#
# For each function:
#   1. Fix the function so the dependency can be injected
#   2. Write a test that passes every time
#
# Your fix must:
#   - add a parameter with default None
#   - use the real dependency only if the parameter is None
#
# Submit this file to Blackboard via GitHub link when done.
# ============================================================


# ------------------------------------------------------------
# Exercise 1 -- datetime dependency
# ------------------------------------------------------------
# This function checks whether a store is open based on the
# current time. A test that calls it without controlling the
# time will pass sometimes and fail sometimes.
#
# Fix: add a parameter so the time can be injected.
# Then write test_store_open() and test_store_closed() below.

def get_store_status(current_time = None):
    if current_time == None:
        current_time = datetime.now()
    hour = current_time.hour
    if 9 <= hour < 21:
        return "Store is open"
    else:
        return "Store is closed"


def test_store_open():
    fake_time = datetime(2024, 1, 1, 9, 0)  # at 9:00 AM
    result = get_store_status(current_time = fake_time)
    assert result == "Store is open"


def test_store_closed():
    fake_time = datetime(2024, 1, 1, 21, 0)  # at 9:00 PM
    result = get_store_status(current_time = fake_time)
    assert result == "Store is closed"


# ------------------------------------------------------------
# Exercise 2 -- random dependency
# ------------------------------------------------------------
# This function assigns a student to a study group at random.
# A test that calls it without controlling randomness cannot
# assert a specific result reliably.
#
# Fix: add a parameter so the random source can be injected.
# Then write test_assign_study_group() below.
# Use == to assert an exact value -- not "result in [...]"

def assign_study_group(random_index = None):
    list = ["Group A", "Group B", "Group C"]
    if random_index == None:
        return random.choice(list)
    else:
        return list[random_index] 


def test_assign_study_group():
    list_index = 2
    result = assign_study_group(list_index)
    assert result == "Group C"


# ------------------------------------------------------------
# Exercise 3 -- environment variable dependency
# ------------------------------------------------------------
# This function returns an API URL based on an environment
# variable. A test that calls it without controlling the
# environment cannot predict which URL it gets back.
#
# Fix: add a parameter so the env value can be injected.
# Then write test_api_url_production() and
# test_api_url_staging() below.

def get_api_url(key_value = None):
    if key_value == None:
        env = os.getenv("APP_ENV")
    else:
        env = key_value
    if env == "production":
        return "https://api.example.com"
    else:
        return "https://staging.example.com"


def test_api_url_production():
    fake_env = "production"
    result = get_api_url(fake_env)
    assert result == "https://api.example.com"


def test_api_url_staging():
    fake_env = "APP_ENV"
    result = get_api_url(fake_env)
    assert result == "https://staging.example.com"
