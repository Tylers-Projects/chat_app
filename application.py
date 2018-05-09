from flask import Flask, render_template

app = Flask(__name__)


# The main route, which will direct users to go to the chatroom.
@app.route("/")
def index():
    names = ["Tyler", "Fred", "Brian"]
    return render_template("index.html", names=names)


# The chatroom, where users will send messages to each other.
@app.route("/chat_room")
def chat_room():
    return render_template("chat_room.html")

# Runs the app
if __name__ == "__main__":
    app.debug = True
    app.run()
