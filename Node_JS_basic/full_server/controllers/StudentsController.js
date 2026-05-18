import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2])
      .then((fields) => {
        const sortedFields = Object.keys(fields).sort((a, b) => a.localeCompare(b));

        let output = 'This is the list of our students';

        sortedFields.forEach((field) => {
          output += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
        });

        response.status(200).send(output);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(process.argv[2])
      .then((fields) => {
        response.status(200).send(`List: ${fields[major].join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
