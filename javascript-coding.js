// Write a function that uppercases the first character of string
firstUpper = (string) => { // javascript libraries
	return string.charAt(0).toUpperCase() + string.slice(1)
}

'''Write a function that uppercases the first letter of each word in a string'''
wordUpper = (string) => {
	const wordList = string.split(" ")
	let finalString = ""
  wordList.forEach((word, _) => {
    const result = firstUpper(word)
    finalString = finalString.concat(result, " ")
  })
	return finalString.slice(0, -1)
}

console.log(firstUpper("javascript libraries"))
console.log(wordUpper("javascript libraries"))

"""Write a function that uppercases every other letter """
uppercaseEveryOtherLetter = (string) => {

}

// Write a function that removes all whitespace from a given string
// Write a function that removes only the extra whitespace from a given string (example: “ a        b ” → “a b”)