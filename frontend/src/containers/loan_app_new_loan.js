/**
 * Created by michael on 05/06/2017.
 */

/* React */
import React, {Component} from 'react';

/* Redux */
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

/* Actions */
import { new_loan } from '../actions/index';

class LoanAppNewLoan extends Component {
    constructor(props) {
        super(props);

        this.state = {
            company: "",
            sector: "",
            synopsis: "",
            amount: 0
        };
    }

    render() {
        return (
            <div>
            <div>
                <div className="input-group input-group-sm">
                    <span className="input-group-addon" id="sizing-addon3">
                        <i className="fa fa-building" aria-hidden="true">

                        </i>
                    </span>
                    <input type="text" className="form-control" placeholder="Company" aria-describedby="sizing-addon3"
                           onChange={(event) => {this.setState({company: event.target.value})}}
                    />
                </div>

                <br/>

                <div className="input-group input-group-sm">
                    <span className="input-group-addon" id="sizing-addon3">
                        <i className="fa fa-industry" aria-hidden="true">

                        </i>
                    </span>

                    <div className="dropdown wide" style={{marginLeft: "5px"}}>
                        <button className="btn dropdown-toggle wide"
                                style={{backgroundColor: "#eceeef", color: "black"}}
                                type="button"
                                data-toggle="dropdown">
                            {this.state.sector.length == 0 ? "Sector" : this.state.sector}
                            <span className="caret">

                            </span>
                        </button>
                        <ul className="dropdown-menu">
                            <li onClick={() => {this.setState({sector: "IT"})}}><a href="#">IT</a></li>
                            <li onClick={() => {this.setState({sector: "Auto"})}}><a href="#">Auto</a></li>
                            <li onClick={() => {this.setState({sector: "Banking"})}}><a href="#">Banking</a></li>
                            <li onClick={() => {this.setState({sector: "Bio Tech"})}}><a href="#">Bio Tech</a></li>
                        </ul>
                    </div>
                </div>

                <br/>

                <div className="input-group">
                    <span className="input-group-addon">£</span>
                    <input type="number" className="form-control" aria-label="Amount (to the nearest dollar)"
                           onChange={(event) => {this.setState({amount: event.target.value})}}/>
                    <span className="input-group-addon">.00</span>
                </div>


                <br/>

                <div className="input-group input-group-sm">
                    <span className="input-group-addon" id="sizing-addon3">
                        <i className="fa fa-pencil" aria-hidden="true">

                        </i>
                    </span>
                    <input type="text" className="form-control" placeholder="Why do you need this loan?"
                           aria-describedby="sizing-addon3"
                           onChange={(event) => {this.setState({synopsis: event.target.value})}}
                    />
                </div>

                <br/>

                <button type="button" className="btn btn-success wide"
                        onClick={() => {this.props.new_loan(this.state, this.props.token)}}>
                    Apply for a loan!
                </button>
                <br/>
            </div>
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
    return bindActionCreators({ new_loan }, dispatch);
}


export default connect(mapStateToProps, mapDispatchToProps)(LoanAppNewLoan);

