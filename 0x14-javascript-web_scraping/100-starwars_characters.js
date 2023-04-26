#!/usr/bin/node
const myArgs = process.argv.slice(2);
const reqURL = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
const request = require('request');
request(reqURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const i of characters) {
      request(i, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});;
