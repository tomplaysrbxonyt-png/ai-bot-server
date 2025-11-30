from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").lower()

    # IA simple (tu peux améliorer)
    if "bonjour" in message:
        reply = "Salut ! Comment puis-je t'aider ?"
    elif "qui es tu" in message:
        reply = "Je suis un bot IA dans ton jeu Roblox !"
    elif "aide" in message:
        reply = "Bien sûr, je suis là pour t'aider."
    else:
        reply = "Je n'ai pas compris, mais je vais m'améliorer !"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
