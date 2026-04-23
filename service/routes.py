from flask import abort
from flask import jsonify
from flask import request

from service import app

accounts = {}
next_id = 1


@app.route("/accounts", methods=["POST"])
def create_account():
    global next_id
    data = request.get_json()
    if not data or "name" not in data:
        abort(400)
    account = {
        "id": next_id,
        "name": data["name"],
        "email": data.get("email", ""),
        "address": data.get("address", ""),
        "phone_number": data.get("phone_number", ""),
        "date_joined": data.get("date_joined", ""),
    }
    accounts[next_id] = account
    next_id += 1
    return jsonify(account), 201


@app.route("/accounts", methods=["GET"])
def list_accounts():
    return jsonify(list(accounts.values())), 200


@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    account = accounts.get(account_id)
    if not account:
        abort(404)
    return jsonify(account), 200


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    account = accounts.get(account_id)
    if not account:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400)
    for field in ["name", "email", "address", "phone_number", "date_joined"]:
        if field in data:
            account[field] = data[field]
    accounts[account_id] = account
    return jsonify(account), 200


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    account = accounts.pop(account_id, None)
    if not account:
        abort(404)
    return "", 204
