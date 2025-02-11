#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL as an argument.');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const wedgeFilms = films.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(wedgeFilms.length);
  }
});
