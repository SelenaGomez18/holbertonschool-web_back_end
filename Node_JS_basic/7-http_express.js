const express = require('express');
const fs = require('fs');

const app = express();

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

// Home route
app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

// Students route
app.get('/students', (request, response) => {
  countStudents(process.argv[2])
    .then((data) => {
      response.send(`This is the list of our students\n${data}`);
    })
    .catch((error) => {
      response.send(`This is the list of our students\n${error.message}`);
    });
});

// Listen on port 1245
app.listen(1245);

module.exports = app;
