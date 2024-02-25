#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const movie = JSON.parse(body);
  for (const character of movie.characters) {
    await new Promise((resolve, reject) => {
      request(character, function (error, response, body) {
        if (error) {
          console.error('error:', error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
}
);
