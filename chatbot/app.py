from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").lower()

    responses = {
        "hello": "Hey there! I'm Finn — need help finding a ride?",
        "hi": "Hey there! I'm Finn — need help finding a ride?",
        "hey": "Hey there! I'm Finn — need help finding a ride?",
        "volcano": "Ashen Secrets is that way! Follow the lava flow north.",
        "ashen secrets": "Ashen Secrets is that way! Follow the lava flow north.",
        "boat": "Ahoy! The Pirate Ship sails south of the resort bridge.",
        "the forgotten current": "Ahoy! The Pirate Ship sails south of the resort bridge.",
        "pirate ship": "Ahoy! The Pirate Ship sails south of the resort bridge.",
        "maze": "The Maze of Whispers is hidden past the stone archway.",
        "maze of whisper": "The Maze of Whispers is hidden past the stone archway.",
        "whisper maze": "The Maze of Whispers is hidden past the stone archway.",
        "resort": "Tiki Resort is just beyond the glowing portals!",
        "secrets of the sands": "Tiki Resort is just beyond the glowing portals!",
        "tiki resort": "Tiki Resort is just beyond the glowing portals!",
        "maze": "The Maze of Whispers is hidden past the stone archway.",
        "maze of whisper": "The Maze of Whispers is hidden past the stone archway.",
        "resort": "Tiki Resort is just beyond the glowing portals!",
        "secrets of the sands": "Tiki Resort is just beyond the glowing portals!",
        "map": "You can find the full Mystery Island map on the homepage.",
        "directions": "You can find the full Mystery Island map on the homepage.",
        "food": "Try the Jungle Café near the central hut for some snacks!"
    }

    for key, reply in responses.items():
        if key in message:
            return jsonify({"reply": reply})

    return jsonify({"reply": "Hmm, I’m not sure. Try asking about the volcano, boat, maze, or food!"})

@app.route("/status")
def status():
    return {"status": "running", "service": "chatbot"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)


@app.route("/", methods=["GET"])
def health_check():
    return "OK", 200
