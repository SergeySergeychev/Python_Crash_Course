import requests

from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Proess information about each submission.

submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
        }
    submission_dicts.append(submission_dict)

s_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)
for s_dict in s_dicts:
    print("\nTitle:", s_dict['title'])
    print("Discussion link:", s_dict['link'])
    print("Comments:", s_dict['comments'])
