
export function getConfig() {

    const environment = process.env.NODE_ENV || 'default';

    const config = require('./config/' + environment + '.json');

    config['env'] = environment;
    config['ipfindApiKey'] = process.env.REACT_APP_IP_FIND_API_KEY || '';

    return config;

}

export function currentLocationInLocationTags(location, categorisedTags) {

    const locationsToCheck = ['country', 'city', 'region', 'county']

    for (const locationToCheck of locationsToCheck) {
        if (categorisedTags['Location'].includes(location[locationToCheck])) {
            return location[locationToCheck]
        }
    }

    return null;

}