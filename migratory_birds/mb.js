const count = (array, item) =>{
    let counter = 0;
    for(let i = 0; i < array.length; i++){
        if (array[i] === item){
            counter++;
        }
    }
    return counter;
}

const migratoryBirds = (array) =>{
    let uniqueItems = new Set(array);
    let  id_max = 0, max_val = 0;
    const counterItems = {};
    for(let item of uniqueItems){
        counterItems[item] = count(array, item);
    }
    for (const key in counterItems) {
        if(counterItems[key] > max_val){
            max_val = counterItems[key];
            id_max = key;
        }
    }
    return id_max;
}

console.log(migratoryBirds([1, 4, 4, 4, 5, 3]));
console.log(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]));