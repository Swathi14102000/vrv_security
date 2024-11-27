from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Mock data for users and roles
users = [
    {"id": 1, "name": "Alice", "role": "Admin", "status": "Active"},
    {"id": 2, "name": "Bob", "role": "Editor", "status": "Inactive"},
]

roles = [
    {"id": 1, "name": "Admin", "permissions": ["Read", "Write", "Delete"]},
    {"id": 2, "name": "Editor", "permissions": ["Read", "Write"]},
    {"id": 3, "name": "Viewer", "permissions": ["Read"]},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/manage-users", methods=["GET", "POST"])
def manage_users():
    if request.method == "POST":
        new_user = {
            "id": len(users) + 1,
            "name": request.form["name"],
            "role": request.form["role"],
            "status": request.form["status"]
        }
        users.append(new_user)
        return redirect(url_for("manage_users"))
    return render_template("manage_users.html", users=users, roles=roles)

@app.route("/manage-roles", methods=["GET", "POST"])
def manage_roles():
    if request.method == "POST":
        new_role = {
            "id": len(roles) + 1,
            "name": request.form["name"],
            "permissions": request.form.getlist("permissions"),
        }
        roles.append(new_role)
        return redirect(url_for("manage_roles"))
    return render_template("manage_roles.html", roles=roles)

@app.route("/api/users", methods=["GET"])
def api_users():
    return jsonify(users)

@app.route("/api/roles", methods=["GET"])
def api_roles():
    return jsonify(roles)

if __name__ == "__main__":
    app.run(debug=True)
