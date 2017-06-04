import {combineReducers} from 'redux';

import ReducerToken from './reducer_token';

const rootReducer = combineReducers({
    token: ReducerToken
});

export default rootReducer;

