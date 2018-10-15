var http = require('http');
var module1 = require('./module1');

function onRequest(request, responce) {
    responce.writeHead(200, {'Content-Tuye': 'text/plain'});
    responce.write(module1.myString);
    module1.myFunction();
    responce.end();
}

http.createServer(onRequest).listen(8000);