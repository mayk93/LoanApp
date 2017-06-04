import React from 'react';
import {Component} from 'react';

import LoanApp from '../containers/loan_app';
import LoanAppJumbotron from './loan_app_jumbotron';
import LoanAppFooter from '../components/loan_app_footer';


export default class App extends Component {
    constructor(props) {

        super(props);
    }

    render() {
        return (
            <div>
                <br/>
                <LoanAppJumbotron/>
                <LoanApp />
                <hr/>
                <LoanAppFooter/>
            </div>
        );
    }
}
