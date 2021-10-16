const min = (val1, val2) => (val1<val2) ? val1 : val2;

const pageCount = (n, p)=> min(~~(p/2), ((~~(n/2))-(~~(p/2))));

console.log(pageCount(6, 5));
console.log(pageCount(6, 2));
console.log(pageCount(5, 4));
console.log(pageCount(73201, 57075));