import * as axios from 'axios';

import { getConfig } from './helpers';

export async function getCategorisedTags() {

    const config = getConfig();
    const requestUrl = config.server + '/tags';

    const categorisedTags = (await axios.get(requestUrl)).data;

    return categorisedTags;

}

export async function getImages(tags) {

    const config = getConfig();
    console.log(config);

    const requestUrl = config.server + '/images';
    var imagesResponse = {}

    if (tags) {
        imagesResponse = (await axios.get(requestUrl, { 
            params: { tags: tags.join() }
        })).data;
    } else {
        imagesResponse = (await axios.get(requestUrl)).data;
    }

    var images;
    if (config.env === "production") {
        images = Object.keys(imagesResponse).map(imageName => imagesResponse[imageName].location);
    } else if (config.env === "development") {
        images = Object.keys(imagesResponse).map(imageName => config.server + imagesResponse[imageName].location);
    }

    return images;

}