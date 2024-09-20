FROM python:3.12-slim
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python","calculator.py","--rest"]