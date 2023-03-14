# WebXCrawler

WebXCrawler is a fast static crawler to crawl a website and get all the links.

## Installation Through PIP

To install dependencies, use the following command:

```bash
pip3 install -r requirements.txt
```

## Installation Through Poetry

This package is built with [Poetry](https://python-poetry.org/). To set up the virtual environment and install dependencies, follow these steps (trying using with sudo, if you get any error):

```bash
poetry install
```

### Installation with Docker

This tool can also be used with [Docker](https://www.docker.com/). To set up the Docker environment, follow these steps (trying using with sudo, if you get any error):

```bash
docker build -t webxcrawler:latest .
```

## Using the WebXCrawler

To run the WebXCrawler on a website, use the '-u' flag and provide the URL as an argument:

```bash
python3 webxcrawler -u URL
```

For an overview of all commands use the following command:

```bash
python3 webxcrawler -h
```

The output shown below are the latest supported commands.

```bash
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗
██║    ██║██╔════╝██╔══██╗╚██╗██╔╝██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝ ╚███╔╝ ██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗ ██╔██╗ ██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██╔╝ ██╗╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                           Coded with Love by Shivam Saraswat (@cybersapien)

usage: python3 webxcrawler [-h] -u URL [-d int] [-t int] [-o file_path] [-V]

WebXCrawler is a fast static crawler to crawl a website and get all the links.

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to crawl
  -d int, --depth int   maximum depth to crawl (default 2)
  -t int, --threads int
                        number of threads to use (default 2)
  -o file_path, --output file_path
                        file to write output to
  -V, --version         show webxcrawler version number and exit

Example: python3 webxcrawler -u https://example.com -d 2 -t 10 -o /tmp/tofile
```

## Using the Docker Container

A typical run through Docker would look as follows:

```bash
docker run -it --rm webxcrawler -u URL
```

**NOTE:** Do check out **[Golang Version of WebXCrawler](https://github.com/shivamsaraswat/webxcrawler_go)**.
