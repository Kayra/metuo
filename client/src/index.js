import React from 'react';
import ReactDOM from 'react-dom';

import './styles.css';
import Filters from './components/filters';
import Image from './components/image';

export class Page extends React.Component {

    state = {
        tags: []
    };

    updateTags = (tag) => {

        if (!this.state.tags.includes(tag)) {

            const updatedTags = [...this.state.tags];
            updatedTags.push(tag);
            this.setState({tags: updatedTags});

        } else if (this.state.tags.includes(tag)) {

            const updatedTags = [...this.state.tags];
            updatedTags.splice(updatedTags.indexOf(tag), 1);
            this.setState({tags: updatedTags});

        }

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