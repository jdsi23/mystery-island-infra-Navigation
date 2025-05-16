from flask import Flask, request, jsonify

# Ensure static files are served correctly
app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/")
def home():
    return """
<html>
<head>
    <title>Mystery Island Navigation</title>
    <style>
        .map-container {
            position: relative;
            display: inline-block;
        }
        .icon {
            position: absolute;
            width: 70px;
            cursor: pointer;
            transition: transform 0.2s ease;
        }
        .icon:hover {
            transform: scale(1.3);
            z-index: 2;
        }
        #directions {
            margin-top: 20px;
            font-family: sans-serif;
            padding: 10px;
            border: 1px solid #aaa;
            width: 60%;
            background: #f7f7f7;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    <script>
        async function getDirections(destination) {
            const res = await fetch(`/directions?to=${destination}`);
            const data = await res.json();
            let html = `<h3>Route to ${data.destination}</h3><ol>`;
            data.route.forEach(step => {
                html += `<li>${step}</li>`;
            });
            html += `</ol>`;
            document.getElementById("directions").innerHTML = html;
        }
    </script>
</head>
<body style="text-align:center;">
    <h1>🗺️ Welcome to Mystery Island</h1>

    <div class="map-container">
        <img src="https://i.postimg.cc/7hTkGYNG/map.png" alt="Mystery Island Map" style="width:90%;">

        <img src="https://i.postimg.cc/HswLBBQJ/icon-volcano.png" class="icon"
             title="🔥 Ashen Secrets 🔥"
             style="top: 100px; left:150px;" onclick="getDirections('volcano')">

        <img src="https://i.postimg.cc/nr8H1DrY/icon-maze.png" class="icon"
             title="🌿 Maze of Whisper 🌿"
             style="top:410px; left:135px;" onclick="getDirections('maze')">

        <img src="https://i.postimg.cc/J7B0B105/icon-boat.png" class="icon"
             title="🚤 The Forgotten Current 🚤"
             style="top:450px; left:600px;" onclick="getDirections('boat')">

        <img src="https://i.postimg.cc/QdNjSs8P/icon-resort.png" class="icon"
             title="🌺 Secrets of the Sands 🌺"
             style="top:80px; left:600px;" onclick="getDirections('resort')">
    </div>

    <div id="directions"></div>
</body>
</html>
"""

@app.route("/status")
def status():
    return jsonify({"status": "running", "service": "navigation"})

@app.route("/directions")
def directions():
    location = request.args.get("to", "unknown")
    steps = {
        "volcano": ["Start at entrance", "Head north", "Follow the lava trail", "Arrive at Volcano Ride!"],
        "maze": ["Enter forest", "Turn left at ruins", "Arrive at Maze Garden!"],
        "boat": ["Go south", "Cross stone bridge", "Dock at Pirate Ship Ride!"],
        "resort": ["Follow river east", "Pass glowing portals", "Welcome to Resort Towers!"]
    }
    return jsonify({
        "destination": location,
        "route": steps.get(location.lower(), ["Destination unknown"])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
