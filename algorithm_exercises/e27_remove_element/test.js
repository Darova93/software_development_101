import { removeElement } from "./solution.js";

describe('RemoveElement', () => {
    let testData = [
        { input: [[3, 2, 2, 3], 3], output: [[2, 2], 2] },
        { input: [[0, 1, 2, 2, 3, 0, 4, 2], 2], output: [[0, 1, 3, 0, 4], 5] }
    ]
    testData.forEach((testCase) => {
        it(`should remove the number ${testCase.input[1]} from array ${testCase.input[0]} and return ${testCase.output[1]}`, () => {
            expect(removeElement(testCase.input[0], testCase.input[1])).toEqual(testCase.output[1])
            expect(testCase.input[0]).toEqual(testCase.output[0])
        })
    });
})
