const minimumDistances = (a) =>{
    for(let distance=1; distance<a.length; distance++){
        for(let i=0; i<(a.length-distance); i++){
            if(a[i]===a[i+distance]){
                return distance;
            }
        }
    }
    return -1;
}

console.log(minimumDistances([7, 1, 3, 4, 1, 7]))
console.log(minimumDistances([1, 2, 1, 2, 1, 2, 1]))