from flask import Flask, request, render_template
from lawBot import *

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/index')
def index():
    f = open("search_page.html", 'r')
    page=f.read()
    f.close()
    return page


@app.route('/search')
def query():
    query = request.args.get('q')
    if query is None:
        return "hello, you searched nothing"
    else:
        print(query[1:-1])

        #make the query
        
        answer, rely, link = lawBot(query)
        print(answer, rely, link)

        return render_template('result_page.html', answer=answer, reliability=round(rely, 3), link=link, query=query)
        return "hello, you searched:<br>\n"+query+'<br>\n<br>\n'+"<a href="+link+">official sources</a>"+answer+rely


if __name__ == "__main__":
    app.run()
