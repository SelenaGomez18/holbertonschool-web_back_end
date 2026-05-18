const http = require('http');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n');

      const students = lines.filter((line) => line.trim() !== '');

      const studentLines = students.slice(1);

      let output = `Number of students: ${studentLines.length}`;

      const fields = {};

      studentLines.forEach((student) => {
        const parts = student.split(',');

        const firstname = parts[0];
        const field = parts[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      });

      Object.keys(fields).forEach((field) => {
        output += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
      });

      resolve(output);
    });
  });
}

const app = http.createServer((request, response) => {
  response.setHeader('Content-Type', 'text/plain');

  if (request.url === '/') {
    response.statusCode = 200;
    response.end('Hello Holberton School!');
  } else if (request.url === '/students') {
    response.statusCode = 200;

    countStudents(process.argv[2])
      .then((data) => {
        response.end(`This is the list of our students\n${data}`);
      })
      .catch((error) => {
        response.end(`This is the list of our students\n${error.message}`);
      });
  } else {
    response.statusCode = 404;
    response.end();
  }
});

app.listen(1245);

module.exports = app;
