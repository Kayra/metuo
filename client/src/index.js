import React from 'react';
import ReactDOM from 'react-dom';

import { Image, Filters } from './components';
import './styles.css';

export class Page extends React.Component {

    filterCategories = [
        'Year',
        'Season',
        'Colour',
        'Location'
    ];

    render() { return (
        <div className='page'>
            <div className='image'>
                <Image src='https://via.placeholder.com/150' alt='' />
            </div>
            <div className='filters'>
                <Filters filterCategories={this.filterCategories} /> 
            </div>
        </div>
    );}
}

ReactDOM.render(
    <Page />,
    document.getElementById('root')
);