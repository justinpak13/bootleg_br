from operator import mod
from flask import Flask
from flask import render_template
from flaskext.markdown import Markdown 
from transform import transform
from make_url import make_url
import codecs
import io

#adjustements 
font_size = 27

#choose 100-900
boldness = 800


# Init App 
app = Flask(__name__)

@app.route("/")
def index():
    raw_text = io.open('input.txt', mode='r', encoding='utf-8')

    text_list = [] 
    holder = [] 
    for i in raw_text:
        if i != '\n':
            holder.append(i)
        else:
            text_list.append(' '.join(holder))
            holder = []
    text_list.append(' '.join(holder))


    bionic_text = '<br>\n<br> '.join([transform(chunk) for chunk in text_list])

    html = make_url(boldness, font_size, bionic_text)

    with codecs.open('templates/index.html', 'w', "utf-8-sig") as output:
        output.write(html)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)