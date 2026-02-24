function calculateStartDelays(jumpScores) {
	const bestJumpScore = Math.max(...jumpScores);
	const delays = jumpScores.map((jumpScore) => {
		const delay = Math.ceil((bestJumpScore - jumpScore) * 1.5);
		return delay;
	});

	return delays;
}

module.exports = calculateStartDelays;
