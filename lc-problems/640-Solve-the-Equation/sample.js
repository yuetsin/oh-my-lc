/**
 * @param {string} equation
 * @return {string}
 */
var solveEquation = function(equation) {
    let equality = equation.split('=')
    let left = equality[0]
    let right = equality[1]
    
    let leftSum = getSum(left)
    let rightSum = getSum(right)
    
    let leftXSum = getXSum(left)
    let rightXSum = getXSum(right)
    
    let x = leftXSum - rightXSum
    let num = rightSum - leftSum
    if (x === 0 && num === 0) {
        return "Infinite solutions"
    }
    
    let res = '';
    res = num / x
    if (!isFinite(res)) {
        return 'No solution'
    }
    
    return `x=${res}`
};

var getSum = function(equation) {
    return eval(equation.replace(/[0-9]*x/gm, 0))
}

var getXSum = function(equation) {
    let xArray = equation.match(/(\+|-)?[0-9]*x/gm)
    if (xArray === null) {
        return 0;
    }
    return xArray.reduce((res, val) => {
        if (val === 'x' || val === '+x') {
            res++
        } else if (val === '-x') {
            res--;
        } else {
            res = res + 1 * val.replace('x', '')
        }
        return res
    }, 0)
}