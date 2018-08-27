import React from 'react';

export class Image extends React.Component {
    render() { return (
        <img src={this.props.src} alt={this.props.alt}></img>
    );}
}

export class Filters extends React.Component {

    filterCategories = this.props.filterCategories.map(filterCategory =>
        <li>{filterCategory}</li>
    );

    render() { return (
        <ul>
            {this.filterCategories}
        </ul>
    );}
}
