import {combineReducers} from 'redux';

import ReducerToken from './reducer_token';
import ReducerLoanList from './reducer_loan_list';

const rootReducer = combineReducers({
    token: ReducerToken,
    loan_list: ReducerLoanList
});

export default rootReducer;

