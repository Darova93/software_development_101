import { useEffect, useState } from "react";
import { WordleResponse } from "../../types/wordleTypes";
import { PATH_WORDLE_API_DANI, PATH_WORDLE_API_KUBO } from "../../utils/constants";
import Keyboard from "../shared/keyboard";
import { getMockResponse } from "./mockDataWordle";
import "./styles.scss";
import WordleWord from "./wordleWord";

const Wordle = () => {
    const [currentWord, setCurrentWord] = useState<string>(" ")
    const [response, setResponse] = useState<WordleResponse[]>()

    useEffect(() => {
        const lastGuess = document.getElementsByClassName('last-guess')[0];
        guessAnimation(lastGuess);
        
    }, [response])

    const guessAnimation = (guess:Element) =>{
        if(guess) {
            Array.from(guess.getElementsByClassName('letter'))?.forEach((element, index) => {
                setTimeout(() => {
                    element.animate({transform: ['rotateX(0)', 'rotateX(90deg)']}, {duration: 250, iterations: 1, easing: "ease-in"}).addEventListener('finish', () => {
                        if(element.classList.contains('correct')) element.classList.add("correctGuessed");
                        if(element.classList.contains('missing')) element.classList.add("missingGuessed");
                        if(element.classList.contains('fails')) element.classList.add("failGuessed");
                        element.animate({transform: ['rotateX(90deg)', 'rotateX(0)']}, {duration: 250, iterations: 1, easing: "ease-out"})
                    });
                }, (index * 500 / 2));
            })
        }
    }
    
    const handleKeyDown = (char:string) => {
        let word = currentWord;
        if(word.includes(" ")) word = word.slice(0, -1);
        if(char === "ENTER") {
            handleEnter();
            return;
        }
        if(!isLetter(char) && !(char === "BACKSPACE")) {
            shakeWord();
            return;
        }
        if(isLetter(char) && word.length < 5) word += char;
        if(char === "BACKSPACE") {
            word = word.slice(0, -1);
        }
        if(word.length === 0) word = " ";
        setCurrentWord(word);
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

    const createPayload = () => {
        let payload: {word: string}[] = [];
        response.forEach(element => {
            payload.push({word: element.word})
        });
        payload.push({word: currentWord})
        
        return payload
    }

    const isLetter = (char:string) =>{
        return char.length === 1 && char.match(/[a-zñ]/i) != null
    }

    const handleEnter = async () => {
        if(currentWord.length < 5) {
            shakeWord();
            return;
        }
        try{
            const serverResponse = await wordRequest(PATH_WORDLE_API_DANI, createPayload());
            const processedResponse = processResponse(serverResponse);
            if(processResponse.length <= 5 && processedResponse[processedResponse.length - 1].correct.length === 5) {endGame();}
            setCurrentWord(" ");
            setResponse(processedResponse);
        }
        catch(e){
            console.log(e);
        }
    }

    const shakeWord = () => {
        document.getElementsByClassName('current-word')[0].animate({
            transform: ["translate(-5%)", "translateX(5%)", "translateX(-10%)", "translateX(10%)", "translateX(-5%)", "translateX(0)"],
            offset: [.1, .3, .5, .7, .9, 1]
      }, {
        duration: 150,
        iterations: 1,
        easing: "ease-in-out"
      });
    }

    const endGame = () => {
        setCurrentWord('')
        alert()
    }

    const processResponse = (serverResponse: any) => {
        let processedResponse: WordleResponse[] = [];
    
        serverResponse.forEach((element: any) => {
            processedResponse.push({
                word: element.word || "",
                correct: element.correct || [],
                missplaced: element.missplaced || [],
                fails: element.fails || []
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
                <WordleWord key={`word-${value.word}-${index}`} value={value} index={index} className={index === response.length - 1 ? "last-guess" : "past-guess"}/>
            ))}
            <WordleWord key={`current-word`} value={{word: currentWord, correct: [], missplaced: [], fails: []}} index={currentWord.length-1} className="current-word"/>
            </div>
            <Keyboard usedLetters={getCurrentLetters() || new Set()} keyClickHandler={(key) => handleKeyDown(key)} ></Keyboard>
        </div>
    </>
    )
}


export default Wordle
