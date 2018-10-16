import React from 'react';
import ReactDOM from 'react-dom';

import './styles.css';
import Filters from './components/filters';
import Image from './components/image';

export class Page extends React.Component {

    state = {
        tags: []
    };

    updateTags = (tags) => {
        this.setState({tags: tags});
    }

    render() { 
        console.log(this.state);
        return (
            <div className='page'>
                <div className='image'>
                    <Image />
                </div>
                <div className='filters'>
                    <Filters updateTags={this.updateTags} /> 
                </div>
            </div>
        );
    }

}

ReactDOM.render(
    <Page />,
    document.getElementById('root')
);