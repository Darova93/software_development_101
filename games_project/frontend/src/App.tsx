import './App.css';
import Wordle from './games/wordle/wordle';
import './styles/global.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Wordle />
      </header>
    </div>
  );
}

export default App;
