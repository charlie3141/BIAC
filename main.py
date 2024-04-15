from flask import Flask, request, render_template, jsonify, redirect
from config import app,db
from models import Users

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/dangnhap", methods=["GET","POST"])
def login(): 
    email = request.json.get("email")
    pwd = request.json.get("pwd")
    if not email or not pwd : 
        return jsonify({"message": "information can't be null"}),400
    User = Users.query.all()
    json_User = list(map(lambda x : x.to_json(),User))
    data = jsonify({"user": json_User})
    
            

@app.route("/dangky", methods = ["POST","GET"])
def dang_ky():
    '''User = Users.query.all()
    json_User = list(map(lambda x : x.to_json(),User))
    data = jsonify({"user": json_User})'''
    if request.method == "POST" : 
        name = request.form["username"]
        email = request.form["email"]
        pwd = request.form["password"]
        if not email or not pwd : 
            return jsonify({"message": "information can't be null"}),400
        newUser = Users(name = name, email = email, pwd = pwd)
        try : 
            db.session.add(newUser)
            db.session.commit()
        except Exception as e :
            return jsonify({"message": str(e)}),400
    return render_template("signup.html")

@app.route("/test")
def test():
    return render_template("signup.html")
if __name__ == "__main__": 
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)