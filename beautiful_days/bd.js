const beautifulDays = (i, j, k) => {
    let count = 0;
    for(let x = i; x<=j; x++){
        let reverse = parseInt(x.toString().split('').reverse().join(''));
        if(Math.abs(x-reverse)%k === 0){
            count++;
        }
    }
    return count;
}

console.log(beautifulDays(20,23,6));