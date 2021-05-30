from flask import Blueprint, request, jsonify

from api import get_server


blueprint = Blueprint("default", __name__, url_prefix="/")


@blueprint.route("/ping")
def ping():
    server = get_server()
    result = server.request.futures_ping()
    return jsonify(result)


@blueprint.route("/time")
def time():
    server = get_server()
    result = server.request.futures_time()
    return jsonify(result)


@blueprint.route("/exchange-info")
def exchange_info():
    server = get_server()
    result = server.request.futures_exchange_info()
    return jsonify(result)


@blueprint.route("/stream", methods=("GET", "PUT", "DELETE"))
def stream():
    server = get_server()
    result = []

    if request.method == "GET":
        listen_key = server.request.futures_stream_get_listen_key()
        result = {"listenKey": listen_key}
    elif request.method == "PUT":
        listen_key = request.args.get("listenKey")
        result = server.request.futures_stream_keepalive(listenKey=listen_key)
    elif request.method == "DELETE":
        listen_key = request.args.get("listenKey")
        result = server.request.futures_stream_close(listenKey=listen_key)

    return jsonify(result)
