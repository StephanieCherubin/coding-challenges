const FIZZ: string = 'fizz'
const BUZZ: string = 'buzz'
const FIZZBUZZ: string = 'fizzbuzz'

/** 
 * Returns true when n is divisible by 3 
 * @param {Number} n
 * @returns {Boolean} fizziness 
 * */
function isFizzy(n: number): boolean {
  return n % 3 === 0
}

/**
 * Returns true when n is divisible by 5
 * @param {Number} n 
 * @returns {Boolean} buzziness
 */
function isBuzzy(n: number): boolean {
  return n % 5 === 0
}

/**
 * Returns FIZZ, BUZZ, or FIZZBUZZ when a number is divisible by 3, 5, or both
 * @param {Number} n
 * @returns {String} '', 'FIZZ', 'BUZZ', or 'FIZZBUZZ'
 */
function fizzyBuzzy(n:number): string {
  let result = ''
  if (isFizzy(n)) { result += FIZZ }
  if (isBuzzy(n)) { result += BUZZ }
  return result
}


interface FizzBuzzResult {
  count: number,
  fizz: number,
  buzz: number
  fizzBuzz: number
}

/**
 * Generates a results object describing a sequence of fizz buzz for count.
 * @param {Number} count 
 * @returns {Object} with properties count, fizz, buzz, and fizzbuzz
 */
function fizzBuzz(count: number): FizzBuzzResult {
  const fizz = Math.floor(count/ 3)
  const buzz = Math.floor(count / 5)
  const fizzBuzz = Math.floor(count / 3 * 5)
  return { fizz, buzz, count, fizzBuzz}
  
}

module.exports.isFizzy = isFizzy
module.exports.isBuzzy = isBuzzy
module.exports.fizzyBuzzy = fizzyBuzzy
module.exports.fizzBuzz = fizzBuzz
module.exports.FIZZ = FIZZ
module.exports.BUZZ = BUZZ
module.exports.FIZZBUZZ = FIZZBUZZ
