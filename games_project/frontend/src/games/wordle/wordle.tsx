import React, { useEffect, useState } from "react";
import { WordleResponse } from "../../types/wordleTypes";
import { getMockResponse } from "./mockDataWordle";
import "./styles.scss";
import WordleWord from "./wordleWord";
const response = getMockResponse();

const Wordle = () => {
    
    const [wordList, setWordList] = useState<string[]>([])
    const [currentWord, setCurrentWord] = useState<string>("")
    const handleKeyDown = (event:any) => {
        let char = event.key.toString().toUpperCase()
        let word = currentWord
        if(char === "ENTER" && word.length === 5) handleEnter()
        if(isLetter(char) && word.length < 5) word += char;
        if(char === "BACKSPACE") word = word.slice(0, -1);
        setCurrentWord(word)
    }

    const isLetter = (char:string) =>{
        return char.length === 1 && char.match(/[a-z]/i);
    }

    const handleEnter = () => {
        console.log("ENTER")
    }

    return(
    <>
        <div tabIndex={0} className="wordle" onKeyDown={(event) => handleKeyDown(event)}>
            {
            response.map((value, index) =>(
                <WordleWord key={`word-${value.word}-${index}`} value = {value} index={index} />
            ))}
            <WordleWord key={`current-word`} value={{word: currentWord, correct: [], missplaced: [], fails: [0, 1, 2, 3, 4]}} index={currentWord.length-1} />
        </div>
    </>
    )
}





export default Wordle
