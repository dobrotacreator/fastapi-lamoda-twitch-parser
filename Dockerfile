FROM python:3.10-slim-bullseye as base
WORKDIR /parser
COPY Pipfile Pipfile.lock /parser/
RUN pip install pipenv \
 && pipenv --python 3.10 \
 && pipenv install --system --deploy
COPY app /parser/

FROM base as fastapi
RUN chmod +x entrypoints/entrypoint_fastapi.sh
CMD ["python", "main.py"]