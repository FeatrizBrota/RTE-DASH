from flask import Flask, render_template, jsonify
from flask_cors import CORS
import queries



#comentario
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    # Consultar o banco de dados dev
    _dev = queries.q_cenarios_gerados_dev()
    resultados_prod = queries.q_cenarios_gerados_prod()

@app.route('/dados')
def get_dados():
    # Consultar o banco de dados dev
    cenarios_dev = queries.q_cenarios_gerados_dev()
    cenarios_prod = queries.q_cenarios_gerados_prod()
    acessos_prod = queries.q_total_acessos_prod()
    acessos_dev = queries.q_total_acessos_dev()
    empresas_dev=queries.q_empresas_criadas_dev()
    empresas_prod=queries.q_empresas_criadas_prod()
    monitoria_dev = queries.total_monitoria_dev()
    monitoria_prod = queries.total_monitoria_prod()
    dados = {
        'cenarios_dev': cenarios_dev,
        'cenarios_prod': cenarios_prod,
        'acessos_prod':acessos_prod,
        'acessos_dev':acessos_dev,
        'empresas_dev':empresas_dev,
        'empresas_prod':empresas_prod,
        'monitoria_dev':monitoria_dev,
        'monitoria_prod':monitoria_prod

    }
    return jsonify(dados)

if __name__ == '__main__':
    app.run()
