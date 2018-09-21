import React from 'react';

import { getTags, getImages } from './requests';
import { filterCategoriesToListItems } from './helpers';


export class Image extends React.Component {

    state = {
        images: []
    };

    async componentDidMount() {

        const images = await getImages();
        this.setState({ images: images });

    }

    render() { 

        const image = this.state.images[0];

        return (
            <img src={image} alt=''></img>
        );
    }

}

export class Filters extends React.Component {

    render() { 

        const componentFilterCategories = filterCategoriesToListItems(this.props.filterCategories);

        return (
            <ul>
                {componentFilterCategories}
            </ul>
        );
    }
}
