var http = require('http');

function onRequest(request, responce) {
    responce.writeHead(200, {'Content-Tuye': 'text/plain'});
    responce.write('Hello World');
    responce.end();
}

http.createServer(onRequest).listen(8000);