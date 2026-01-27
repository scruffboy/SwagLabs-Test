# SwagLabs UI Automation Testing

Automatic testing of the authorization page on the SwagLabs(SauceDemo) demo site (<https://www.saucedemo.com/>)

## Technology Stack

- **Program Language**: Python 3.10
- **Framework**: Pytest
- **Testing Tool**: Playwright
- **Reporting**: Allure Framework with Screenshots
- **Logging**: Python Logging
- **Containerization**: Docker

## Local Setup & Run

**Clone git and navigate to project**

```bash
git clone https://github.com/scruffboy/SwagLabs-Test.git
cd SwagLabs-Test

```

**Create, activate virtual environment and run tests**

```bash
python -m venv .venv
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate

# Install requiremetns and browser
pip install -r requirements.txt
playwright install chromium

# Run tests
pytest
```

## Run Docker

**Build Docker Image and run tests in container**

```bash
docker build -t swag-labs-test .
docker run --rm swag-labs-test
```

## Allure Reports

```bash
allure serve allure-results
```

## Project Structure

- `pages/` - Page Object models(BasepPage, LoginPage)
- `tests/` - Test scenarios and conftest(fixtures, browser management)
- `tools/` - Tools classes(custom Logger)
- `utils/` - Utility classses(Config: URL, Timeouts)
- `dockerfile` - Container configuration
- `pytest.ini` - Test runner configuration
