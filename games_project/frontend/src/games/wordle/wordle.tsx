import { useState } from "react";
import { WordleResponse } from "../../types/wordleTypes";
import { PATH_WORDLE_API } from "../../utils/constants";
import Keyboard from "../shared/keyboard";
import { getMockResponse } from "./mockDataWordle";
import "./styles.scss";
import WordleWord from "./wordleWord";

const Wordle = () => {
    const [currentWord, setCurrentWord] = useState<string>(" ")
    const [response, setResponse] = useState<WordleResponse[]>()
    
    const handleKeyDown = (char:string) => {
        let word = currentWord
        if(word.includes(" ")) word = word.slice(0, -1);
        if(char === "ENTER" && word.length === 5) handleEnter()
        if(isLetter(char) && word.length < 5) word += char
        if(char === "BACKSPACE") {
            word = word.slice(0, -1)
        }
        setCurrentWord(word)
    }

    const createPayload = () => {
        let payload: {word: string}[] = [];
        if(response){
            response.forEach(element => {
                payload.push({word: element.word})
            });           
        }
        payload.push({word: currentWord})
        
        return payload
    }

    const isLetter = (char:string) =>{
        return char.length === 1 && char.match(/[a-zñ]/i) != null
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
    
    const getCurrentLetters = () => {
        return response?.reduce((usedLetters:Set<string>, value:WordleResponse):Set<string> => {
            [...value.word].forEach(char => {
                usedLetters.add(char)
            })
            return usedLetters
        }, new Set<string>())
    }

    return(
    <> 
        <div tabIndex={0} className="wordle" onKeyDown={(event) => handleKeyDown(event.key.toString().toUpperCase())}>
            <div className="words-wrapper">
            {response?.map((value, index) =>(
                <WordleWord key={`word-${value.word}-${index}`} value={value} index={index} className={index === response.length - 1 ? "newWord" : ""}/>
            ))}
            <WordleWord key={`current-word`} value={{word: currentWord, correct: [], missplaced: [], fails: [0, 1, 2, 3, 4]}} index={currentWord.length-1} className="currentWord"/>
            </div>
            <Keyboard usedLetters={getCurrentLetters() || new Set()} keyClickHandler={(key) => handleKeyDown(key)} ></Keyboard>
        </div>
    </>
    )
}


export default Wordle
