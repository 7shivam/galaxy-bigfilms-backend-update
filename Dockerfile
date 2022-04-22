FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY ./app /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

ENV PYTHONPATH "${PYTHONPATH}:/app/src"

CMD ["uvicorn","src.index:app","--host=0.0.0.0","--reload"]
