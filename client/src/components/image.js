import React from 'react';

import { getImages } from '../requests';


export default class Image extends React.Component {

    state = {
        images: [],
        image: '',
        index: 0
    };

    loopImages = () => {

        setInterval(() => {

            const index = this.state.index === this.state.images.length - 1 ? 0 : this.state.index + 1;
            this.setState({index: index})

        }, 3000)

    }

    previousImage = () => {

        const previousIndex = this.state.index > 0 ? this.state.index - 1 : this.state.images.length - 1;
        this.setState({index: previousIndex});
    }

    nextImage = () => {

        const nextIndex = this.state.index < this.state.images.length - 1 ? this.state.index + 1 : 0;
        this.setState({index: nextIndex});

    }

    keyDown = (event) => {
        // eslint-disable-next-line
        switch (event.keyCode) {
            case 37:
                this.previousImage();
                break;
            case 39:
                this.nextImage();
                break;
        }
    }

    async componentDidMount() {

        const images = await getImages();
        this.setState({ images: images });
        this.loopImages();

        document.addEventListener('keydown', this.keyDown.bind(this));

    }

    async componentDidUpdate(previousProps, previousState) {

        if (previousProps.tags !== this.props.tags && this.props.tags.length) { 
            const images = await getImages(this.props.tags); 
            if (images.length) {
                this.setState({ images: images });
                this.setState({ index: 0 });
            }
        }

    }

    render() { 

        return (
            <div>
                <button onClick={() => this.previousImage()}> &lt; </button>
                <img src={this.state.images[this.state.index]} alt=''></img>
                <button onClick={() => this.nextImage()}> &gt; </button>
            </div>
        );

    }

}

