fs = require("fs");

let content = fs.readFileSync("input4.txt", "utf-8");

content = content.split(/\r?\n/);

const expr = /(\d{2})(-|\.\.\.|:)(\d{2})\2(\d{2})\2(\d{2})/;

for (const line of content) {
    console.log(line.match(expr).map((x) => [...x]));
}
