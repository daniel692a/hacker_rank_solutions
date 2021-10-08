const sum = (nums) => {
    let sum = 0;
    console.log(nums);
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
    }
    console.log(sum);
    return sum;
}


const birthday = (s, d, m) => {
    let count = 0;
    for (let i = 0; i < s.length; i++) {
        if(sum(s.slice(i, i + m)) === d) {
            count++;
        }
    }
    return count;
}

console.log(birthday([4, 2, 1, 3, 5], 4, 2));