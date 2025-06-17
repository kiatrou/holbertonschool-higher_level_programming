#!/usr/bin/python3
"""
This is about learning API security and authentication techniques
"""

from flask import Flask, request, jsonify
# HTTPBasicAuth is a class from Flask-HTTPAuth for handling basic username/password authentication
from flask_httpauth import HTTPBasicAuth
# gen password - turns a plain password into a secure hashed version
# check password - compares a stored hash with a plain password to verify if they match
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

app = Flask(__name__)
# sets up basic authentication handling
auth = HTTPBasicAuth()
# sets a configuration option for the flask app - FIXED: should be JWT_SECRET_KEY
app.config["JWT_SECRET_KEY"] = "your-secret-key"
# initialises the JWT extension with flask app
jwt = JWTManager(app)

# dictionary that stores users' info
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# JWT Error Handlers - Return 401 for all authentication errors
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

# function to verify credentials - ie passwords
@auth.verify_password
def verify_password(username, password):
    # checks if username exists in users dictionary and if the entered password matches the stored hashed password
    if username in users and \
            check_password_hash(users[username]["password"], password):
        return users[username]  # Return the user object
    return False  # Return False if authentication fails

# Custom error handler for basic auth
@auth.error_handler
def auth_error(status):
    return jsonify({"error": "Unauthorized access"}), 401

# Basic Authentication Route
@app.route("/basic-protected")
@auth.login_required  # ADDED: This decorator was missing
def basic_protected():
    return "Basic Auth: Access Granted"

# JWT Login Route
@app.route("/login", methods=["POST"])
def user_login():
    # Get JSON data from request
    data = request.get_json()
    
    # Check if required fields are present
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password required"}), 400
    
    username = data['username']
    password = data['password']
    
    # Verify credentials
    if username in users and check_password_hash(users[username]["password"], password):
        # Create JWT token with user info embedded
        additional_claims = {
            "username": username,
            "role": users[username]["role"]
        }
        access_token = create_access_token(
            identity=username,
            additional_claims=additional_claims
        )
        return jsonify({"access_token": access_token})
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# JWT Protected Route
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Admin-Only Route (Role-based Access Control)
@app.route("/admin-only")
@jwt_required()
def admin_only():
    # Get current user's identity and claims
    current_user = get_jwt_identity()
    claims = get_jwt()
    
    # Check if user has admin role
    if claims.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"

# Test route to verify server is running
@app.route("/")
def home():
    return jsonify({"message": "API is running", "endpoints": [
        "/basic-protected (GET) - Basic Auth required",
        "/login (POST) - Login to get JWT token", 
        "/jwt-protected (GET) - JWT token required",
        "/admin-only (GET) - Admin JWT token required"
    ]})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)