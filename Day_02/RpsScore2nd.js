const fs = require('fs');

const allFileContents = fs.readFileSync('Day_02\\inputProd.txt', 'utf-8');
Lines = allFileContents.split(/\r?\n/)

myDict = {
	"A X": 3,
	"B X": 1,
	"C X": 2,
	"A Y": 4,
	"B Y": 5,
	"C Y": 6,
	"A Z": 8,
	"B Z": 9,
	"C Z": 7
}
count = 0;
Lines.forEach(element => {
	if (element != ""){
		count += myDict[element];
	}
});
console.log(count);