import * as axios from 'axios';

import { getConfig } from './helpers';

export async function getTags() {

    var config = getConfig();
    var server = config.server;

    var response = await axios.get(server + '/tags');

    return response.data;

}
