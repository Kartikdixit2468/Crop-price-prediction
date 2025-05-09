// Build with proud by Kartik Dixit!

const express = require('express')
const routes = express.Router()

routes.get('/', (req, res)=>{
    res.send("Hello, server running successfully and this route should only be used for getting data through the model.")
})

module.exports = routes;