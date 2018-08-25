import React from 'react';
import ReactDOM from 'react-dom';
import './styles.css';

class Image extends React.Component {
    render() { return (
        <img src={this.props.src} alt={this.props.alt}></img>
    );}
}

class Filters extends React.Component {

    filterCategories = this.props.filterCategories.map(filterCategory =>
        <li>{filterCategory}</li>
    );

    render() { return (
        <ul>
            {this.filterCategories}
        </ul>
    );}
}

class Page extends React.Component {

    filterCategories = [
        'Year',
        'Season',
        'Colour',
        'Location'
    ];

    render() { return (
        <div className='page'>
            <div className='image'>
                <Image src='https://via.placeholder.com/150' alt='' />
            </div>
            <div className='filters'>
                <Filters filterCategories={this.filterCategories} /> 
            </div>
        </div>
    );}
}

ReactDOM.render(
    <Page />,
    document.getElementById('root')
);