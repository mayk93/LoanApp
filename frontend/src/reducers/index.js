import {combineReducers} from 'redux';

import ReducerLogin from './reducer_login';

const rootReducer = combineReducers({
    login_result: ReducerLogin
});

export default rootReducer;

