import requests

import pygal
from pygal.style import DarkStyle as DS, RotateStyle as RS
from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts, titles = [], []
for submission_id  in submission_ids[:30]:
    # Make a separate call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()
    title = response_dict['title']
    titles.append(title)
    submission_dict = {
        'label': response_dict['title'],
        'xlink': 'http://news/ycombinator.com/item?id=' + str(submission_id),
        'value': response_dict.get('descendants', 0),
        }
    print(str(submission_id))
    submission_dicts.append(submission_dict)

# s_dicts  = sorted(submission_dicts, key=itemgetter('comments'),
#                             reverse=True)


# print(s_dicts)
# for s_dict in s_dicts:
#     print("\nTitle:", s_dict['title'])
#     print("Discussion link:", s_dict['link'])
#     print("COmments:", s_dict['comments'])

# Make visualization.
my_style = RS('#75ff98', base_style=DS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "The most active discussion on Hacker-News"
chart.x_labels = titles
chart.add('', submission_dicts)
chart.render_to_file('active_discussion.svg')
