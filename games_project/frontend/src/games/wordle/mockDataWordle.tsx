import { WordleResponse } from "../../types/wordleTypes"

export const getMockResponse = (): WordleResponse[] => {
    return [
        {word: "HOTEL", missplaced: [4], fails: [0, 1, 2], correct: [3]},
        {word: "MOTEL", missplaced: [4], fails: [0, 1, 2], correct: [3]},
        {word: "BARBA", missplaced: [], fails: [0, 1, 2, 3, 4], correct: []},
        {word: "MAMAS", missplaced: [], fails: [0, 1, 2, 3, 4], correct: []}

    ]
}
