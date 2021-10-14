const count = (array, item) =>{
    let counter = 0;
    for(let i = 0; i < array.length; i++){
        if(array[i] === item){
            counter++;
        }
    }
    return counter;
}

const sock_merchant = (n, ar) => {
    let pairs = 0;
    let uniqueColors = new Set(ar);
    let countSock = {};
    console.log(uniqueColors);
    for (let i = 0; i < uniqueColors.size; i++) {
        countSock[i] = count(ar, uniqueColors);
    }
    console.log(countSock);
    for (const key in countSock) {
        pairs += Math.floor(countSock[key] / 2);
    }
    return pairs;
};


console.log(sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]));