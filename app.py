from bottle import route, run, template, request, post

@post('/hello/<name>')
def index(name):
    print(request.body)
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='10.10.21.35', port=8080)
