import { useState } from "react";
import { WordleResponse } from "../../types/wordleTypes";
import { PATH_WORDLE_API } from "../../utils/constants";
import { getMockResponse } from "./mockDataWordle";
import "./styles.scss";
import WordleWord from "./wordleWord";

const _response = getMockResponse();

const Wordle = () => {
    const [currentWord, setCurrentWord] = useState<string>(" ")
    const [response, setResponse] = useState(_response)

    const handleKeyDown = (event:any) => {
        let char = event.key.toString().toUpperCase()
        let word = currentWord
        if(word.includes(" ")) word = word.slice(0, -1);
        console.log(char)
        if(char === "ENTER" && word.length === 5) handleEnter(PATH_WORDLE_API, createPayload())
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
        return char.length === 1 && char.match(/[a-z]/i);
    }

    const handleEnter = async (url: any, data: any) => {
        console.log(data)
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
    
            if (!response.ok) {
                throw new Error('Fail');
            }
    
            const serverResponse = await response.json();
    
            let processedResponse: WordleResponse[] = [];
    
            serverResponse.array.forEach((element: any) => {
                processedResponse.push({
                    word: element.word,
                    correct: element.correct,
                    missplaced: element.missplaced,
                    fails: element.failed
                });
            });
    
            setResponse(processedResponse);
        } catch (error) {
            console.error('Error:', error);
        }
    };
    
    return(
    <>
        <div tabIndex={0} className="wordle" onKeyDown={(event) => handleKeyDown(event)}>
            <div className="words-wrapper">
            {response.map((value, index) =>(
                <WordleWord key={`word-${value.word}-${index}`} value = {value} index={index} />
            ))}
            <WordleWord key={`current-word`} value={{word: currentWord, correct: [], missplaced: [], fails: [0, 1, 2, 3, 4]}} index={currentWord.length-1} />
            </div>
        </div>
    </>
    )
}





export default Wordle
