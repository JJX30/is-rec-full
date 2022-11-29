const express = require("express");
const { spawn } = require("child_process");
const app = express();

const childPython = spawn("python3", ["compare.py"]);

app.get("/", (req, res) => {
  res.send("hi");
});

app.listen(3000);
