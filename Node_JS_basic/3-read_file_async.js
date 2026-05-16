const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      // Handle file error
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Convert file into lines
      const lines = data.split('\n');

      // Remove empty lines
      const students = lines.filter((line) => line.trim() !== '');

      // Remove header
      const studentLines = students.slice(1);

      console.log(`Number of students: ${studentLines.length}`);

      const fields = {};

      studentLines.forEach((student) => {
        const parts = student.split(',');

        const firstname = parts[0];
        const field = parts[3];

        // Create field array if needed
        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      });

      // Display students by field
      Object.keys(fields).forEach((field) => {
        console.log(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
        );
      });

      resolve();
    });
  });
}

module.exports = countStudents;
