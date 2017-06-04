import React from 'react';
import {Component} from 'react';


export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="jumbotron small-jumbotron">
                <div className="page-header">
                    <h1>Loan app</h1>
                    <small>A simple manager that uses Django REST framework</small>
                </div>
                <hr/>
            </div>
        );
    }
}