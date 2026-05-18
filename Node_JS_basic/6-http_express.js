const express = require('express');

// Create Express application
const app = express();

// Home route
app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

// Listen on port 1245
app.listen(1245);

module.exports = app;
