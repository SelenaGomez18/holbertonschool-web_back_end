import express from 'express';
import router from './routes';

const app = express();

// Use routes
app.use('/', router);

// Listen on port 1245
app.listen(1245);

export default app;
