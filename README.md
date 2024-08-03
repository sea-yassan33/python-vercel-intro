## python(Flasks)をVarcelにデプロイする方法

### 用意するファイル
```
.project_direct
|-- index.py
|-- requirements.txt
|-- vercel.json
```

### GitHubリポジトリにアップロード

### アップロードしたリポジトリをvercelにデプロイ
- Frameworke Preset :Other

### 環境変数の設定について
#### ローカル上での環境変数の設定
```python
import os
from dotenv import load_dotenv

# ローカル環境の場合、.envファイルから環境変数をロード
if os.getenv('FLASK_ENV') == 'development':
    load_dotenv()
```

#### vercelの環境変数の設定
- Settings
- Enciroment Varilables