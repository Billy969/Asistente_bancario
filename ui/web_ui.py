from flask import Flask, render_template, request, jsonify
from core.agent import BankingAgent

app = Flask(__name__)  # Asegúrate de que esta línea exista
agent = BankingAgent("data/faqs.json")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    query = request.form["query"]
    response = agent.handle_query(query)
    return jsonify({"response": response})

if __name__ == '__main__':
    # No necesitas esto aquí si main.py es el punto de entrada
    # app.run(debug=True)
    pass