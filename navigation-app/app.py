from flask import Flask, render_template, request, jsonify

# Set up Flask with proper static/template paths
app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")  # ✅ Uses your updated HTML + Tailwind

@app.route("/directions")
def directions():
    destination = request.args.get("to")
    route_data = {
        "destination": destination,
        "route": [
            "Walk to the nearest portal",
            "Enter the mystic forest",
            f"Proceed to {destination}"
        ]
    }
    return jsonify(route_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
