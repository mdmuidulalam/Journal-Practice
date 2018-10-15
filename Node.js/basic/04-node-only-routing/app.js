var url = require('url');
var fs = require('fs');

function renderHTML(path, responce) {
    fs.readFile(path, null, function(error, data) {
        if(error) {
            responce.writeHead(404);
            responce.write('File not found'); 
        } else {
            responce.write(data);
        }
        responce.end();
    });
}

module.exports = {
    handleRequest: function(request, responce) {
        responce.writeHead(200, {'Content-Tuye': 'text/html'});

        var path = url.parse(request.url).pathname;

        switch(path){
            case '/':
                renderHTML('./index.html', responce);
                break
            case '/login':
                renderHTML('./login.html', responce); 
            default: 
                responce.writeHead(404);
                responce.write('Route not found');
                responce.end();
        }
    }
}