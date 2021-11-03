const repeatedString = (s, n) => {
	if(s === 'a'){
		return n
	}else{
		let re = /a/g;
		let repeat_a = s.match(re).length;
		let repeatStr = ~~(n / s.length);
		let totalA = (repeat_a * repeatStr) + s.slice(0, n%s.length).match(re).length;
		return totalA;
	}
}

console.log(repeatedString('aba', 10));
console.log(repeatedString('a', 1000000000000));
