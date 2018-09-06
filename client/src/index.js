import React from 'react';
import ReactDOM from 'react-dom';

import { Image, Filters } from './components';
import { getTags } from './requests';
import './styles.css';

export class Page extends React.Component {

    filterCategories = [
        'Year',
        'Season',
        'Colour',
        'Location'
    ];

    // tags = (async () => {
    //     await getTags();
    // })();

    tags = getTags().then(tags => tags);

    render() { return (
        <div className='page'>
            <div className='image'>
                <Image src='https://via.placeholder.com/150' alt='' />
                {/* <p>{this.tags}</p> */}
                {console.log(this.tags)}
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