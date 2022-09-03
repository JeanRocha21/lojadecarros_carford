from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.forms import Cadastro
from app.models.tables import Client

@app.route('/') #route = indica o endereço do site, todas as paginas do site devem ter
def index():
    return render_template('index.html')

@app.route("/register", methods= ["GET", "POST"])
def register():
    form = Cadastro()
    if form.validate_on_submit():
        c = Client(None,None,None,None,None,None,None)

        form.populate_obj(c)
        db.session.add(c)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('register.html', form=form)

@app.route('/list')
def list():
    clientes = Client.query.all()
    return render_template("list.html", clientes=clientes)