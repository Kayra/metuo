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

    filterCategoryButtonOnClick = (filterCategory) => {
        this.toggleFilterCategory(filterCategory);
    }

    filterListItemButtonOnClick = (filter, filterCategory) => {
        this.toggleTag(filterCategory, filter);
    }

    filterCategoryListConstructor = (filterCategory) => {

        const displayCategoryOrFilter = !Object.keys(this.state.toggledCategoryTags).includes(filterCategory) ? filterCategory : this.state.toggledCategoryTags[filterCategory];

        return (
            <li>
                <button onClick={() => this.filterCategoryButtonOnClick(filterCategory)}>
                    {displayCategoryOrFilter}
                </button>
            </li>
        )
    }

    filtersListConstructor = (filterCategory, filters) => {
     
        const filterList = filters.map(filter => 
            <li>
                <button onClick={() => this.filterListItemButtonOnClick(filter, filterCategory)}>
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

    render() { 

        const filters = Object.keys(this.state.categorisedTags)
                        .map(filterCategory => this.filtersConstructor(filterCategory, this.state.categorisedTags[filterCategory]));

        return (
            <nav className="filtersComponent">
                {filters}
            </nav>
        );

    }
}
