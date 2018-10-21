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

            this.setState({image: this.state.images[this.state.index]})
            const index = this.state.index === this.state.images.length - 1 ? 0 : this.state.index + 1;
            this.setState({index: index})

        }, 3000)

    }

    async componentDidMount() {

        const images = await getImages();
        this.setState({ images: images });
        this.setState({ image: images[0] });
        this.loopImages();

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
            <img src={this.state.image} alt=''></img>
        );

    }

}

