process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

// Handle user input
process.stdin.on('data', (data) => {
  process.stdout.write(`Your name is: ${data}`);
});

// Handle program termination
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
