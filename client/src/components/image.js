import React from "react";
import { Transition, animated } from "react-spring/renderprops";

import { getImages } from "../requests";

export default class Image extends React.Component {
  state = {
    images: [],
    image: "",
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
  };

  nextImage = () => {
    clearTimeout(this.timeout);
    const nextIndex =
      this.state.index < this.state.images.length - 1
        ? this.state.index + 1
        : 0;

    this.setState({ index: nextIndex });
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
    const images = await getImages();
    this.buildImages(images);
    this.loopImages();

    document.addEventListener("keydown", this.keyDown.bind(this));
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

  buildImages(images) {
    const imageEls = images.map(img => style => (
      <animated.img style={style} src={img} key={img} alt={img} />
    ));
    this.setState({ images: imageEls });
  }

  render() {
    return (
      <div className="image">
        <button onClick={() => this.previousImage()}> &lt; </button>
        <button onClick={() => this.nextImage()}> &gt; </button>

        <div style={{ marginTop: 10 }}>
          <Transition
            native
            reset
            unique
            items={this.state.index}
            from={{ opacity: 0 }}
            enter={{ opacity: 1 }}
            leave={{ opacity: 0 }}
          >
            {index => this.state.images && this.state.images[index]}
          </Transition>
        </div>
      </div>
    );
  }
}
