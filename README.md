# WebXCrawler

WebXCrawler is a fast static crawler to crawl a website and get all the links.

## Installation Through Poetry
This package is built with [Poetry](https://python-poetry.org/). To set up the virtual environment and install dependencies, follow these steps:

```bash
# Install the dependencies
poetry install
```

To run the program, use the following command:

```bash
python3 webxcrawler -h
```

### Installation with Docker
This package can also be used with [Docker](https://www.docker.com/). To set up the Docker environment, follow these steps:

```bash
docker build -t webxcrawler:latest .
```

To run the program, use the following command:

```bash
docker run --rm webxcrawler -h
```

# Using the WebXCrawler
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
                                                                                                                                                                                            
usage: python3 webxcrawler [-h] -u URL [-d int] [-t int] [-o file_path]

WebXCrawler is a fast static crawler to crawl a website and get all the links.

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to crawl
  -d int, --depth int   maximum depth to crawl (default 2)
  -t int, --threads int
                        number of threads to use (default 2)
  -o file_path, --output file_path
                        file to write output to

Example: python3 webxcrawler -u https://toscrape.com -d 2 -t 10 -o /tmp/toscrape
```
## Using the Docker

A typical run through Docker would look as follows:

```bash
docker run -it --rm webxcrawler -u URL
```
