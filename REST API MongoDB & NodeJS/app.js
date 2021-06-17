const express = require('express');
const app = express();
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');
require('dotenv/config')


//Middleswares, case could be authentication 
// app.use("/posts", () => {
//     console.log("This is a middleware running")
// });

//Middlewares
app.use(cors());
app.use(bodyParser.json());

//import routes
const postsRoute = require('./routes/posts');
app.use('/posts', postsRoute);

//ROUTES
app.get("/", (req, res) => {
    res.send("we are on home");
});

// Connect to db, send in parameters to avoid deprication warnings
mongoose.connect(
    process.env.DB_CONNECTION, { useNewUrlParser: true , useUnifiedTopology: true }, ()=> {
    console.log("connected to db")
});

//Start listening to server
app.listen(3000);