const calculateStartDelays = require("./nordicCombined");

describe("nordicCombined", () => {
	describe("calculateStartDelays", () => {
		it("should return [8, 23, 0]", () => {
			expect(calculateStartDelays([120, 110, 125])).toEqual([8, 23, 0]);
		});

		it("should return [11, 0, 5, 8]", () => {
			expect(calculateStartDelays([118, 125, 122, 120])).toEqual([11, 0, 5, 8]);
		});

		it("should return [30, 23, 38, 15, 0, 8, 18]", () => {
			expect(calculateStartDelays([100, 105, 95, 110, 120, 115, 108])).toEqual([
				30, 23, 38, 15, 0, 8, 18,
			]);
		});

		it("should return [3, 11, 6, 18, 21, 15, 8, 26, 0, 12]", () => {
			expect(
				calculateStartDelays([
					130, 125, 128, 120, 118, 122, 127, 115, 132, 124,
				]),
			).toEqual([3, 11, 6, 18, 21, 15, 8, 26, 0, 12]);
		});
	});
});
