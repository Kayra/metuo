import React from 'react';
import ReactDOM from 'react-dom';

import './styles.css';
import Filters from './components/filters';
import Image from './components/image';

import { determineToggledCategoryTags } from './helpers';
import { getCategorisedTags, getLocationInfo } from "./requests";

export class Page extends React.Component {

    state = {
        tags: []
    };

    categorisedTags = {};
    toggledCategoryTags = {};

    updateTags = (tags) => {
        this.setState({tags: tags});
    }

    async componentDidMount() {

        this.categorisedTags = await getCategorisedTags();
        const location = await getLocationInfo();
    
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
    
        this.toggledCategoryTags = determineToggledCategoryTags(location, urlParams, this.categorisedTags);
    
        const tags = this.toggledCategoryTags ? Object.keys(this.toggledCategoryTags).map(key => this.toggledCategoryTags[key]) : [];

        this.setState({tags: tags});
            
    }

    render() { 

        return (
            <div className='page'>
                <Image tags={this.state.tags}/> 
                <Filters updateTags={this.updateTags} categorisedTags={this.categorisedTags} toggledCategoryTags={this.toggledCategoryTags} /> 
            </div>
        );
    }

}

ReactDOM.render(
    <Page />,
    document.getElementById('root')
);