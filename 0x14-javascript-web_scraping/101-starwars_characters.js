#!/usr/bin/node
const myArgs = process.argv.slice(2);
const reqURL = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
const request = require('request');
const charactersDict = {};
let id = '';
function firstRequest () {
  return new Promise((resolve, reject) => {
    request(reqURL, function (error, response, body) {
      if (error) {
        console.log(error);
        reject(error);
      } else {
        const characters = JSON.parse(body).characters;
        for (const i of characters) {
          charactersDict[i.slice(37, -1)] = i;
          request(i, function (error, response, body) {
            if (error) {
              console.log(error);
            } else {
              id = JSON.parse(body).url.slice(37, -1);
              charactersDict[id] = JSON.parse(body).name;
            }
            if (i === characters[characters.length - 1]) {
              resolve(charactersDict);
            }
          });
        }
      }
    });
  });
}

async function asyncCall () {
  const result = await firstRequest();
  for (const i in result) {
    console.log(result[i]);
  }
}

asyncCall();
