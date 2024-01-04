from flask import Flask,render_template, request, session, redirect
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug import secure_filename
import json


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'

# if(local_server):
#     app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/test"
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/test"

# db = SQLAlchemy(app)

# class Certificates(db.Model):
#     daysleft=db.Column(db.integer,nullable=False)
#     name=db.Column(db.String(50),nullable=False)
#     category=db.Column(db.String(50),nullable=False)
#     expiry=db.Column(db.Date,nullable=False)

localuser="R0013"


@app.route("/certificate_status")
def home():
    if params['user_role1']==localuser:
        return render_template("certificate_status.html",user=localuser)
    elif params['user_role2']==localuser:
        return render_template("certificate_status.html",user=localuser)
    elif params['user_role3']==localuser:
        return render_template("certificate_status.html",user=localuser)
    elif params['user_role4']==localuser:
        return render_template("certificate_status.html",user=localuser)
    elif params['user_role5']==localuser:
        return render_template("certificate_status.html",user=localuser)
    elif params['user_role6']==localuser:
        return render_template("certificate_status.html",user=localuser)
    elif params['user_role7']==localuser:
        return render_template("certificate_status.html",user=localuser)
    elif params['user_role8']==localuser:
        return render_template("certificate_status.html",user=localuser)
    elif params['user_role9']==localuser:
        return render_template("certificate_status.html",user=localuser)
    return render_template("certificate_status.html")



if __name__=="__main__":
    app.run(debug=True)


