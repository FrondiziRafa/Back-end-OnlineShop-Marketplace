from flask_restful import Resource, reqparse
from models.produto import ProdutoModel


class Produtos(Resource):

    def get(self):
        return {"produtos": [produto.json() for produto in ProdutoModel.query.all()]}

class Produto(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('genero', type=str,required= True, help= " O campo 'Gênero' precisa ser preenchido")
    argumentos.add_argument('secao', type=str,required= True, help= " O campo 'Seção' precisa ser preenchido")
    argumentos.add_argument('categoria', type=str,required= True, help= " O campo 'Categoria' precisa ser preenchido")
    argumentos.add_argument('estilo', type=str,required= True, help= " O campo 'Estilo' precisa ser preenchido")
    argumentos.add_argument('nome', type=str,required= True, help= " O campo 'Nome' precisa ser preenchido")
    argumentos.add_argument('descricao', type=str,)
    argumentos.add_argument('qtd_estoque', type=int,required= True, help= " O campo 'Quantidade em estoque' precisa ser preenchido")
    argumentos.add_argument('cor', type=str,required= True, help= " O campo 'Cor' precisa ser preenchido")
    argumentos.add_argument('tamanho', type=str,required= True, help= " O campo 'Tamanho' precisa ser preenchido")
    argumentos.add_argument('preco', type=float,required= True, help= " O campo 'Preço' precisa ser preenchido")

    def get(self, produto_id):
        
        produto = ProdutoModel.buscar_produtos(produto_id)
        if produto:
            return produto.json()
        return {'mensagem': 'Produto não encontrado.'}, 404

    def post(self, produto_id):

        if ProdutoModel.buscar_produtos(produto_id):
            return {"mensagem":"Produto '{}' já existente !".format(produto_id)}, 404

        dados = Produto.argumentos.parse_args()
        produto = ProdutoModel(produto_id, **dados)
        try:
            produto.salvar_produto()
        except:
            return {"mensagem":"Ocorreu um erro interno"}, 500
        return produto.json()

    def put(self, produto_id):
        
        dados = Produto.argumentos.parse_args()

        produto_encontrado = ProdutoModel.buscar_produtos(produto_id)
        if produto_encontrado:
            produto_encontrado.atualizar_produto(**dados)
            produto_encontrado.salvar_produto()
            return produto_encontrado.json(), 200

        produto = ProdutoModel( produto_id, **dados )

        try:
            # return {"Mensagem":"Aoba"}
            produto.salvar_produto()
        except:
            return {"Ocorreu um erro interno"}, 500
        return produto.json(), 201

    def delete(self, produto_id):
        produto = ProdutoModel.buscar_produtos(produto_id)
        if produto:
            try:
                produto.deletar_produto()
            except:
                return {"mensagem":"Ocorreu um erro interno"}, 500
            return{"mensagem": "Produto deletado com sucesso"}
        return{"mensagem":"Produto não encontrado"}