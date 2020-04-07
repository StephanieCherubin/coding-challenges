/*Given an array of values you need to map the values on to a grid. Return an array of objects containing the original value, and a row and col that would represent the position of where the object would map on the grid. Assume the length of the original array is always a square e.g. 4, 9, 16 etc. Assume the grid has an equal height and width.
*/

arr =[1,2,1,1,
    1,2,2,1,
    1,2,3,0,
    1,1,1,0]
    
function grid(arr) {
    const array_width = Math.sqrt(arr.length)
    final_grid = []
    
    for (let item = 0; item < arr.length; item += array_width) {
        subarray = arr.slice(item, item + array_width)
        final_grid.push(subarray)
    }
    return final_grid
}

console.log(grid(arr))




