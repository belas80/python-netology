import requests
from datetime import datetime
from dateutils import relativedelta
from pprint import pprint


def get_questions(url, params):
    result = requests.get(
        url=url,
        params=params
    )
    result.raise_for_status()
    return result


if __name__ == '__main__':
    now = datetime.today()
    days_ago = int((now + relativedelta(days=-2)).timestamp())
    my_url = 'https://api.stackexchange.com/2.3/questions'
    my_params = {
        'fromdate': days_ago,
        'todate': int(now.timestamp()),
        'order': 'desc',
        'sort': 'creation',
        'tagged': 'Python',
        'site': 'stackoverflow'
    }
    questions = get_questions(my_url, my_params)
    # pprint(questions.json())
    for q in questions.json()['items']:
        print(f'question_id:', q['question_id'])
        print(f'creation_date:', datetime.fromtimestamp(q['creation_date']))
        print(f'title:', q['title'])
        print(f'link:', q['link'])
        print(f'tags:', q['tags'])
        print('============')
    print(len(questions.json()['items']))
    # https://api.stackexchange.com/2.3/questions?fromdate=1696377600&todate=1696550400&order=desc&sort=creation&tagged=Python&site=stackoverflow

