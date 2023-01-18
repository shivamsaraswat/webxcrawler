# Build: docker build -t webxcrawler:latest .
# Run: docker run -it --rm webxcrawler -h

# Base Image
FROM python:3.10-alpine

# Maintainer
LABEL maintainer="Shivam Saraswat <thecybersapien@protonmail.com>"
LABEL description="WebXCrawler is a fast static crawler to crawl a website and get all the links."

# Install OS Dependencies
RUN apk update && apk upgrade && apk add --no-cache bash gcc libffi-dev musl-dev curl

# Set Work Directory
WORKDIR /usr/src/app
# Copy Project
COPY . .

# Install Poetry.
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
RUN poetry config virtualenvs.create false

# Install Project Dependencies
RUN poetry install --no-root

# Start with console arguments passed to docker run
ENTRYPOINT ["python3", "webxcrawler"]