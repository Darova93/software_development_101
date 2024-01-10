// const RemoveElement = require('solution.js');
import { removeElement } from "./solution.js";

describe('RemoveElement', () => {

    it('should remove the numbers 3 from array element and return 2', () => {
        let arrayToTest = [3, 2, 2, 3]
        let valueToTest = 3
        expect(removeElement(arrayToTest, valueToTest)).toEqual(2)
        expect(arrayToTest).toEqual([2, 2])
    })

})

describe('RemoveElement', () => {

    it('should remove the numbers 3 from array element and return 2', () => {
        let arrayToTest = [0, 1, 2, 2, 3, 0, 4, 2]
        let valueToTest = 2
        expect(removeElement(arrayToTest, valueToTest)).toEqual(5)
        expect(arrayToTest).toEqual([0, 1, 3, 0, 4])
    })

})
