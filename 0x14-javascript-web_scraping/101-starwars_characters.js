#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide the movie ID as an argument.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    const names = [];

    characters.forEach((characterUrl, index) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const character = JSON.parse(charBody);
          names[index] = character.name;
          if (names.length === characters.length) {
            names.forEach(name => console.log(name));
          }
        }
      });
    });
  }
});
