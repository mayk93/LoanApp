import request from 'superagent';

let server = "http://localhost:8000/";
let login_endpoint = "api-token-auth/";
let loan_list_endpoint = "loans/";


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


export function api_get_loan_list(token) {
    return function(dispatch) {
        let loan_list_request = request.get(server + loan_list_endpoint);
        // loan_list_request.set("WWW-Authenticate", "Token");
        loan_list_request.set("Authorization", token);
        loan_list_request.end((error, response) => {
            if (error == null) {
                console.log("Success getting list: ", response.body.results);
                return dispatch({
                    type: "LOAN_LIST",
                    payload: response.body.results
                });
            } else {
                console.log("Failed to get loan list: ", error);
                return dispatch({
                    type: "LOAN_LIST",
                    payload: []
                });
            }
        });
    }
}

export function new_loan(data) {

}