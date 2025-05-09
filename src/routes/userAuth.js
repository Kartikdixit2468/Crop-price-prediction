// Build with proud by Kartik Dixit!

const express = require('express')
const routes = express.Router()

routes.get('/', (req, res)=>{
    res.send("Hello, this route is working successfully!.")
})

module.exports = routes;
