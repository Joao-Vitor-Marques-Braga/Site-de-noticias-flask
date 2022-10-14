from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Notícias:
    def __init__(self, titulo, descrição, materia, imagem1, imagem2, imagem3, autor):
        self.titulo = titulo
        self.descrição = descrição
        self.materia = materia
        self.imagem1 = imagem1
        self.imagem2 = imagem2
        self.imagem3 = imagem3
        self.autor = autor
lista = list()

@app.route('/')
def home():
    if len(lista) == 0:
        return "Página em Manutenção"
    else:
        return render_template('index.html', lista=lista)

@app.route('/publicar')
def publicar():
    return render_template('publicar.html')

@app.route('/inserir', methods=['POST'])
def inserir():
    titulo = request.form['titulo']
    descrição = request.form['descricao']
    materia = request.form['materia']
    imagem1 = request.form['img1']
    imagem2 = request.form['img2']
    imagem3 = request.form['img3']
    autor = request.form['autor']

    obj = Notícias(titulo, descrição, materia, imagem1, imagem2, imagem3, autor)

    lista.append(obj)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)