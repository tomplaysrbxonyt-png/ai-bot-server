from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ai", methods=["POST"])
def ai_decision():
    data = request.json
    
    player_distance = data.get("playerDistance", 100)
    bot_health = data.get("botHealth", 100)

    # Petites décisions d'IA
    if bot_health < 30:
        action = "retreat"  # se retirer
    elif player_distance < 10:
        action = "attack"   # attaquer
    elif player_distance < 25:
        action = "chase"    # poursuivre
    else:
        action = "idle"     # attendre

    return jsonify({"action": action})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
