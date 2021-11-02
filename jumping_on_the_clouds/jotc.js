const jumpingOnTheClouds = (c) =>{
    let jumps = 0, i=0;
    while(i<c.length-1){
        if(i<c.length-2 && c[i+2]===0){
            i++;
        }
        jumps++;
        i++;
    }
    return jumps;
}

console.log(jumpingOnTheClouds([0,0,1,0,0,1,0]));
console.log(jumpingOnTheClouds([0, 0, 0, 1, 0, 0, 0]));