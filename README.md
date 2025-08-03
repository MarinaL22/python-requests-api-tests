# RESTful API Test Automation

Automated API tests using Python, Pytest, and Requests, organized into a modular test framework with configuration, test data, and reusable utilities.

## Project Structure

```
restful-api/
├── config/              # Configuration settings (e.g. base URL)
│   └── config.py
├── data/                # Test data in JSON format
│   └── test_data.json
├── tests/               # Test cases and pytest fixtures
│   ├── conftest.py
│   └── test_crud.py
├── utils/               # Custom reusable API client
│   └── api_client.py
├── pytest.ini           # Pytest configuration
├── requirements.txt     # Dependencies
└── .gitignore
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/restful-api.git
cd restful-api
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate       # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Tests

Simply run:

```bash
pytest
```

With verbose output:

```bash
pytest -v
```

Or run a specific test module:

```bash
pytest tests/test_crud.py
```

## Key Components

- `api_client.py`: Wrapper around `requests` for reusable HTTP methods
- `config.py`: Base configuration including the API base URL
- `test_data.json`: Example payloads or expected values for test scenarios
- `conftest.py`: Pytest fixtures for setup, teardown, and shared logic
- `test_crud.py`: Main test file covering Create, Read, Update, Delete operations

## Features

- Modular and scalable folder structure
- Externalized test data
- Fixtures and utility client for cleaner test logic
- Easy configuration via `config.py`

## Dependencies

Listed in `requirements.txt`. Example:

```
requests
pytest
```

Install them with:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.
