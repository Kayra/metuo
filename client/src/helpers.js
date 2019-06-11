const _ = require("lodash")

export function getConfig() {

    const environment = process.env.NODE_ENV || 'default';

    const config = require('./config/' + environment + '.json');

    config['env'] = environment;
    config['ipfindApiKey'] = process.env.REACT_APP_IP_FIND_API_KEY || '';

    return config;

}

export function updateUrlParamsWithToggledCategoryTags(toggledCategoryTags) {
 
    var urlParams = categorisedTagsToUrlParams(toggledCategoryTags);
    urlParams ? window.history.replaceState({}, "metuo", '?' + urlParams) : window.history.replaceState({}, "metuo", '/');
}


function categorisedTagsToUrlParams(categoryTags) {

    return Object.entries(categoryTags).map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`).join('&');

}

export function determineToggledCategoryTags(location, urlParams, categorisedTags) {

    var toggledCategoryTags = {};

    const currentLocationTag = location ? currentLocationInLocationTags(location, categorisedTags) : null;
    const urlCategoryTags = urlParams ? urlParamsToCategoryTags(urlParams, categorisedTags) : null;

    if (currentLocationTag) {
        toggledCategoryTags['Location'] = currentLocationTag;
    }

    if (urlCategoryTags) {
        toggledCategoryTags = Object.assign({}, toggledCategoryTags, urlCategoryTags);
    }

    return toggledCategoryTags;

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

export function urlParamsToCategoryTags(urlParams, categorisedTags) {

    const toggledCategoryTags = {};

    for (const entry of urlParams.entries()) {

        const urlCategory = titleCase(entry[0]);
        const urlTag = titleCase(entry[1]);

        if (Object.keys(categorisedTags).includes(urlCategory)) {

            if (urlCategory in categorisedTags && categorisedTags[urlCategory].includes(urlTag)) {

                Object.keys(toggledCategoryTags).includes(urlCategory) && console.warn(`Multiple url tags for category "${urlCategory}"`);
                toggledCategoryTags[urlCategory] = urlTag;

            } else {
                console.warn(`Could not find tag "${urlTag}" (category "${urlCategory}") in categorised tags.`);
            }

        } else {
            console.warn(`Could not find tag "${urlTag}" (category "${urlCategory}") in categorised tags.`);
        }

    }

    return toggledCategoryTags;

}

function titleCase(str) {
    return _.startCase(_.toLower(str));
}