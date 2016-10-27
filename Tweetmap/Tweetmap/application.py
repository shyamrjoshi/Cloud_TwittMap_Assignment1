from flask import Flask, render_template, request
import search
import twittstream
application = Flask(__name__)
@application.route("/", methods=['GET', 'POST'])
def main():
    twittstream.main()
    if request.method == "POST":
        tag = request.form.get("tags")
        locations = search.search(tag)
        return render_template("TwittMap.html", locs = locations)
    else:
        return render_template("TwittMap.html", locs=[])
if __name__ == "__main__":
    application.run(host='127.0.0.2')
