import * as axios from 'axios';

import { getConfig } from './helpers';

export async function getTags() {

    var server = getConfig().server;
    const requestUrl = server + '/tags';

    const tags = (await axios.get(requestUrl)).data;

    return tags;

}

export async function getImages() {

    const server = getConfig().server;
    const requestUrl = server + '/images';

    const imagesResponse = (await axios.get(requestUrl, { 
        params: { tags: 'hey' }
    })).data;

    const images = Object.keys(imagesResponse).map(imageName => server + imagesResponse[imageName].location);

    return images;

}