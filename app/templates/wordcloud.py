import matplotlib.pyplot as plt
import io
import urllib, base64

from wordcloud import WordCloud, STOPWORDS
comment_words = ' '
stopwords = set(STOPWORDS) 

# iterate through the csv file 
for val in data1['Body Content']: 

   # typecaste each val to string 
   val = str(val) 

   # split the value 
   tokens = val.split() 

# Converts each token into lowercase 
for i in range(len(tokens)): 
    tokens[i] = tokens[i].lower() 

for words in tokens: 
    comment_words = comment_words + words + ' '


wordcloud = WordCloud(width = 800, height = 800, 
            background_color ='white', 
            stopwords = stopwords, 
            min_font_size = 10).generate(comment_words) 

# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show()
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")

image = io.BytesIO()
plt.savefig(image, format='png')
image.seek(0)  # rewind the data
string = base64.b64encode(image.read())

image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
