import request from 'superagent';

let server = "http://localhost:8000/";
let _server = "https://localhost:8000/";
let login_endpoint = "api-auth/login/";


function login_liaison(data) {
    return {
        type: "LOGIN",
        payload: data
    };
}


export function login(data) {
    console.log("Sending ", data, " to login endpoint.");
    return function(dispatch) {
        let login_request = request.post(server + login_endpoint);
        login_request.send(data);
        login_request.end((error, response) => {
            if (error == null) {
                console.log("Success, made a POST to the login endpoint: ", response);
                dispatch(login_liaison(response.body));
            } else {
                console.log("Failed, did not make a POST to the login endpoint: ", error);
                return dispatch({
                    type: "LOGIN",
                    payload: "ERROR"
                });
            }
        });
    }
}

/* ----- */