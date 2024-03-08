from influxdb import InfluxDBClient

# InfluxDB データベースに接続する
# client = InfluxDBClient(host='74.226.208.84', port=8086, username=None, password=None, database='test_db')
client = InfluxDBClient(host='4.216.59.33', port=8086, username='zhang', password='zhang', database='test_db')


# データを書き込む
json_body = [
    {
        "measurement": "test_m",
        "tags": {
            "tag1": "戦国名将"
        },
        "fields": {
            "name": "豊臣秀吉",
            "age": 22
        }
    }
]
client.write_points(json_body)

# データをクエリする（読み込み）
result = client.query('SELECT * FROM test_m LIMIT 5')
print("クエリ結果: {0}".format(result))

# 接続を閉じる
client.close()
