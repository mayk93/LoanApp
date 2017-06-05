/**
 * Created by michael on 05/06/2017.
 */

/* React */
import React, {Component} from 'react';

/* Redux */
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

/* Actions */
import { api_get_loan_list } from '../actions/index';

class LoanAppListLoans extends Component {
    constructor(props) {
        super(props);
    }

    componentWillMount() {
        this.props.api_get_loan_list(this.props.token);
    }

    get_loan_list() {
        return this.props.loan_list.map((loan) => {
            console.log("Trying to map: ", loan);
            return (
                <li className="list-group-item" key={loan.id}>
                    <div className="panel-heading">{loan.company}</div>
                    <div className="panel-body">
                        <p>{"Your requested a loan for " + loan.amount.toString() + " GBP."}</p>
                    </div>
                    <div className={
                        loan.approved ? "alert alert-success": "alert alert-danger"
                    } role="alert">
                        {loan.approved ?
                        "Your loan has been approved!"
                        :
                        "Your loan has been rejected!"}</div>

                </li>
            )
        });
    }

    render() {
        let loan_list = this.get_loan_list();
        return (
            <div>
                <ul className="list-group">
                    {loan_list}
                </ul>
            </div>
        )

    }
}

function mapStateToProps(state) {
    return {
        token: state.token,
        loan_list: state.loan_list
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators({ api_get_loan_list }, dispatch);
}


export default connect(mapStateToProps, mapDispatchToProps)(LoanAppListLoans);
