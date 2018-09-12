import React from 'react';

export function getConfig() {

    const environment = process.env.NODE_ENV || 'default';

    const config = require('./config/' + environment + '.json');

    return config;

}

export function filterCategoriesToListItems(filterCategories) {
    return filterCategories.map(filterCategory =>
        <li key={filterCategory}>{filterCategory}</li>
    );
}
