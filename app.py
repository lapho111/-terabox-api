from flask import Flask, request, jsonify
from cfscrape import create_scraper

app = Flask(__name__)
session = create_scraper()

@app.route("/terabox")
def terabox():
    url = request.args.get("url")

    try:
        res = session.get(url)
        key = res.url.split("?surl=")[-1]

        api = f"https://www.terabox.com/share/list?app_id=250528&shorturl={key}&root=1"
        r = session.get(api)

        data = r.json()
        dlink = data["list"][0]["dlink"]

        return jsonify({"dlink": dlink})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()
