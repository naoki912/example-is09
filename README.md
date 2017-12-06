# example-is09
Example of carrier design for is09

## 実行方法

```
git clone https://github.com/naoki912/example-is09.git
cd example-is09/src
python app.py
```

## 設定

`example-is09/src/config.py` で設定を変更できます。

- `HOST`: string
  - リクエストを受け付けるIPアドレス
  - `0.0.0.0` で全てのIPアドレスでリクエストを受け付けます。
- `PORT`: int
  - リクエストを受け付けるポート番号
- `DEBUG`: bool
  - デバッグメッセージを出力するかしないか
- `DB`
  - `TYPE`: string
    - 使用するDBMS
  - `NAME`:
    - データベース名
- `DEFAULT_BALANCE`: int
  - gift code作成時に、gift codeに設定するデフォルト残高
