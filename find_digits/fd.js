const findDigits = (n) => {
	let count = 0;
	for(let i = 0; i< n.toString().length; i++){
		if(parseInt(n.toString()[i]) === 0){
			continue;
		} else if(n % parseInt(n.toString()[i]) === 0){
			count++;
		}
	}
	return count;
}

console.log(findDigits(12));
console.log(findDigits(1012));