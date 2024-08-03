from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# UTF-8に変換（日本語をJSONで返す場合は必要）
app.config["JSON_AS_ASCII"] = False
# アプリ全体に対してCORSを有効化にする
CORS(app)

@app.route("/")
def hello_world():
   return "<p>こんにちは、python!</p>"

# アプリケーションを実行
if __name__ == '__main__':
    app.run(debug=True)