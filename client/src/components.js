import React from 'react';

import { filterCategoriesToListItems } from './helpers';


export class Image extends React.Component {
    render() { return (
        <img src={this.props.src} alt={this.props.alt}></img>
    );}
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
