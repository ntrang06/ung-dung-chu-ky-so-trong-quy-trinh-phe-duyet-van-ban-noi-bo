FROM python:3.12-slim

WORKDIR /app

RUN pip install cryptography

COPY source/ ./source/

CMD ["/bin/bash"]