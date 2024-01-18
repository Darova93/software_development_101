import React, { useEffect } from "react";
import { WordleResponse } from "../../types/wordleTypes";
import { getMockResponse } from "./mockDataWordle";
import "./styles.css";
const response = getMockResponse();

const Wordle = () => {

    useEffect(() => {
        response.forEach(value => {
            console.log(value)
        })
      }, []);
    

    return(
    <>
        <div className="wordle">
            {
            response.map((value, index) =>(
                <WordleWord key={`word-${value}-${index}`} value = {value} index={index} />
            ))}
        </div>
    </>
    )
}

const WordleWord = ({value, index} : {value: WordleResponse, index:number}) => {
    const classes = {
        correct: "correct",
        missing: "missing",
        fail: "fail"
    }

    const getLetterClass = (value:WordleResponse, index:number):string => {
        return "correct"
    }

    return (
        <div className="word">
            {value.word.split("").map((letter, index) => 
                <WordleLetter key={`letter-${letter}-${index}`} letter={letter} index={index} className={getLetterClass(value, index)}/>
            )}
        </div>
    )
}

const WordleLetter = ({letter, index, className} : {letter:string, index:number, className:string}) => {
    return(
            <div className={`letter ${className}`}>
                {letter}
            </div>
    )
}

export default Wordle
