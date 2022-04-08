FROM python:3.8-slim-buster


# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
    COPY . .
CMD ["python","manage.py","runserver"]
EXPOSE 800
