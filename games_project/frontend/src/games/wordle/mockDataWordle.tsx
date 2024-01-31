import { WordleResponse } from "../../types/wordleTypes"

export const getMockResponse = (): WordleResponse[] => {
    return [
        {word: "HOTEL", missplaced: [4], fails: [0, 1, 2], correct: [3]},
        {word: "MOTEL", missplaced: [4], fails: [0, 1, 2], correct: [3]},
        {word: "PELOS", missplaced: [1, 2], fails: [0, 3], correct: [4]},
        {word: "LUNAS", missplaced: [], fails: [3], correct: [0, 1, 2, 4]}
    ]
}
