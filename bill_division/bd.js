const billDivision = (bill, k, b) =>{
    let cost = 0;
    for(let i = 0; i < bill.length; i++){
        if(i==k){
            continue;
        }else{
            cost += bill[i];
        }
    }
    let divCost = cost/2;
    if(divCost === b){
        console.log('Bon Appetit');
    } else {
        console.log(b-divCost);
    }
}

billDivision([3, 10, 2, 9], 1, 7);
billDivision([3, 10, 2, 9], 1, 12);