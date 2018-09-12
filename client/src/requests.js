import * as axios from 'axios';

import { getConfig } from './helpers';

export async function getTags() {

    var server = getConfig().server;

    var tags = (await axios.get(server + '/tags')).data;

    return tags;

}
