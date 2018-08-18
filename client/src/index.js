import React from 'react';
import ReactDOM from 'react-dom';
import './styles.css';

class Image extends React.Component {
    render() { return (
        <img src="{this.props.src}"></img>
    );}
}

class Filters extends React.Component {
    render() { return (
        <ul>
            <li>Year</li>
            <li>Season</li>
            <li>Colour</li>
            <li>Location</li>
        </ul>
    );}
}

class Page extends React.Component {
    render() { return (
        <div className='page'>
            <div className='image'>
                <Image />
            </div>
            <div className='filters'>
                <Filters />
            </div>
        </div>
    );}
}

ReactDOM.render(
    <Page />,
    document.getElementById('root')
  );