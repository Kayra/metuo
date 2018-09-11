import * as axios from 'axios';

import { getConfig } from './helpers';

export async function getTags() {

    var config = getConfig();
    var server = config.server;

    var tags = (await axios.get(server + '/tags')).data;

    return tags;

}
