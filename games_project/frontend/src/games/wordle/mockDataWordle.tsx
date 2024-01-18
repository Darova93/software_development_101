import { WordleResponse } from "../../types/wordleTypes"

export const getMockResponse = (): WordleResponse[] => {
    return [
        {word: "hotel", missplaced: [4], fails: [0, 1, 2], correct: [3]},
        {word: "motel", missplaced: [4], fails: [0, 1, 2], correct: [3]},
    ]
}
