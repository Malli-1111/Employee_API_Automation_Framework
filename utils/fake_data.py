from faker import Faker
import random

fake = Faker()


class FakeData:

    @staticmethod
    def employee_payload():

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