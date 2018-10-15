var http = require('http');
var fs = require('fs');

function onRequest(request, responce) {
    responce.writeHead(200, {'Content-Tuye': 'text/html'});
    fs.readFile('./index.html', null, function(error, data) {
        if(error) {
            responce.writeHead(404);
            responce.write('File not found'); 
        } else {
            responce.write(data);
        }
        responce.end();
    });
}

http.createServer(onRequest).listen(8000);