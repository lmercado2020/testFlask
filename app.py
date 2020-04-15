from flask import Flask, request, jsonify
from ClientRemote import ClientRemote
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/ping', methods=['GET'])
def ping():
    user= request.args['user']
    password = request.args['pass']
    host = request.args['host']
    dest = request.args['dest']
    c_paq= request.args['cp']

    cliente = ClientRemote(host,user,password)
    cliente.realice_ping(c_paq,dest)
    lista_result = cliente.get_result()
    print(lista_result[len(lista_result)-2])
    cliente.realice_traceroute(dest)
    result = cliente.get_result()
    return  jsonify({'result': lista_result[len(lista_result)-2]+'traceroute: '+ str(result)})


app.run(
  host = '0.0.0.0',
  debug = True,
  port = 8080
)

