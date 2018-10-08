import React from 'react';

import { getCategorisedTags } from '../requests';


export default class Filters extends React.Component {
    
    state = {
            categories: [],
            categorisedTags: {},
            toggledCategories: [],
            toggledCategoryTags: {}
    };

    async componentDidMount() {

        const categorisedTags = await getCategorisedTags();
        const categories = Object.keys(categorisedTags);

        this.setState({ 
            categories: categories,
            categorisedTags: categorisedTags
        });

    }

    filterCategoriesList = (filterCategories) => {

        const categoriesList = filterCategories.map(filterCategory => this.categoryListItemButton(filterCategory));

        return (
            <ul>
                {categoriesList}
            </ul>
        )
    }

    categoryListItemButton = (filterCategory) => {
        return (
            <li key={filterCategory}>
                <button onClick={() => this.toggleFilterCategory(filterCategory)}>
                    {filterCategory}
                </button>
            </li>
        );
    }

    renderTagsOrTagOrCategory = (filterCategory) => {
        if (this.state.toggledCategories.includes(filterCategory)) {
            return this.tagsList(filterCategory, this.state.categorisedTags[filterCategory]);
        } else if (Object.keys(this.state.toggledCategoryTags).includes(filterCategory)) { 
            return this.state.toggledCategoryTags[filterCategory];
        } else {
            return filterCategory;
        }
    }

    tagsList = (filterCategory, tags) => {

        const tagListItems = tags.map(tag => 
            <li key={tag}>
                <button onClick={() => this.toggleTag(filterCategory, tag)}>
                    {tag}
                </button>
            </li>
        );

        return (
            <ul>
                {tagListItems}
            </ul>
        );

    }

    toggleFilterCategory = (filterCategory) => {

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

    toggleTag = (filterCategory, tag) => {
        
        if (Object.keys(this.state.toggledCategoryTags).includes(filterCategory)) {

            var updatedToggledCategoryTags = {...this.state.toggledCategoryTags};
            delete updatedToggledCategoryTags[filterCategory];
            this.setState({toggledCategoryTags: updatedToggledCategoryTags});

        } else if (!Object.keys(this.state.toggledCategoryTags).includes(filterCategory)) {

            const updatedToggledCategoryTags = {...this.state.toggledCategoryTags};
            updatedToggledCategoryTags[filterCategory] = tag;
            this.setState({toggledCategoryTags: updatedToggledCategoryTags});

        }

    }

    render() { 

        const componentFilterCategories = this.filterCategoriesList(this.state.categories);
        console.log(this.state);
        return (
            <div>
                {componentFilterCategories}
            </div>
        );

    }
}
