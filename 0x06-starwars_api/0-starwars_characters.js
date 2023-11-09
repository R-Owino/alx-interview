#!/usr/bin/node

/* Prints all characters of a Star Wars movie
 * using the Star wars API
 */

const request = require('request');

function getJson (url) {
  return new Promise((resolve, reject) => {
    request({ url, json: true, followAllRedirects: true }, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

if (process.argv.length === 3) {
  const movieId = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  getJson(url)
    .then(film => {
      const characterPromises = film.characters.map(getJson);
      return Promise.all(characterPromises);
    })
    .then(characters => {
      characters.forEach(character => {
        console.log(character.name);
      });
    })
    .catch(error => {
      console.log(error);
    });
}
