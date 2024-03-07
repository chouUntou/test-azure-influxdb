from influxdb import InfluxDBClient

# InfluxDB データベースに接続する
# client = InfluxDBClient(host='74.226.208.84', port=8086, username=None, password=None, database='test_db')
client = InfluxDBClient(host='4.216.59.33', port=8086, username='zhang', password='zhang', database='test_db')

# データをクエリする
#result = client.query('SELECT * FROM test_m LIMIT 5')
#print("クエリ結果: {0}".format(result))

# データを書き込む
json_body = [
    {
        "measurement": "test_m_1",
        "tags": {
            "tag1": "name",
            "tag2": "age"
        },
        "fields": {
            "field1": "張",
            "field2": 18
        }
    }
]
client.write_points(json_body)

# 接続を閉じる
client.close()
