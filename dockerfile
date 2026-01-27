FROM mcr.microsoft.com/playwright:v1.58.0-noble

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium

COPY . . 

CMD ["pytest"]
