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
    const requestUrl = config.server + '/images';
    var imagesResponse = {}

    if (tags) {
        imagesResponse = (await axios.get(requestUrl, { 
            params: { tags: tags.join() }
        })).data;
    } else {
        imagesResponse = (await axios.get(requestUrl)).data;
    }

    return imagesResponse;

}

export async function getLocationInfo() {

    const config = getConfig();
    const apiKey = config.ipfindApiKey;
    
    const locationResponse = (await axios.get('https://api.ipfind.com/me?auth=' + apiKey).catch(() => null));

    return locationResponse;

}
