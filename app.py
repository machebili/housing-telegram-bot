from flask import Flask
import threading
import bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

threading.Thread(target=bot).start()

if __name__ == "__main__":
    app.run()
