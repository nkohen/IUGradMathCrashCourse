var fibCache: number[] = [1, 1]

function fibonacci(m: number): number {
    if (fibCache.length < m){
        for (var i = fibCache.length; i <= m; i++) {
            fibCache[i] = fibCache[i-1] + fibCache[i-2];
        }
    }
    return fibCache[m-1]
}

// computes the golden ratio
function computephi(): number {
    return (Math.sqrt(5) + 1) / 2
}

// approximates the golden ratio using fibonacci sequence
function approxphi(m: number): number {
    let aprxphi = fibonacci(m-2) / fibonacci(m-3);
    return aprxphi
}


let n = 10;
let fibs = fibonacci(n);
let actual = computephi();
let approx = approxphi(n);
let err = actual - approx;
console.log("the " + n + "th fibbonaci number: ", fibs);
console.log("the approximation of the golden ratio:", approx);
console.log("the error in approimation:", err);
