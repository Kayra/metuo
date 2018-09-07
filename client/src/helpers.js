
export function getConfig() {

    const environment = process.env.NODE_ENV || 'default';

    const config = require('./config/' + environment + '.json');

    return config;

}