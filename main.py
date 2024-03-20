from bs4 import BeautifulSoup
import requests
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

url = 'https://www.imdb.com/title/tt0903747/episodes?season='

# Define a custom User-Agent string to simulate a real web browser
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

show_ratings_lst = []
for i in range(1, 6):
    response = requests.get(url+str(i), headers={"User-Agent": user_agent})
    soup = BeautifulSoup(response.text, 'html.parser')

    ratings_lst = [float(rating.text.split("/")[0]) for rating in
                   soup.select('span.ipc-rating-star--imdb')]
    show_ratings_lst.append(ratings_lst)


# for season in show_ratings_lst:
    # min_r, max_r, avg_r = min(season), max(season), sum(season) / len(season)
    # print(f'Min: {min_r}\nMax: {max_r}\nAverage: {avg_r}')

for season in show_ratings_lst:
    season += [0.0] * (16 - len(season))

seasons = [f'Season {i}' for i in range(1, len(show_ratings_lst) + 1)]
episodes = [f'Episode {i}' for i in range(1, 17)]

arr = np.array(show_ratings_lst)

fig, ax = plt.subplots()

im = ax.imshow(arr, cmap=plt.cm.YlGn)

ax.set_yticks(np.arange(len(seasons)), labels=seasons)
ax.set_xticks(np.arange(len(episodes)), labels=episodes)

plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

for i in range(len(seasons)):
    for j in range(len(episodes)):
        text = ax.text(j, i, arr[i][j], ha='center', va='center', color='w')

ax.set_title('Breaking Bad - ratings per episode')
fig.tight_layout()
plt.show()


