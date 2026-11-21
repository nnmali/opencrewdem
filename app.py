
from flask import Flask, jsonify, request

app = Flask(__name__)

team = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]


@app.route("/")
def home():
    return jsonify({"message": "Welcome to OpenCrew"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/team", methods=["GET"])
def get_team():
    return jsonify(team)


@app.route("/team", methods=["POST"])
def add_team_member():
    data = request.get_json()

    member = {
        "id": len(team) + 1,
        "name": data["name"]
    }

    team.append(member)

    return jsonify(member), 201


if __name__ == "__main__":
    app.run(debug=True)
