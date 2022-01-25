const marsExploration = (s) => {
    let countWrongs = 0;
    for(let i=0; i < s.length; i++){
        if(i%3==1){
            if(s[i] !== 'O'){
                countWrongs++;
            }
        } else if(s[i] !== 'S'){
            countWrongs++;
        }
    }
    return countWrongs;
}

console.log(marsExploration("SOSSPSSQSSOR"));
console.log(marsExploration("SOSSOT"));