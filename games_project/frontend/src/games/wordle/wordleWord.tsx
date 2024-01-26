import { WordleResponse } from "../../types/wordleTypes"
import WordleLetter from "./wordleLettter"

const WordleWord = ({value, index, className=""} : {value: WordleResponse, index:number, className:string}) => {
    const classes = {
        correct: "correct",
        missing: "missing",
        fail: "fail"
    }

    const getLetterClass = (value:WordleResponse, index:number):string => {
        if(value.correct.includes(index)) return classes.correct
        if(value.missplaced.includes(index)) return classes.missing
        return classes.fail
    }

    return (
        <div className={`word ${className}`}>
            {value.word.split("").map((letter, index) => 
                <WordleLetter key={`letter-${letter}-${index}`} letter={letter} index={index} className={getLetterClass(value, index)}/>
            )}
        </div>
    )
}

export default WordleWord