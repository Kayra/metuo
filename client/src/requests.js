import * as axios from 'axios';

import { getConfig } from './helpers';

export async function getTags() {

    var server = getConfig().server;

    var tags = (await axios.get(server + '/tags')).data;

    return tags;

}

export async function getImages() {

    var server = getConfig().server;

    var imagesResponse = (await axios.get(server + '/images?tags=hey')).data;

    const images = Object.keys(imagesResponse).map(imageName => server + imagesResponse[imageName].location);

    return images;

}