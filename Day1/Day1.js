'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
process.stdin.resume();
process.stdin.setEncoding('utf-8');
var inputString = '';
var inputLines = [];
var currentLine = 0;
process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});
process.stdin.on('end', function () {
    inputLines = inputString.split('\n');
    inputString = '';
    main();
});
function readLine() {
    return inputLines[currentLine++];
}
/*
 * Complete the 'diagonalDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */
function diagonalDifference(arr) {
    // Write your code here
    var size = arr.length;
    var ad = 0;
    for (var i = 0; i < size; i++) {
        ad += arr[i][i] - arr[i][size - 1 - i];
    }
    return Math.abs(ad);
}
function main() {
    var n = parseInt(readLine().trim(), 10);
    var arr = Array(n);
    for (var i = 0; i < n; i++) {
        arr[i] = readLine().replace(/\s+$/g, '').split(' ').map(function (arrTemp) { return parseInt(arrTemp, 10); });
    }
    var result = diagonalDifference(arr);
    console.log(result);
}
