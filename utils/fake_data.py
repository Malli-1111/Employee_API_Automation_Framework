"""
Test data generation utilities.

Provides reusable methods for generating realistic and
randomized employee test data.
"""
from faker import Faker
import random

fake = Faker()


class FakeData:
    """Provides dynamically generated test data for API testing."""
    @staticmethod
    def employee_payload():
        """
        Generate a randomized employee request payload.

        Returns:
            dict: Employee payload containing a random name,
            department, and salary.
        """

        return {
            "name": fake.name(),
            "department": random.choice(
                [
                    "QA",
                    "Developer",
                    "DevOps",
                    "Support",
                    "HR"
                ]
            ),
            "salary": random.randint(30000, 120000)
        }