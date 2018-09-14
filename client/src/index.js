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
        tags: [],
        images: []
    };

    async componentDidMount() {

        const tags = await getTags();
        this.setState({ tags: tags });

        const images = await getImages();
        this.setState({ images: images });

    }

    render() { 

        const tags = this.state.tags;
        const image = this.state.images[0];

        return (
        <div className='page'>
            <div className='image'>
                <Image src={image} alt='' />
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