const max = (array) => {
    let max = 0;
    for(let i of array){
        if(i>max){
            max=i;
        }
    }
    return max;
}

const hurdleRace = (k, height) => ( max(height)-k < 0 ) ? 0 : max(height)-k;

console.log(hurdleRace(4, [1, 6, 3, 5, 2]));
console.log(hurdleRace(7, [2, 5, 4, 5, 2]));