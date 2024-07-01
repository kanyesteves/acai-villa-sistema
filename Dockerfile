FROM python:3.9

WORKDIR /app

COPY requirements.txt . 
COPY db/db_users.sqlite .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "src/login.py"]