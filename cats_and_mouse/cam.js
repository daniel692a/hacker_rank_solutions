const absValue = (x) => Math.abs(x);

const catAndMouse = (x, y, z) => {
    const catA = absValue(x - z);
    const catB = absValue(y - z);

    if (catA === catB) {
        return 'Mouse C';
    }else if (catA < catB) {
        return 'Cat A';
    } else {
        return 'Cat B';
    }
}

console.log(catAndMouse(1, 2, 3));
console.log(catAndMouse(1, 3, 2));