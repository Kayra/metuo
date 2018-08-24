import React from 'react';
import ReactDOM from 'react-dom';
import './styles.css';

class Image extends React.Component {
    render() { return (
        <img src={this.props.src} alt={this.props.alt}></img>
    );}
}

class Filters extends React.Component {

    filters = this.props.filterNames.map(filterName =>
        <li>{filterName}</li>
    );

    render() { return (
        <ul>
            {this.filters}
        </ul>
    );}
}

class Page extends React.Component {

    filterNames = [
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
                <Filters filterNames={this.filterNames} /> 
            </div>
        </div>
    );}
}

ReactDOM.render(
    <Page />,
    document.getElementById('root')
);