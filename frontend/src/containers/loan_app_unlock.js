/* React */
import React, {Component} from 'react';

/* Redux */
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

/* Actions */
import { get_token } from '../actions/index';

class LoanAppUnlock extends Component {
    constructor(props) {
        super(props);

        this.state = {
            username: "",
            password: "",
            button_color: "btn btn-primary wide"
        };
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.token == "") {
            // No change case
            this.setState({
                button_color: "btn btn-primary wide"
            });
        } else if (nextProps.token == "ERROR") {
            // Red / Failed case
            this.setState({
                button_color: "btn btn-danger wide"
            });
        } else {
            // Green / Success case
            this.setState({
                button_color: "btn btn-success wide"
            });
        }
    }

    render() {
        return (
            <div>
                <div className="input-group input-group-sm">
                    <span className="input-group-addon" id="sizing-addon3">
                        <i className="fa fa-user" aria-hidden="true">

                        </i>
                    </span>
                    <input type="text" className="form-control" placeholder="Username" aria-describedby="sizing-addon3"
                           onChange={(event) => {this.setState({username: event.target.value})}}
                    />
                </div>

                <br/>

                <div className="input-group input-group-sm">
                    <span className="input-group-addon" id="sizing-addon3">
                        <i className="fa fa-key" aria-hidden="true">

                        </i>
                    </span>
                    <input type="password" className="form-control"
                           placeholder="Username" aria-describedby="sizing-addon3"
                           onChange={(event) => {this.setState({password: event.target.value})}}
                    />
                </div>

                <br/>

                <button type="button" className={this.state.button_color}
                        onClick={() => {this.props.get_token(this.state)}}>
                    Unlock the API
                </button>
                <br/>
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
    return bindActionCreators({ get_token }, dispatch);
}


export default connect(mapStateToProps, mapDispatchToProps)(LoanAppUnlock);