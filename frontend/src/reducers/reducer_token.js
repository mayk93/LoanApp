/**
 * Created by michael on 23/03/2017.
 */


export default function (state = "", action) {
    switch (action.type) {
        case "TOKEN":
            return action.payload;
        default:
            return state;
    }
}
