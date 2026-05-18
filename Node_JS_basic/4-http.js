const http = require('http');

// Create HTTP server
const app = http.createServer((request, response) => {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');
  response.end('Hello Holberton School!');
});

// Listen on port 1245
app.listen(1245);

module.exports = app;
