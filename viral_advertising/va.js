const viralAdvertising = (n) => {
    let likes = 2, shares = 5;
    for(let i=1; i<n; i++){
        shares = ~~(shares/2) *3;
        likes += ~~(shares/2);
    }
    return likes;
}

console.log(viralAdvertising(5));
console.log(viralAdvertising(3));