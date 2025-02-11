#!/usr/bin/node
// Number of films with the given character ID
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    const filmsWithCharacter = content.results.filter((film) => {
      return film.characters.some((characterUrl) => {
        return characterUrl.endsWith('/18/');
      });
    });
    console.log(filmsWithCharacter.length);
  }
});
