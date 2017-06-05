/**
 * Created by michael on 05/06/2017.
 */

export default function (state = [], action) {
    switch (action.type) {
        case "LOAN_LIST":
            return action.payload;
        default:
            return state;
    }
}
