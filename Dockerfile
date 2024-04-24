FROM python:3.10-slim-bullseye

RUN apt-get update \
	&& apt-get install -y --no-install-recommends --no-install-suggests \
	&& pip install --no-cache-dir --upgrade pip

WORKDIR /listing.ai
COPY ./backEnd/requirements.txt /listing.ai
RUN pip install --no-cache-dir --requirement /listing.ai/requirements.txt
COPY . /listing.ai

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host 0.0.0.0"]









