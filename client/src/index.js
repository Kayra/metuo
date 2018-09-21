import React from 'react';
import ReactDOM from 'react-dom';

import { Image, Filters } from './components';
import { getTags, getImages } from './requests';
import './styles.css';

export class Page extends React.Component {

    filterCategories = [
        'Year',
        'Season',
        'Colour',
        'Location'
    ];

    state = {
        tags: []
    };

    async componentDidMount() {

        const tags = await getTags();
        this.setState({ tags: tags });

    }

    render() { 

        const tags = this.state.tags;

        return (
        <div className='page'>
            <div className='image'>
                <Image />
            </div>
            <div className='filters'>
                <Filters filterCategories={tags} /> 
            </div>
        </div>
    );}
}

ReactDOM.render(
    <Page />,
    document.getElementById('root')
);