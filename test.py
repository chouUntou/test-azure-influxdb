from influxdb import InfluxDBClient

# 環境変数からInfluxDBの接続情報を取得
host = os.environ['INFLUXDB_HOST']
port = os.environ['INFLUXDB_PORT']
username = os.environ['INFLUXDB_USERNAME']
password = os.environ['INFLUXDB_PASSWORD']
database = os.environ['INFLUXDB_DATABASE']

# InfluxDBに接続
client = InfluxDBClient(host=host, port=port, username=username, password=password, database=database)

# データを書き込む
data = [{
    "measurement": "cpu_load_short",
    "tags": {
        "host": "server01",
        "region": "jp-east"
    },
    "fields": {
        "value": 0.64
    }
}]
client.write_points(data)

# データを読み込む
result = client.query('SELECT * FROM "cpu_load_short"')
print(result)
