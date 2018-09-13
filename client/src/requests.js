import * as axios from 'axios';

import { getConfig } from './helpers';

export async function getTags() {

    var server = getConfig().server;

    var tags = (await axios.get(server + '/tags')).data;

    return tags;

}

export async function getImages() {

    var server = getConfig().server;

    var images = (await axios.get(server + '/images')).data;

    return images;

}