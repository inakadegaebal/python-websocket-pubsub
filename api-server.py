from flask import Flask
import redis

app = Flask(__name__)

@app.route("/pushpage/")
def pushpage():
    return "<form action='/push'><input type='submit'></form>"

@app.route("/push/")
def push():
    redis_con = redis.Redis(host='localhost')
    redis_con.publish('user_id_1', 'hello') # チャンネル名は引数にする必要ある

    return "pushed!!"

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0')