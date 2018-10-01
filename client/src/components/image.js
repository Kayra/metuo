import React from 'react';

import { getImages } from '../requests';


export default class Image extends React.Component {

    state = {
        images: []
    };

    async componentDidMount() {
        const images = await getImages();
        this.setState({ images: images });
    }

    render() { 

        const image = this.state.images[0];

        return (
            <img src={image} alt=''></img>
        );

    }

}

