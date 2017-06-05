/**
 * Created by michael on 05/06/2017.
 */

/* React */
import React, {Component} from 'react';

/* Redux */
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

/* Actions */
import {} from '../actions/index';

class LoanAppNewLoan extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                Here you will be able to make a new loan soon
            </div>
        )

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


export default connect(mapStateToProps, mapDispatchToProps)(LoanAppNewLoan);

