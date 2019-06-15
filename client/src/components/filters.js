import React from 'react';

import { getConfig, updateUrlParamsWithToggledCategoryTags } from '../helpers';


export default class Filters extends React.Component {
    
    state = {
            categories: [],
            toggledCategories: [],
            toggledCategoryTags: {}
    };

    loadedInitialCategoryTags = false;

    componentDidUpdate() {
        if (!this.loadedInitialCategoryTags && this.props.toggledCategoryTags) {
            this.setState({ 
                toggledCategoryTags: this.props.toggledCategoryTags
            });
            this.loadedInitialCategoryTags = true;
        }
    }

    filterIsSelected = (filter) => {
        return Object.values(this.state.toggledCategoryTags).includes(filter);
    }

    categoryIsFiltered = (category) => {
        return Object.keys(this.state.toggledCategoryTags).includes(category);
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
        
        var updatedToggledCategoryTags;

        if (Object.keys(this.state.toggledCategoryTags).length && !Object.values(this.state.toggledCategoryTags).includes(tag)) {
            
            updatedToggledCategoryTags = {...this.state.toggledCategoryTags};
            updatedToggledCategoryTags[filterCategory] = tag;
            this.setState({toggledCategoryTags: updatedToggledCategoryTags});
            this.toggleFilterCategory(filterCategory);

            this.props.updateTags(Object.values(updatedToggledCategoryTags));

        } else if (!Object.keys(this.state.toggledCategoryTags).includes(filterCategory)) {

            updatedToggledCategoryTags = {...this.state.toggledCategoryTags};
            updatedToggledCategoryTags[filterCategory] = tag;
            this.setState({toggledCategoryTags: updatedToggledCategoryTags});
            this.toggleFilterCategory(filterCategory);

            this.props.updateTags(Object.values(updatedToggledCategoryTags));

        } else if (Object.keys(this.state.toggledCategoryTags).includes(filterCategory)) {

            updatedToggledCategoryTags = {...this.state.toggledCategoryTags};
            delete updatedToggledCategoryTags[filterCategory];
            this.setState({toggledCategoryTags: updatedToggledCategoryTags});
            this.toggleFilterCategory(filterCategory);

            this.props.updateTags(Object.values(updatedToggledCategoryTags));
        
        }

        updateUrlParamsWithToggledCategoryTags(updatedToggledCategoryTags);

    }

    filterCategoryButtonOnClick = (filterCategory) => {
        this.toggleFilterCategory(filterCategory);
    }

    filterListItemButtonOnClick = (filter, filterCategory) => {
        this.toggleTag(filterCategory, filter);
    }

    filterCategoryListConstructor = (filterCategory) => {

        const displayCategoryOrFilter = !this.categoryIsFiltered(filterCategory) ? filterCategory : this.state.toggledCategoryTags[filterCategory];

        return (
            <li key={filterCategory}>
                <button 
                    className = {this.categoryIsFiltered(filterCategory) ? 'selectedFilter' : ''}
                    onClick={() => this.filterCategoryButtonOnClick(filterCategory)}>
                    {displayCategoryOrFilter}
                </button>
            </li>
        )
    }

    filtersListConstructor = (filterCategory, filters) => {

        const filterList = filters.map(filter => 
            <li key={filter}>
                <button 
                    className={this.filterIsSelected(filter) ? 'selectedFilter' : ''}
                    onClick={() => this.filterListItemButtonOnClick(filter, filterCategory)}>
                    {filter}
                </button>
            </li>
        );

        return (
            [filterList]
        )

    }

    filtersConstructor = (filterCategory, filters) => {
        
        const filterList = this.filtersListConstructor(filterCategory, filters);

        const filterCategoryList = this.filterCategoryListConstructor(filterCategory);

        const categoryIsSelected = this.state.toggledCategories.includes(filterCategory);

        return (
            <div>
                <ul
                    className="filterCategory"
                    style={{display: !categoryIsSelected ? 'inline' : 'none'}}>
                    {filterCategoryList}
                </ul>
                <ul
                    className="filterList"
                    style={{display: categoryIsSelected ? 'inline-grid' : 'none'}}>
                    {filterList}
                </ul>
            </div>
        )

    }

    determineFilterCategoriesToContruct = (filterCategories) => {

        const homeCategories = getConfig().homeCategories;
        return filterCategories.filter(filterCategory => homeCategories.includes(filterCategory.toLowerCase()));

    }

    render() { 

        const filterCategoriesToContruct = this.determineFilterCategoriesToContruct(Object.keys(this.props.categorisedTags));

        const filters = filterCategoriesToContruct
                        .map(filterCategory => this.filtersConstructor(filterCategory, this.props.categorisedTags[filterCategory]));

        return (
            <nav className="filtersComponent">
                {filters}
            </nav>
        );

    }
}
