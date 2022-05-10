# Lab: Serverless Function


# Features
Create a serverless function following Vercel’s get-started directions that handles two kinds of queries:
The serverless function should handle a GET http request with a given country name that responds with a string with the form The capital of X is Y
E.g./capital-finder?country=Chile should generate an http response of The capital of Chile is Santiago.
The serverless function should handle a GET http request with a given capital that responds with a string with the form The capital of X is Y
E.g./capital-finder?capital=Santiago should generate an http response of Santiago is the capital of Chile.


# Working urls
search by country: https://capital-finder-gamma.vercel.app/api/capital_finder?name=france
search by capital: https://capital-finder-gamma.vercel.app/api/capital_finder?capital=kathmandu