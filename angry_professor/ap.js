const angryProfessor = (k, a) => {
    let onTime = 0;
    for (let i = 0; i < a.length; i++) {
        if (a[i] <= 0) {
            onTime++;
        }
    }
    return onTime >= k ? "NO" : "YES";
}


console.log(angryProfessor(3, [-1, -3, 4, 2]));
console.log(angryProfessor(2, [0, -1, 2, 1]));