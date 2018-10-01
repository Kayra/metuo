import React from 'react';
import ReactDOM from 'react-dom';

import './styles.css';
import Filters from './components/filters';
import Image from './components/image';

export class Page extends React.Component {

    render() { 
        return (
            <div className='page'>
                <div className='image'>
                    <Image />
                </div>
                <div className='filters'>
                    <Filters /> 
                </div>
            </div>
        );
    }

}

ReactDOM.render(
    <Page />,
    document.getElementById('root')
);