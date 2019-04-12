var jwt = require('jsonwebtoken');

class jwtConfig{
    constructor(){}
    verifyJWTToken(token) {
        return new Promise((resolve, reject) => {
            jwt.verify(token, "asdfg", (err, decodedToken) =>  {
                if (err || !decodedToken) {
                    return reject(err);
                }

                resolve(decodedToken);
            });
        });
    }

    createJWToken(details) {
        if (typeof details !== 'object') {
            details = {};
        }

        let token = jwt.sign({
                data: details
            }, "asdfg", {
            expiresIn: 3600
        });

        return token;
    }
}

var jwtC = new jwtConfig();

