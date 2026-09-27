const smallestMult = require('./smallestMultiple');

test('smallestMult(5) should return a number', () => {
    expect(typeof smallestMult(5)).toBe('number');
});

test('smallestMult(5) should return 60', () => {
    expect(smallestMult(5)).toBe(60);
});

test('smallestMult(7) should return 420', () => {
    expect(smallestMult(7)).toBe(420);
});

test('smallestMult(10) should return 2520', () => {
    expect(smallestMult(10)).toBe(2520);
});

test('smallestMult(13) should return 360360', () => {
    expect(smallestMult(13)).toBe(360360);
});

test('smallestMult(20) should return 232792560', () => {
    expect(smallestMult(20)).toBe(232792560);
});
