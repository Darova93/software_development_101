import { useEffect, useRef, useState } from "react";
import { WordleResponse } from "../../types/wordleTypes";
import { PATH_WORDLE_API } from "../../utils/constants";
import Keyboard from "../shared/keyboard";
import { getMockResponse } from "./mockDataWordle";
import "./styles.scss";
import WordleWord from "./wordleWord";

const _response = getMockResponse();

const Wordle = () => {
    const [currentWord, setCurrentWord] = useState<string>(" ")
    const [response, setResponse] = useState(_response)
    
    const handleKeyDown = (event:any) => {
        const char = event.key.toString().toUpperCase()
        let word = currentWord
        if(word.includes(" ")) word = word.slice(0, -1);
        if(char === "ENTER" && word.length === 5) handleEnter()
        if(isLetter(char) && word.length < 5) word += char
        if(char === "BACKSPACE") {
            word = word.slice(0, -1)
            if(!word) word = " "
        }
        setCurrentWord(word)
    }

    const createPayload = () => {
        let payload: {word: string}[] = [];
        response.forEach(element => {
            payload.push({word: element.word})
        });
        payload.push({word: currentWord})
        
        return payload
    }

    const isLetter = (char:string) =>{
        return char.length === 1 && char.match(/[a-z]/i) != null
    }

    const handleEnter = async () => {
        const serverResponse = await wordRequest(PATH_WORDLE_API, createPayload())
        const processedResponse = processResponse(serverResponse)
        if(processResponse.length === 5 && processedResponse[processedResponse.length - 1].correct.length === 5) endGame()
        setCurrentWord(" ")
        setResponse(processedResponse)
    }

    const endGame = () => {
        setCurrentWord('')
        
    }

    const processResponse = (serverResponse: any) => {
        let processedResponse: WordleResponse[] = [];
    
        serverResponse.forEach((element: any) => {
            processedResponse.push({
                word: element.word || "",
                correct: element.correct || [],
                missplaced: element.missplaced || [],
                fails: element.failed || []
            });
        });

        return (processedResponse);
    }

    const wordRequest = async (url: any, data: any) => {
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
    
            if (!response.ok) {
                throw new Error('Fail');
            }
            let serverResponse = await response.json();

            return serverResponse
        } catch (error) {
            console.error('Error:', error);
        }
    };
    
    return(
    <> 
        <div tabIndex={0} className="wordle" onKeyDown={(event) => handleKeyDown(event)}>
        {/* <div tabIndex={0} className="wordle" > */}
            <div className="words-wrapper">
            {response.map((value, index) =>(
                <WordleWord key={`word-${value.word}-${index}`} value = {value} index={index} />
            ))}
            <WordleWord key={`current-word`} value={{word: currentWord, correct: [], missplaced: [], fails: [0, 1, 2, 3, 4]}} index={currentWord.length-1} />
            </div>
            <Keyboard usedLetters={new Set()} keyClickHandler={(a) => console.log(a)} ></Keyboard>
        </div>
    </>
    )
}


export default Wordle
