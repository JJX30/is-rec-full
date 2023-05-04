const express = require("express");
const fs = require("fs");
const axios = require("axios");
const app = express();

const oneLiner = [
  "Are you ready to get 'Student Rekt'!",
  "Sweating orange and blue.",
  "Building muscles and brain power since 1853.",
  "Don't skip leg day, or Gator day.",
  "How do we know?",
  "Albert goes to Marston...",
  "Go gata!",
  "is-grog-full coming soon...",
  "Missing Kent Fuchs :(",
  "Ben Sasse has a p kink",
  "3 Chik-Fil-A's, 2 gyms",
];

/* endpoint should save previous image and update image jpeg and find the difference between 
   both using compare.py, gonna have to switch jpg's too */
app.get("/gym", (req, res) => {
  axios({
    method: "get",
    url: "http://recsports.ufl.edu/cam/cam8.jpg",
    responseType: "stream",
  }).then(function (response) {
    response.data.pipe(fs.createWriteStream("student-rec.jpg"));
    res.send("image received");
  });
});

// send a random one-liner string from oneLiner list
app.get("/random", (req, res) => {});

app.get("/", (req, res) => {
  res.send("hi");
});

app.listen(3001);
