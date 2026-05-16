from flask import Blueprint, request
import requests

from config import NEWS_API_KEY

news_bp = Blueprint('news', __name__)


@news_bp.route('/news')
def get_news():

    category = request.args.get('category', 'india')

    url = f'https://newsapi.org/v2/everything?q={category}&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}'

    response = requests.get(url)

    data = response.json()

    return data