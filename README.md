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
## Install requiremetns and browser
pip install -r requirements.txt
playwright install chromium
## Run tests
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

---

# Автоматизированное тестирование пользовательского интерфейса SwagLabs

Автоматическое тестирование страницы авторизации на демонстрационном сайте SwagLabs (SauceDemo) (<https://www.saucedemo.com/>)

## Технологический стек

- **Язык программирования**: Python 3.10
- **Фреймворк**: Pytest
- **Инструмент тестирования**: Playwright
- **Отчетность**: Allure Framework со скриншотами
- **Логирование**: Python Logging
- **Контейнеризация**: Docker

## Локальная настройка и запуск

**Клонируйте git и перейдите в проект**

```bash
git clone https://github.com/scruffboy/SwagLabs-Test.git
cd SwagLabs-Test

```

**Создайте, активируйте виртуальное окружение и запустите тесты**

```bash
python -m venv .venv
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate

# Установка требований и браузера
pip install -r requirements.txt
playwright install chromium

# Запуск тестов
pytest
```

## Запуск Docker

**Создание образа Docker и запуск тестов в контейнере**

```bash
docker build -t swag-labs-test .

docker run --rm swag-labs-test
```

## Отчеты Allure

```bash
allure serve allure-results
```

## Структура проекта

- `pages/` - Модели Page Object (BasepPage, LoginPage)
- `tests/` - Тестовые сценарии и conftest (фикстуры, управление браузером)
- `tools/` - Классы инструментов (пользовательский логгер)
- `utils/` - Вспомогательные классы (Config: URL, Timeouts)
- `dockerfile` - Конфигурация контейнера
- `pytest.ini` - Конфигурация средства запуска тестов
