#!/usr/bin/node

/* Prints all characters of a Star Wars movie
 * using the Star wars API
 */

const request = require('request');
const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/films/${movieId}`;

request(url, (error, res, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const json = JSON.parse(body);
  const characters = json.characters;

  const fetchCharacterInfo = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, characterBody) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(characterBody);
          resolve(characterData.name);
        }
      });
    });
  };

  const characterPromises = characters.map((character) => {
    return fetchCharacterInfo(character);
  });

  Promise.all(characterPromises)
    .then((characterNames) => {
      characterNames.forEach((name, index) => {
        console.log(`${index + 1}. ${name}`);
      });
    })
    .catch((error) => {
      console.log(error);
    });
});
