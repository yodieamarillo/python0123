from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index(res=None):
    return render_template('index.html')
###agregamos la ruta a la cual se va enviar la inforamacion del formulario 
def formData(res):
    return render_template('response.html',res)


if __name__=='__main__':
    app.run(debug=True)
