from flask import render_template, url_for, redirect
from flask_login import login_required, login_user

from fakepin import app, database, bcrypt
from fakepin.forms import formLogin, formCriarConta
from fakepin.models import Usuario


@app.route('/', methods=['GET', 'POST'])
def homescreen():
    formLoginlogin = formLogin()
    return render_template('homescreen.html', form=formLoginlogin)


@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    createConta = formCriarConta()
    if createConta.validate_on_submit():
        print('teste')
        senha = bcrypt.generate_password_hash(createConta.senha.data).decode('utf-8')
        usuario = Usuario(username=createConta.username.data,
                          email=createConta.email.data, senha=senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario)
        return redirect(url_for('perfil', usuario=createConta.username.data))
    return render_template('criarconta.html', form=createConta)


@app.route('/perfil/<usuario>')
@login_required
def atualizar(usuario):
    return render_template('perfil.html', usuario=usuario)
