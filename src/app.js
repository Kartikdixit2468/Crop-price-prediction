// Made by Kartik

const express = require('express');
const app = express()
const user_routes = require('./routes/userAuth')
const api_routes = require('./routes/apiRoutes')

// Middlewares
app.use(express.json())


// Defining Routes
app.get('/', (req, res)=> {
    res.send("Awesome!")
})

// For Model!
app.use('/api/model/', api_routes);

app.use('/user/', user_routes);


module.exports = app;