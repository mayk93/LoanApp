import React from 'react';
import {Component} from 'react';


export default class App extends Component {
    constructor(props) {

        super(props);
    }

    render() {
        return (
            <div className="container navbar navbar-fixed-bottom">
                <footer>
                    Hosted on
                    <span className="span-padding-left">
                    <a href="https://github.com/mayk93/" className="prevent-color-change">
                        <i className="fa fa-github" aria-hidden="true">

                        </i>
                    </a>
                    </span>
                </footer>
            </div>
        );
    }
}
