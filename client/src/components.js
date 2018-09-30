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
            categorisedTags: {},
            toggledCategories: []
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
                <button onClick={() => this.toggleCategory(filterCategory)}>

                    {this.renderCategoryOrTags(filterCategory)}

                </button>
            </li>

        );
    }

    renderCategoryOrTags = (filterCategory) => {
        if (this.state.toggledCategories.includes(filterCategory)) {
            return this.state.categorisedTags[filterCategory];
        } else {
            return filterCategory;
        }
    }

    toggleCategory = (filterCategory) => {

        if (this.state.toggledCategories.includes(filterCategory)) {

            const updatedToggledCategories = [...this.state.toggledCategories];
            updatedToggledCategories.splice(filterCategory);
            this.setState({toggledCategories: updatedToggledCategories});

        } else if (!this.state.toggledCategories.includes(filterCategory)) {

            const updatedToggledCategories = [...this.state.toggledCategories];
            updatedToggledCategories.push(filterCategory);
            this.setState({toggledCategories: updatedToggledCategories});

        }

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
