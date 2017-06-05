/**
 * Created by michael on 05/06/2017.
 */

/* React */
import React, {Component} from 'react';

/* Redux */
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

/* Actions */
import {  } from '../actions/index';

/* Containers */
import LoanAppListLoans from './loan_app_list_loans';
import LoanAppNewLoan from './loan_app_new_loan';

class LoanApp extends Component {
    constructor(props) {
        super(props);

        this.state = {
            current_api_view: 0

        };

        this.api_views = {
            0: "",
            1: <LoanAppListLoans/>,
            2: <LoanAppNewLoan/>
        };

        this.api_unlocked.bind(this);
    }

    api_unlocked() {
        return this.props.token != "ERROR" && this.props.token.length > 0;
    }

    render() {
        if (this.api_unlocked()) {
            return (
                <div>
                    <div className="_flex spaced">
                        <button type="button spaced btn-default gray"
                                style={{margin: "10px", backgroundColor: "#eceeef"}}
                                className="btn btn-default"
                                onClick={() => {this.setState({
                                    current_api_view: 1
                                })}}>View loans</button>
                        <button type="button spaced btn-default gray"
                                style={{margin: "10px", backgroundColor: "#eceeef"}}
                                className="btn btn-default"
                                onClick={() => {this.setState({
                                    current_api_view: 2
                                })}}>New loan</button>
                    </div>
                    <hr/>
                    {this.api_views[this.state.current_api_view]}
                </div>
            )
        } else {
            return (
                <div>
                </div>
            )
        }

    }
}

function mapStateToProps(state) {
    return {
        token: state.token
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators({}, dispatch);
}


export default connect(mapStateToProps, mapDispatchToProps)(LoanApp);