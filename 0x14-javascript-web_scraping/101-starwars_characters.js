#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const charactersUrls = movie.characters;

    charactersUrls.forEach((characterUrl, index) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
          
          // Check if it's the last character to avoid printing extra line breaks
          if (index === charactersUrls.length - 1) {
            console.log("");
          }
        }
      });
    });
  }
});
