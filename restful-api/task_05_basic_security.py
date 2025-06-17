#!/usr/bin/python3
"""
This is about learning API security and authentication techniques
"""


from flask import Flask
# HTTPBasicAuth is a class from Flask-HTTPAuth for handling basic username/password authentication
from flask_httpauth import HTTPBasicAuth
# gen password - turns a plain password into a secure hashed version
# check password - compares a stored hash with a plain password to verify if they match
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


app = Flask(__name__)
# sets up basic autheincation handling
auth = HTTPBasicAuth()
# sets a configuration option for the flask app
app.config["JWT_SECRET_KEY"] = "your-secret-key"
# initialises the JWT extension with flask app
jwt = JWTManager(app)

# dictionary that stores users' info
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


# function to verify credentials - ie passwords
@auth.verify_password
# checks if username exists in users dictionary and if the entered password matches the stored hashed password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users[username]["password"], password):
        return (users[username])

@auth.error_response
def auth_error_response():
    return (jsonify({"error": "Unauthorized access"}), 401)


# basic protected creates a route available at /basic-protected
@app.route("/basic-protected")
# enforces authentication
@auth.login_required
# gets called when someone visits the url
def basic_protected():
    return ("Basic Auth: Access Granted")


@app.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users or not check_password_hash(users[username]["password"], password):
        return (jsonify({"error": "Invalid credentials"}), 401)

    access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
    return (jsonify(access_token=access_token))

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return ("JWT Auth: Access Granted")


@app.route("/admin-only")
@jwt_required()
def admin_only():
    user = get_jwt_identity()
    if user["role"] != "admin":
        return (jsonify({"error": "Admin access required"}), 403)
    return ("Admin Access: Granted")

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)