import * as axios from 'axios';

import { getConfig } from './helpers';

export async function getTags() {

    var server = getConfig().server;
    const requestUrl = server + '/tags';

    const tags = (await axios.get(requestUrl)).data;

    return tags;

}

export async function getImages(tags) {

    const server = getConfig().server;
    const requestUrl = server + '/images';
    var imagesResponse = {}

    if (tags) {
        imagesResponse = (await axios.get(requestUrl, { 
            params: { tags: tags.join() }
        })).data;
    } else {
        imagesResponse = (await axios.get(requestUrl)).data;
    }

    const images = Object.keys(imagesResponse).map(imageName => server + imagesResponse[imageName].location);

    return images;

}