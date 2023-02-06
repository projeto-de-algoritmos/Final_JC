import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom'
import MapImage from '../../assets/mapEasy.jpg';
import './index.css';

function EasyPage() {
  const navigate = useNavigate()
  const [answer, setAnswer] = useState('')
  const [graphAns, setGraphAns] = useState({})
  const [showAnswer, setShowAnswer] = useState(false)
  const [tryAgain, setTryAgain] = useState(false)
  const [userAnswer, setUserAnswer] = useState(true)

  function handleChangeAnswer(value) {
    setAnswer(value)
    console.log(answer)
  }

  function handleSubmitAnswer() {
    if (answer == 30 - graphAns['custo']) {
      setShowAnswer(true)
      setUserAnswer(false)
    }
    else {
      setTryAgain(true)
      setUserAnswer(false)
    }
  }

  function handleSubmitTryAgain() {
    setTryAgain(false)
    setUserAnswer(true)
  }

  const getApiData = async () => {
    await fetch(`http://localhost:8004/easy`)
      .then((response) => response.json())
      .then((data) => {
        setGraphAns(data)
      });
  }

  useEffect(() => {
    getApiData();
  }, []);

  const data_city = {
    "Kingdom of Tentes": 12,
    "Gey": -13,
    "Principality of Montih": 5,
    "Republic of Nyirkad": 7,
    "Kingdom of Merland": -2,
    "Principality of Sicocoria": 6,
  }

  return (
    <div className='easy-mode'>
      <div className='map-easy'>
        <img className='map-easy-image' src={MapImage} />
      </div>
      <div className='info-easy'>

        {userAnswer && (
          <>
            <h2 className='desc'>Valor inicial na carteira: 30</h2>
            <h2 className='desc'>Valor para entrar em cada reino:</h2>
            <h2 className='desc'>Kingdom of Tentes: {data_city['Kingdom of Tentes']}</h2>
            <h2 className='desc'>Gey: {data_city['Gey']}</h2>
            <h2 className='desc'>Principality of Montih: {data_city['Principality of Montih']}</h2>
            <h2 className='desc'>Republic of Nyirkad: {data_city['Republic of Nyirkad']}</h2>
            <h2 className='desc'>Kingdom of Merland: {data_city['Kingdom of Merland']}</h2>
            <h2 className='desc'>Principality of Sicocoria: {data_city['Principality of Sicocoria']}</h2>
            <h2 className='desc'>Indo de {graphAns['cidade inicial']} para {graphAns['cidade de destino']}, quanto de ouro você teria no final?</h2>
            <div className='input-container'>
              <h2 className='desc'>Valor final na carteira: </h2>
              <input onChange={(e) => handleChangeAnswer(e.target.value)}
                type="text"
                value={answer}
                name="answer"
                className="input" />
              <button onClick={handleSubmitAnswer} className="button">Enviar</button>
            </div>
          </>
        )}

        {tryAgain && (
          <div className='show-answer'>
            <h2 className='desc'>Você Errou!</h2>
            <button onClick={handleSubmitTryAgain} className="button-try-again">Tentar Novamente</button>
          </div>
        )}

        {showAnswer && (
          <>
            <h2 className='desc'>Você Acertou! O caminho, gastando apenas {graphAns['custo']} e ficando com {30 - graphAns['custo']} na carteira, seria:</h2>
            <h2 className='desc'>{graphAns['caminho'].join("->")}</h2>
          </>
        )}

        <button className="button-return" onClick={() => navigate("/")}>Voltar</button>
      </div>
    </div>
  );
}

export default EasyPage;
