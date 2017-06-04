/* React */
import React, {Component} from 'react';

/* Redux */
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

/* Actions */
import { login } from '../actions/index';

class LoanApp extends Component {
    constructor(props) {
        super(props);

        this.state = {
            username: "",
            password: ""
        };
    }

    render() {
        return (
            <div>
                <input type="text" onChange={(event) => {this.setState({username: event.target.value})}} />
                <br/>
                <input type="password" onChange={(event) => {this.setState({password: event.target.value})}} />
                <br/>
                <button onClick={() => {this.props.login(this.state)}}>Login</button>
                <br/>
                <p>You sent: {this.props.login_result}</p>
            </div>
        )

    }
}

function mapStateToProps(state) {
    return {
      login_result: state.login_result
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators({ login }, dispatch);
}


export default connect(mapStateToProps, mapDispatchToProps)(LoanApp);