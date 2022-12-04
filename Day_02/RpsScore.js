const fs = require('fs');

const allFileContents = fs.readFileSync('Day_02\\inputProd.txt', 'utf-8');
Lines = allFileContents.split(/\r?\n/)

myDict = {
	"A X": 4,
	"B X": 1,
	"C X": 7,
	"A Y": 8,
	"B Y": 5,
	"C Y": 2,
	"A Z": 3,
	"B Z": 9,
	"C Z": 6
};
count = 0;
Lines.forEach(element => {
	if (element != ""){
		count += myDict[element];
	}
});
console.log(count);