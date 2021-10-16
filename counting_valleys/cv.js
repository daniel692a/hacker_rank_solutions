const countigValleys = (steps, path) => {
    let valleys = 0, seaLevel = 0;
    for (const step of path) {
        (step === 'U') ? seaLevel++ : seaLevel--;
        if(seaLevel===0 && step ==='U') valleys++;
    }
    return valleys;
}

console.log(countigValleys(8, 'UDDDUDUU'));
console.log(countigValleys(12, 'DDUUDDUDUUUD'));