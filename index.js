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
server.listen(80, () => {
  console.log('Listening on http://localhost:' + 8080)
})