from flask import Flask, render_template
from doc2vec import *
import sys

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    return render_template('articles.html', my_list=Alist)


@app.route("/article/<topic>/<filename>")
def article(topic,filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """
    for art in articles_table:
        if art[0]== "%s/%s" %(topic, filename):
            title_str = art[1]
            text_list = art[2].split('\n')
            text_list = [t.lower() for t in text_list if len(t) >= 1]
            rec = recommended(art[0], articles_table, 5)
            break
    return render_template('article.html', title=title_str, text=text_list, fiveA= rec) # link= , 5articles=)


# initialization
glove_filename =  'data/glove.6B.50d.txt' #sys.argv[1]
articles_dirname = 'data/bbc' #sys.argv[2]

gloves = load_glove(glove_filename)
articles_table = load_articles(articles_dirname, gloves)
Alist = []
for art in articles_table:
    Alist.append((art[1], art[0]))

if __name__ == '__main__':
    app.debug = True
    app.run()
#app.run(host='localhost', port=80)

