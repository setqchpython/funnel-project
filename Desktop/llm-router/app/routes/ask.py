import asyncio
from flask import Blueprint, request, jsonify

from app.services.router import Router
from app.providers.gemini import GeminiProvider
from app.providers.mistral import MistralProvider



ask_bp = Blueprint("ask", __name__)

providers = [
    GeminiProvider(),
    MistralProvider(),
]

router = Router(providers)

@ask_bp.route("/ask", methods=["POST"])
def ask():
    prompt = request.json["prompt"]

    results = asyncio.run(router.ask_all(prompt))

    return jsonify({
        "prompt": prompt,
        "results": results
    })