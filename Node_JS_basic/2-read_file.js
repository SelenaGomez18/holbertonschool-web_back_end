const fs = require('fs');

function countStudents(path) {
  let data;

  // Read file synchronously
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  // Convert file into lines
  const lines = data.split('\n');

  // Remove empty lines
  const students = lines.filter((line) => line.trim() !== '');

  // Remove header row
  const studentLines = students.slice(1);

  console.log(`Number of students: ${studentLines.length}`);

  const fields = {};

  studentLines.forEach((student) => {
    const parts = student.split(',');

    const firstname = parts[0];
    const field = parts[3];

    // Create array if field doesn't exist
    if (!fields[field]) {
      fields[field] = [];
    }

    // Add firstname to field
    fields[field].push(firstname);
  });

  // Display students by field
  Object.keys(fields).forEach((field) => {
    console.log(
      `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
    );
  });
}

module.exports = countStudents;
