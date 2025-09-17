function multiplesOf3Or5(number) {
	const nums = [];
	for (let i = 1; i < number; i++) {
		if (i % 3 === 0 || i % 5 === 0) {
			nums.push(i);
		}
	}
	return nums.reduce((acc, curr) => acc + curr, 0);
}

module.exports = multiplesOf3Or5;
