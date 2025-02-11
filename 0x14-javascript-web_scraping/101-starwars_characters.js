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

    // Create an array of promises for each character request
    const promises = characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            const character = JSON.parse(charBody);
            resolve(character.name);
          }
        });
      });
    });

    // Wait for all promises to resolve and then print the names
    Promise.all(promises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error(error);
      });
  }
});
