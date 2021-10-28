const circularArrayRotation = (a, k, queries) => {
    for(let i = 0; i<k; i++){
        let last  = a[a.length-1];
        a.pop();
        a.unshift(last);
    }
    return queries.map(q => a[q]);
    // const arr = [];
    // for (let i = 0; i < a.length; i++) {
    //     const index = (i + k) % a.length;
    //     arr[index] = a[i];
    // }
    // return queries.map(q => arr[q]);
}

console.log(circularArrayRotation([1, 2, 3], 2, [0, 1, 2]));