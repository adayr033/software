from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template ('Index.html')

@app.route('/Index.html')
def Index1():
    return render_template ('Index.html')

@app.route('/index.html')
def inicio():
    return render_template('inicio.html')

@app.route('/')
def registro():
    return render_template ('registro.html')

@app.route('/registro.html')
def registro2():
    return render_template ('registro.html')

@app.route('/')
def software():
    return render_template ('software.html')

@app.route('/software.html')
def software3():
    return render_template ('software.html')


@app.route('/')
def Contactanos():
    return render_template ('Contactanos.html')

@app.route('/Contactanos.html')
def Contactanos4():
    return render_template ('Contactanos.html')


if __name__== '__main__':
    app.run(debug=True)