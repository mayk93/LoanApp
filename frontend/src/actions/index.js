import request from 'superagent';

let server = "http://localhost:8000/";
let login_endpoint = "api-token-auth/";


function login_liaison(data) {
    return {
        type: "TOKEN",
        payload: data
    };
}


export function get_token(data) {
    return function(dispatch) {
        let login_request = request.post(server + login_endpoint);
        login_request.send(data);
        login_request.end((error, response) => {
            if (error == null) {
                dispatch(login_liaison(response.body.token));
            } else {
                console.log("Failed to get token: ", error);
                return dispatch({
                    type: "TOKEN",
                    payload: "ERROR"
                });
            }
        });
    }
}

/* ----- */