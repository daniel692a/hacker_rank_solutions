const getMoneySpent = (keyboards, drives, b) => {
    let max_price = -1;
    for(let keyboard of keyboards){
        for(let drive of drives){
            if(((keyboard + drive) <= b) && (keyboard + drive) > max_price){
                max_price = keyboard + drive;
            }
        }
    }
    return max_price;
}

console.log(getMoneySpent([3, 1], [5, 2, 8], 10));