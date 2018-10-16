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

    filterButtonsList = (filterCategories) => {

        const categoriesList = filterCategories.map(filterCategory => this.renderTagsOrTagOrCategory(filterCategory));

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
            return this.selectedTagListItemButton(filterCategory, this.state.toggledCategoryTags[filterCategory]);
        } else {
            return this.categoryListItemButton(filterCategory);
        }
    }

    tagsList = (filterCategory, tags) => {

        const tagListItems = tags.map(tag => this.tagListItemButton(filterCategory, tag));

        return (
            <ul>
                {tagListItems}
            </ul>
        );

    }

    tagListItemButton = (filterCategory, tag) => {

        var style = {};

        if (Object.values(this.state.toggledCategoryTags).includes(tag)) {
            style = {color: 'red'}
        }

        return (
            <li key={tag}>
                <button style={style} onClick={() => this.toggleTag(filterCategory, tag)}>
                    {tag}
                </button>
            </li>
        )
    }

    selectedTagListItemButton = (filterCategory, tag) => {
        return (
            <li key={tag}>
                <button onClick={() => this.toggleFilterCategory(filterCategory)}>
                    {tag}
                </button>
            </li>
        )
    }

    toggleFilterCategory = (filterCategory) => {

        if (this.state.toggledCategories.includes(filterCategory)) {

            const updatedToggledCategories = [...this.state.toggledCategories];
            updatedToggledCategories.splice(updatedToggledCategories.indexOf(filterCategory), 1);
            this.setState({toggledCategories: updatedToggledCategories});

        } else if (!this.state.toggledCategories.includes(filterCategory)) {
        
            const updatedToggledCategories = [...this.state.toggledCategories];
            updatedToggledCategories.push(filterCategory);
            this.setState({toggledCategories: updatedToggledCategories});

        }

    }

    toggleTag = (filterCategory, tag) => {
        
        if (Object.keys(this.state.toggledCategoryTags).length && !Object.values(this.state.toggledCategoryTags).includes(tag)) {
            
            const updatedToggledCategoryTags = {...this.state.toggledCategoryTags};
            updatedToggledCategoryTags[filterCategory] = tag;
            this.setState({toggledCategoryTags: updatedToggledCategoryTags});
            this.toggleFilterCategory(filterCategory);

            this.props.updateTags(Object.values(updatedToggledCategoryTags));

        } else if (!Object.keys(this.state.toggledCategoryTags).includes(filterCategory)) {

            const updatedToggledCategoryTags = {...this.state.toggledCategoryTags};
            updatedToggledCategoryTags[filterCategory] = tag;
            this.setState({toggledCategoryTags: updatedToggledCategoryTags});
            this.toggleFilterCategory(filterCategory);

            this.props.updateTags(Object.values(updatedToggledCategoryTags));

        } else if (Object.keys(this.state.toggledCategoryTags).includes(filterCategory)) {

            var updatedToggledCategoryTags = {...this.state.toggledCategoryTags};
            delete updatedToggledCategoryTags[filterCategory];
            this.setState({toggledCategoryTags: updatedToggledCategoryTags});
            this.toggleFilterCategory(filterCategory);

            this.props.updateTags(Object.values(updatedToggledCategoryTags));

        }

    }

    render() { 

        const filterButtons = this.filterButtonsList(this.state.categories);
        console.log(this.state);
        return (
            <div>
                {filterButtons}
            </div>
        );

    }
}
