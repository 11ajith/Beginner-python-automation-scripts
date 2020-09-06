# Generating a word cloud from the given text 

from wordcloud import WordCloud

background_color = "#101010"
height = 720
width = 1080

with open("specify the path of the text file", "r") as f:
    words = f.read().split()

data = dict()

for word in words:
    word = word.lower()
    data[word] = data.get(word, 0) + 1

word_cloud = WordCloud(
    background_color=background_color,
    width=width,
    height=height
)

word_cloud.generate_from_frequencies(data)
word_cloud.to_file('image.png')