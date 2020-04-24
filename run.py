import subprocess

from flask import Flask
from flask import request
from flask_api import status

name_id = 0
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Crawler service"


@app.route('/get_airbnb')
def airbnb():
    """
        Run spider in another process and store items in file. Simply issue command:

        wait for  this command to finish, and read output.json to client.
        """
    city = request.args.get("city")
    if city:
        global name_id
        name_id = name_id + 1
        try:
            subprocess.check_output(['scrapy', 'crawl', "bnb", "-a", f"query=\"{city}\"", "-o", f"{name_id}.json"],
                                    cwd="airbnb-scraper/")
        except Exception:
            return status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        return "City is not specified", status.HTTP_204_NO_CONTENT
    with open(f"airbnb-scraper/{name_id}.json") as items_file:
        return items_file.read()


@app.route('/get_amazon')
def amazon():
    """
        Run spider in another process and store items in file. Simply issue command:

        wait for  this command to finish, and read output.json to client.
        """
    category = request.args.get("category")
    if category:
        global name_id
        name_id = name_id + 1
        try:
            subprocess.check_output(['scrapy', 'crawl', "amazon_scraper", "-a", f"category=\"{category}\"",
                                     "-o", f"{name_id}.json"],
                                    cwd="amazon-scraper-master/")
        except Exception:
            return status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        return "Category is not specified", status.HTTP_204_NO_CONTENT
    with open(f"amazon-scraper-master/{name_id}.json") as items_file:
        return items_file.read()


if __name__ == '__main__':
    app.run(port=6379)
