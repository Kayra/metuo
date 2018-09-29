import React from 'react';

import { getCategorisedTags, getImages } from './requests';


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
    
    state = {
            categories: [],
            categorisedTags: {}
    };

    async componentDidMount() {

        const categorisedTags = await getCategorisedTags();
        const categories = Object.keys(categorisedTags);

        this.setState({ 
            categories: categories,
            categorisedTags: categorisedTags
        });

    }

    filterCategoriesToListItems = (filterCategories) => {
        return filterCategories.map(filterCategory =>
            <li key={filterCategory}>
                <button onClick={this.handleClick}>
                    {filterCategory}
                </button>
            </li>
        );
    }

    handleClick = () => {
        console.log('this is: ', this);
    }

    render() { 

        const componentFilterCategories = this.filterCategoriesToListItems(this.state.categories);

        return (
            <ul>
                {componentFilterCategories}
            </ul>
        );

    }
}
