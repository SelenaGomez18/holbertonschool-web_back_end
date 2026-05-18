import fs from 'fs';

const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (error, data) => {
    if (error) {
      reject(error);
      return;
    }

    const lines = data.split('\n');

    const students = lines.filter((line) => line.trim() !== '');

    const studentLines = students.slice(1);

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

    resolve(fields);
  });
});

export default readDatabase;
