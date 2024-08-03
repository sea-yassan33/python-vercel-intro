from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
# UTF-8に変換（日本語をJSONで返す場合は必要）
app.config["JSON_AS_ASCII"] = False
# アプリ全体に対してCORSを有効化にする
CORS(app)

# ローカル環境の場合、.envファイルから環境変数をロード
# from dotenv import load_dotenv
# if os.getenv('FLASK_ENV') == 'development':
#     load_dotenv()

env_integer = os.getenv('TEST_STRING')

@app.route("/")
def hello_world():
   return f"<p>こんにちは、{env_integer}!</p>"

# アプリケーションを実行
if __name__ == '__main__':
    app.run(debug=True)