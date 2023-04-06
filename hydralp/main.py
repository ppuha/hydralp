from flask import Flask, request, render_template, redirect, url_for
from hydra import accept_login, get_consent, accept_consent
from pg import query
from config import get_config

app = Flask(__name__)
config = get_config(app.root_path + "/static/db.yaml")

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET":
    challenge = request.args.get("login_challenge")
    return render_template("login.jinja", challenge=challenge)
  else:
    challenge = request.form.get("challenge")
    username = request.form.get("username")
    password = request.form.get("password")

    user = query(username, password, config)
    if user == None:
      return redirect(url_for("login"))
    
    extras = dict(zip(config["extra"].values(), list(user)[2:]))

    res = accept_login(challenge, username, extras)

    return redirect(res['redirect_to'])
  
@app.route("/consent")
def consent():
  challenge = request.args.get("consent_challenge")
  consent = get_consent(challenge)
  res = accept_consent(challenge, consent["context"])

  return redirect(res['redirect_to'])

app.run(port=3000, debug=True)
