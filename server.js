const express = require("express");
const fs = require("fs");
const axios = require("axios");
const app = express();

app.get("/gym", (req, res) => {
  axios({
    method: "get",
    url: "http://recsports.ufl.edu/cam/cam8.jpg",
    responseType: "stream",
  }).then(function (response) {
    response.data.pipe(fs.createWriteStream("student-rec.jpg"));
  });
});

app.get("/", (req, res) => {
  res.send("hi");
});

app.listen(3000);
