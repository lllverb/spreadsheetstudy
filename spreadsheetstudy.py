import gspread
import settings

# ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

SSK = settings.SSK
JSN = settings.JSN


# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

# 認証情報設定
# ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSN, scope)

# OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

# 共有設定したスプレッドシートキーを変数SPREADSHEET_KEYに格納する。
SPREADSHEET_KEY = SSK

# スプレッドシートのシート1を開く。
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

# A1の値を入手、数値化
import_value = int(worksheet.acell("A1").value)

# A1に100を足す。
export_value = import_value + 100

# 縦、横の順番。1,2は縦が1横がBつまりB1に書き出す
worksheet.update_cell(1, 2, export_value)
