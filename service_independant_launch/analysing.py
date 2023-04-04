import pandas as pd
from wordcloud import WordCloud
import io
import base64
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from collections import defaultdict
import seaborn as sns
from collections import Counter


def text_print(path: str, i: str):
    df = pd.read_csv(f"./{path}")
    index = int(i)
    news = {
        'text': df['text'][index],
        'title': df['title'][index],
        'date': df['date'][index],
        'url': df['url'][index]
    }
    return news


def draw_wordcloud(i: str, photo: bool, name=None):
    wordcloud = WordCloud(
            width = 1280,
            height = 720,
            # width = 320,
            # height = 240,
            background_color='white',
            max_words=100,
            max_font_size=200,
            scale=3,
            random_state=123,
            colormap='twilight')

    df = pd.read_csv('./static/lib/df_preprocess.csv')
    index = int(i)
    data = df['text_str'][index]
    wc = wordcloud.generate(data)
    fig = plt.figure(1, figsize=(20, 12))
    plt.axis('off')
    plt.imshow(wordcloud)
    if photo == True:
        plt.savefig(name, bbox_inches='tight')
    #plt.show()
    pngImage = io.BytesIO()
    fig.savefig(pngImage)
    pngImageb64String = base64.b64encode(pngImage.getvalue()).decode('ascii')

    return pngImageb64String


def generate_ngrams(text, n_gram=1):
    token = [token for token in text.split(' ')]
    ngrams = zip(*[token[i:] for i in range(n_gram)])
    return [' '.join(ngram) for ngram in ngrams]


def count_unigrams(i: str):
    df = pd.read_csv('./static/lib/df_preprocess.csv')
    index = int(i)
    data = df['text_str'][index]

    unigrams = defaultdict(int)
    for word in generate_ngrams(data, 1):
        unigrams[word] += 1

    df_unigrams = pd.DataFrame(sorted(unigrams.items(), key=lambda x: x[1])[::-1])
    N = 30
    unigrams_less_100 = df_unigrams[:N]

    fig, axes = plt.subplots(ncols=1, figsize=(10, N // 3), dpi=60)
    plt.tight_layout()
    sns.barplot(y=unigrams_less_100[0], x=unigrams_less_100[1], ax=axes, color='purple')
    axes.spines['right'].set_visible(False)
    axes.set_xlabel('')
    axes.set_ylabel('')
    axes.tick_params(axis='x', labelsize=17)
    axes.tick_params(axis='y', labelsize=17)
    axes.set_title(f'Топ {N} наиболее популярных слов в тексте', fontsize=20)
    axes.bar_label(axes.containers[0], size=13, padding=10)
    pngImage = io.BytesIO()
    fig.savefig(pngImage, bbox_inches='tight')
    pngImageb64String = base64.b64encode(pngImage.getvalue()).decode('ascii')

    return pngImageb64String


def count_topics(topics):
    topic_dict = dict(Counter(topics))
    topic_dict = sorted(topic_dict.items(), key=lambda item: item[1], reverse=True)

    y = [topic_dict[i][0] for i in range(len(topic_dict))]
    x = [topic_dict[i][1] for i in range(len(topic_dict))]

    fig, axes = plt.subplots(ncols=1, figsize=(12, 8), dpi=1200)
    #fig.set_size_inches(640, 480)
    plt.tight_layout()
    sns.barplot(x=x, y=y, ax=axes, palette="crest")
    axes.spines['right'].set_visible(False)
    axes.set_xlabel('')
    axes.set_ylabel('')
    axes.tick_params(axis='x', labelsize=17)
    axes.tick_params(axis='y', labelsize=17)
    axes.set_title('Популярные темы', fontsize=20)
    axes.bar_label(axes.containers[0], size=13, padding=10)
    pngImage = io.BytesIO()
    fig.savefig(pngImage, bbox_inches='tight', dpi=1200)
    pngImageb64String = base64.b64encode(pngImage.getvalue()).decode('ascii')

    return pngImageb64String
