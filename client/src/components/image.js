import React from "react";
import { Transition, animated } from "react-spring/renderprops";

import { shuffleArray } from "../helpers";
import { getImages } from "../requests";


export default class Image extends React.Component {

  state = {
    images: [],
    index: 0
  };

  timeout = undefined;

  loopImages = () => {
    this.timeout = setTimeout(() => {
      this.nextImage();
      this.loopImages();
    }, 3000);
  };

  previousImage = () => {

    clearTimeout(this.timeout);
    const previousIndex =
      this.state.index > 0
        ? this.state.index - 1
        : this.state.images.length - 1;

    this.setState({ index: previousIndex });
    setTimeout(function(){}, 2000);
    this.loopImages();

  };

  nextImage = () => {

    clearTimeout(this.timeout);
    const nextIndex =
      this.state.index < this.state.images.length - 1
        ? this.state.index + 1
        : 0;

    this.setState({ index: nextIndex });
    setTimeout(function(){}, 2000);
    this.loopImages();

  };

  keyDown = event => {
    // eslint-disable-next-line
    switch (event.keyCode) {
      case 37:
        this.previousImage();
        break;
      case 39:
        this.nextImage();
        break;
    }
  };

  async componentDidMount() {

    document.addEventListener("keydown", this.keyDown.bind(this));

  }

  async componentDidUpdate(previousProps, previousState) {

    if (previousProps.tags !== this.props.tags) {

      const imageResponses = await getImages(this.props.tags);

      if (Object.keys(imageResponses).length) {
        clearTimeout(this.timeout);
        this.buildImages(imageResponses);
        this.setState({ index: 0 });
        setTimeout(function(){}, 2000);
        this.loopImages();
      }

    }

  }

  buildImages(images) {

    const shuffledKeys = shuffleArray(Object.keys(images));

    const imageEls = shuffledKeys.map(imageKey => style => (
      <animated.img style={style} src={images[imageKey]['location']} alt={imageKey} />
    ));

    this.setState({ images: imageEls });

  }

  render() {

    return (

      <div className="imageComponent">

        <div className="imageComponent__image">
          <Transition
            native
            reset
            unique
            items={ this.state.index }
            config={{ duration: 1000 }}
            from={{ opacity: 0 }}
            enter={{ opacity: 1 }}
            leave={{ opacity: 0 }}
          >
            {index => this.state.images && this.state.images[index]}
          </Transition>
        </div>

        <button type="button" className="btn btn-default left" aria-label="Left Align" onClick={() => this.previousImage()}>
            <span className="oi oi-chevron-left" title="chevron-left" aria-hidden="true"></span>
        </button>
        <button type="button" className="btn btn-default right" aria-label="Left Align" onClick={() => this.nextImage()}>
            <span className="oi oi-chevron-right" title="chevron-right" aria-hidden="true"></span>
        </button>

      </div>

    );
  }

}
