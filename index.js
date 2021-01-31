require('dotenv').config()
const express = require('express')
const http = require('http')

const app = express()
const router = express.Router()

router.get('/rooms/:roomId', (req, res) => {
  if(req.params.roomId == "ABCD") {
    res.status(200).json({ receiver: "THIS SHOULD BE A FIREBASE REALTIME DB URL" })
  } else {
    res.status(401).json({ error: "Invalid code" })
  }
})
app.use('/', router)

const server = http.createServer(app)
server.listen(process.env.PORT, () => {
  console.log('Listening on http://localhost:' + process.env.PORT)
})