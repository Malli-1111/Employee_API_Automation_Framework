# Employee Management API Automation Framework

A Python-based REST API automation framework built using Pytest and Requests, with a FastAPI application used as the backend for testing.

The framework demonstrates functional, negative, data-driven, schema, database, performance, file-upload, and end-to-end API testing along with reporting, logging, Docker, and CI/CD integration.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Automation language |
| Pytest | Test framework |
| Requests | REST API automation |
| FastAPI | Application/API |
| SQLAlchemy | Database interaction |
| SQLite | Application database |
| Pydantic | Request/response validation |
| Python-Jose | JWT authentication |
| Faker | Dynamic test data generation |
| Allure | Test reporting |
| Pytest-HTML | HTML test reporting |
| Docker | Containerization |
| Git | Version control |
| GitHub | Source code repository |
| GitHub Actions | CI/CD |
| Jenkins | CI/CD and webhook integration |

---

## Framework Architecture

```text
                    Test Layer
                        |
                        v
                API Client Layer
                        |
                        v
                     BaseAPI
                        |
                        v
                    Requests
                        |
                        v
                FastAPI Application
                   /          \
                  /            \
                 v              v
        JWT Authentication   SQLite Database

## Framework Layers
Tests - Contains Pytest test cases and fixtures.
API Client Layer - Provides reusable methods for interacting with APIs.
BaseAPI - Centralizes HTTP request handling and retry configuration.
FastAPI Application - Provides the backend APIs used by the automation framework.
Database - SQLite database accessed through SQLAlchemy.
Utilities - Provides logging, assertions, configuration, test data, database helpers, and reporting utilities.

##Project Structure
Employee_API_Automation_Framework/
│
├── .github/
│   └── workflows/
│       └── api-tests.yml
│
├── Api/
│   ├── auth_api.py
│   ├── base_api.py
│   ├── employee_api.py
│   └── upload_api.py
│
├── app/
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── config/
│   ├── dev.json
│   ├── qa.json
│   ├── uat.json
│   └── prod.json
│
├── payloads/
│   └── employee_payload.py
│
├── resources/
│   └── sample.txt
│
├── schemas/
│   └── employee_schema.py
│
├── test_data/
│   └── employee_data.json
│
├── tests/
│   ├── conftest.py
│   ├── test_create_employee.py
│   ├── test_create_employee_dynamic.py
│   ├── test_create_employee_json.py
│   ├── test_create_employee_param.py
│   ├── test_database_validation.py
│   ├── test_delete_employee.py
│   ├── test_employee_workflow.py
│   ├── test_get_all_employees.py
│   ├── test_get_employee.py
│   ├── test_login.py
│   ├── test_response_headers.py
│   ├── test_response_time.py
│   ├── test_schema_validation.py
│   ├── test_update_employee.py
│   └── test_upload_file.py
│
├── utils/
│   ├── allure_utils.py
│   ├── assertions.py
│   ├── config.py
│   ├── db_utils.py
│   ├── fake_data.py
│   ├── json_reader.py
│   └── logger.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── pytest.ini
├── requirements.txt
└── README.md

##API Coverage

The framework covers the following scenarios:

Authentication
JWT authentication
Valid login
Invalid credentials
Blank credentials
Employee APIs
Create employee
Get employee
Get all employees
Update employee
Delete employee
Negative Testing
Invalid employee IDs
Invalid data types
Invalid authentication credentials
Blank request values
Additional API Testing
Response header validation
Response time validation
Response schema validation
Database persistence validation
File upload testing
End-to-end employee workflow

##End-to-End Employee Workflow

The framework validates the complete employee lifecycle:
Create Employee
      |
      v
Get Employee
      |
      v
Update Employee
      |
      v
Delete Employee
      |
      v
Verify Employee Deleted

This validates the interaction between multiple APIs rather than testing each endpoint independently.

##Test Data Strategies
The framework supports multiple test-data approaches.

--Static Data--
Reusable payloads are maintained in:
 payloads/employee_payload.py

--Dynamic Data--
Realistic employee data is generated using Faker:
 utils/fake_data.py

--JSON Data-Driven Testing--
External test data is maintained in:
 test_data/employee_data.json

--Pytest Parameterization--
Multiple test scenarios can be executed using:
 @pytest.mark.parametrize

#Validation
The framework performs validation at multiple levels.

#API Response Validation
Reusable assertions are maintained in:
 utils/assertions.py

--Examples include:--
Status code validation
Response body validation
Required field validation
Response content validation

#Schema Validation
 Employee response structures are validated using Pydantic-based schemas:
 schemas/employee_schema.py

##Database Validation

The framework validates data persistence directly in the SQLite database using SQLAlchemy.

API Request
    |
    v
Create Employee
    |
    v
Get Employee ID
    |
    v
Query SQLite Database
    |
    v
Compare API Data
with Database Data

This provides an additional layer of validation beyond API response assertions.

##Configuration Management

Environment-specific configuration files are maintained under:

config/
├── dev.json
├── qa.json
├── uat.json
└── prod.json

The test environment can be selected using the TEST_ENV environment variable.

--Example:--

set TEST_ENV=qa
pytest

If no environment is specified, the framework uses the default environment configured by the project.

Sensitive credentials and secrets should be supplied through environment variables or CI/CD secrets rather than committed to source control.

##Setup and Installation
1. Clone the Repository
   git clone <repository-url>
   cd Employee_API_Automation_Framework

2. Create Virtual Environment
  python -m venv .venv

3. Activate Virtual Environment
Windows:
 .venv\Scripts\activate

4. Install Dependencies
 pip install -r requirements.txt

##Running the Application

Start the FastAPI application:
 python -m uvicorn app.main:app --host 127.0.0.1 --port 8000

Swagger documentation:
 http://127.0.0.1:8000/docs

##Running Tests
Run all tests
 pytest
Run smoke tests
 pytest -m smoke
Run regression tests
 pytest -m regression
Run login tests
 pytest -m login
Run end-to-end tests
 pytest -m e2e

##Pytest Fixtures

Reusable test setup is maintained in:

 tests/conftest.py

The framework uses fixtures for common test dependencies such as:

Authentication token
Authorization headers
Employee creation
Test setup and teardown

This reduces code duplication and keeps test cases focused on validation.

##Retry Mechanism

HTTP request handling is centralized in:

 Api/base_api.py

The framework uses a retry mechanism for selected transient HTTP failures.

The retry configuration handles server-side responses such as:
 500
 502
 503
 504
This improves test stability when temporary server-side failures occur.

##Logging

API execution details are captured using Python's logging framework.

Logs include information such as:
HTTP method
Endpoint
Request parameters
Request payload
Response status
Response body
Execution time
Request exceptions

--Logs are generated under:--

  logs/

Generated log files are excluded from source control.

##Reporting
The framework supports multiple reporting mechanisms.

--HTML Report--
Pytest HTML reporting can generate:
 reports/report.html

--Allure--
Allure results are generated under:
 allure-results/

The framework also provides utilities for attaching request and response information to Allure reports.

##Docker

The application can be containerized using Docker.

--Build Docker Image--
docker build -t employee-api .

--Run Container--
 docker run -d --name employee-api-container -p 8000:8000      employee-api

--Check Running Containers--
  docker ps

--View Container Logs--
  docker logs employee-api-container

--Swagger documentation:--

  http://127.0.0.1:8000/docs

The .dockerignore file prevents unnecessary files such as virtual environments, Git files, caches, logs, reports, and local database files from being included in the Docker build context.

##CI/CD

GitHub Actions

--The project contains:--

  .github/workflows/api-tests.yml

The workflow automates API test execution.

 Pipeline:

GitHub
   |
   v
Checkout Code
   |
   v
Setup Python
   |
   v
Install Dependencies
   |
   v
Start FastAPI
   |
   v
Wait for API
   |
   v
Run Pytest
   |
   v
Upload Test Artifacts

The workflow is configured to execute tests for relevant repository events such as pushes and pull requests.

Artifacts can include test reports and application logs generated during execution.

##Jenkins

Jenkins is used for CI execution and GitHub webhook integration.

--Pipeline:--

GitHub
   |
   v
GitHub Webhook
   |
   v
Jenkins
   |
   v
Checkout Code
   |
   v
Install Dependencies
   |
   v
Start Application
   |
   v
Run Pytest
   |
   v
Publish Results

This demonstrates integration between source control, CI automation, application startup, and automated API testing.

##Key Framework Features

Reusable API client architecture
Centralized HTTP request handling
Pytest fixtures
JWT authentication
Positive and negative testing
Data-driven testing
Dynamic test data generation
Pytest parameterization
Schema validation
Database validation
Response header validation
Response time validation
File upload testing
End-to-end workflow testing
Centralized assertions
API logging
Retry mechanism
Allure reporting
HTML reporting
Docker execution
GitHub Actions CI/CD
Jenkins integration

##What This Project Demonstrates

This project demonstrates practical experience in:

Designing a reusable API automation framework
REST API testing using Python and Requests
Pytest framework development
Authentication and authorization testing
Functional and negative testing
Data-driven automation
API schema validation
Database validation
Test data generation
Logging and reporting
Dockerized application execution
CI/CD integration
Git and GitHub workflow

##Future Improvements
--Potential improvements include:--

Move all credentials and secrets to environment variables or CI/CD secrets
Add broader boundary-value and security testing
Add API contract validation against OpenAPI specifications
Improve database session management using FastAPI dependencies
Add Docker Compose for multi-service execution
Publish Allure reports automatically from CI
Expand API coverage with additional edge cases