import React from 'react';

export class Image extends React.Component {
    render() { return (
        <img src={this.props.src} alt={this.props.alt}></img>
    );}
}

export class Filters extends React.Component {

    render() { 

        const componentFilterCategories = this.props.filterCategories.map(filterCategory =>
            <li key={filterCategory}>{filterCategory}</li>
        );

        return (
            <ul>
                {componentFilterCategories}
            </ul>
        );
    }
}
