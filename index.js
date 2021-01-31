require('dotenv').config()
const express = require('express')
const multer = require('multer')
const http = require('http')

const app = express()
const router = express.Router()
const upload = multer({ dest: 'assets/' })

app.post('/upload', upload.single('file'), (req, res, next) => {
  console.log(req.file.filename)
  console.log(req.file.mimetype)
  console.log(req.file.size)
  res.status(200).json({ res: 'Success' })
})

router.get('/rooms/:roomId', (req, res) => {
  if(req.params.roomId == "ABCD") {
    res.status(200).json({ receiver: "THIS SHOULD BE A FIREBASE REALTIME DB URL" })
  } else {
    res.status(401).json({ error: "Invalid code" })
  }
})
app.use('/', router)

const server = http.createServer(app)
const port = process.env.PORT || 8080
server.listen(port, () => {
  console.log('Listening on http://localhost:' + port)
})