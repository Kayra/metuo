import * as axios from 'axios';

import { getConfig } from './helpers';

export async function getCategorisedTags() {

    var server = getConfig().server;
    const requestUrl = server + '/tags';

    const categorisedTags = (await axios.get(requestUrl)).data;

    return categorisedTags;

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