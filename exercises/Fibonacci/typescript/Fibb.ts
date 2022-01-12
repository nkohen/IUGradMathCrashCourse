var i = 2;
let N = 10

var f :number[]=[N]

f[0] = 1;
f[1] = 1;

for (i = 2; i <=N-1; i++){
    f[i] = f[i-1]+f[i-2];
}


console.log(f[N-1]);