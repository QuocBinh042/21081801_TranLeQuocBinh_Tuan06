// app.js
const http = require('http');
const PORT = 3000;

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello, Docker!');
});

server.listen(PORT, () => {
  console.log(`Server đang chạy trên cổng ${PORT}`);
});
