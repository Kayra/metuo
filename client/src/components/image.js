import React from 'react';

import { getImages } from '../requests';


export default class Image extends React.Component {

    state = {
        images: [],
        image: ''
    };

    loopImages = (images) => {

        var index = 0;

        setInterval(() => {
            
            this.setState({image: this.state.images[index]})

            if (index === images.length - 1) {
                index = 0;
            } else {
                index++;
            }

        }, 3000)

    }

    async componentDidMount() {

        const images = await getImages();
        this.setState({ images: images });
        this.loopImages(images);

    }

    async componentDidUpdate(previousProps, previousState) {

        if (previousProps.tags !== this.props.tags && this.props.tags.length) { 
            const images = await getImages(this.props.tags); 
            if (images.length) {
                this.setState({ images: images });
                this.loopImages(images);
            }
        }

        console.log(this.state);

    }

    render() { 

        return (
            <img src={this.state.image} alt=''></img>
        );

    }

}

