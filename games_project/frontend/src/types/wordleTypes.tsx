export type WordleRequest = {
    word:string
}

export type WordleResponse = {
    word: string,
    missplaced: number[],
    fails: number[],
    correct: number[]
}
