import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom'
import MapImage from '../../assets/mapHard.jpg';
import './index.css';

function HardPage() {
  const navigate = useNavigate()
  const [answer, setAnswer] = useState('')
  const [showAnswer, setShowAnswer] = useState(false)
  const [graphAns, setGraphAns] = useState({})
  const [tryAgain, setTryAgain] = useState(false)
  const [userAnswer, setUserAnswer] = useState(true)

  function handleChangeAnswer(value) {
    setAnswer(value)
    console.log(answer)
  }

  function handleSubmitAnswer() {
    if (answer == 40 - graphAns['custo menor energia'] ||  answer == 40 + graphAns['custo mais rentavel']) {
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
    await fetch(`http://localhost:8004/hard`)
      .then((response) => response.json())
      .then((data) => {
        setGraphAns(data)
      });
  }

  useEffect(() => {
    getApiData();
  }, []);

  const data_hard = {
    "Kingdom of Tentes": 30,
    "Gey": -25,
    "Principality of Montih": 43,
    "Republic of Nyirkad": 4,
    "Kingdom of Merland": 1,
    "Principality of Sicocoria": -3,
    "Kingdom of Guileria": 12,
    "Kingdom of Givrairatil": -24,
    "Grand Duchy of Lignia": 40,
    "Douchientian Theocracy": -37,
    "United Provinces of Rouertia": 31,
    "Bishopric of Silgulia": 37,
    "Lharanha": -2
  }

  return (
    <div className='hard-mode'>
      <div className='map'>
        <img className='map-image' src={MapImage} />
      </div>
      <div className='info'>
        {userAnswer && (
          <>
            <h2 className='desc'>Valor inicial na carteira e total de energia: 40</h2>
            <h2 className='desc'>Valor para entrar em cada reino:</h2>
            <div className='info-container'>
              <div className='left-info'>
                <h2 className='desc'>Kingdom of Tentes: {data_hard['Kingdom of Tentes']}</h2>
                <h2 className='desc'>Gey: {data_hard['Gey']}</h2>
                <h2 className='desc'>Principality of Montih: {data_hard['Principality of Montih']}</h2>
                <h2 className='desc'>Republic of Nyirkad: {data_hard['Republic of Nyirkad']}</h2>
                <h2 className='desc'>Kingdom of Merland: {data_hard['Kingdom of Merland']}</h2>
                <h2 className='desc'>Principality of Sicocoria: {data_hard['Principality of Sicocoria']}</h2>
              </div>
              <div className='right-info'>
                <h2 className='desc'>Kingdom of Guileria: {data_hard['Kingdom of Guileria']}</h2>
                <h2 className='desc'>United Provinces of Rouertia: {data_hard['United Provinces of Rouertia']}</h2>
                <h2 className='desc'>Kingdom of Givrairatil: {data_hard['Kingdom of Givrairatil']}</h2>
                <h2 className='desc'>Douchientian Theocracy: {data_hard['Douchientian Theocracy']}</h2>
                <h2 className='desc'>Grand Duchy of Lignia: {data_hard['Grand Duchy of Lignia']}</h2>
                <h2 className='desc'>Lharanha: {data_hard['Lharanha']}</h2>
                <h2 className='desc'>Bishopric of Silgulia: {data_hard['Bishopric of Silgulia']}</h2>
              </div>
            </div>
            <h2 className='desc'>Indo de {graphAns['cidade inicial']} para {graphAns['cidade de destino']}, quanto de ouro ou energia você teria no final?</h2>
            <div className='input-container'>
              <input onChange={(e) => handleChangeAnswer(e.target.value)}
                type="text"
                value={answer}
                name="answer"
                className="input" />
              <button onClick={handleSubmitAnswer} className="button">Enviar</button>
            </div>
          </>
        )}

        {showAnswer && (
          <div className='show-answer-hard'>
            <h2 className='desc'>Você Acertou! O caminho poderia ser o mais rentavel, ganhando {graphAns['custo mais rentavel']} e ficando com {40 + graphAns['custo mais rentavel']} na carteira, sendo:</h2>
            <h2 className='desc'>{graphAns['caminho mais rentavel'].join(" OU ")}</h2>
            <h2 className='desc'>Ou o caminho poderia ser o com menos gasto energetico, gastando apenas {graphAns['custo menor energia']} e ficando com {40 - graphAns['custo menor energia']} na carteira, sendo:</h2>
            <h2 className='desc'>{graphAns['caminho menor energia'].join(" -> ")}</h2>
          </div>
        )}

        {tryAgain && (
          <div className='try-again-hard'>
            <h2 className='desc'>Você Errou!</h2>
            <button onClick={handleSubmitTryAgain} className="button-try-again">Tentar Novamente</button>
          </div>
        )}
        <button className="button-return" onClick={() => navigate("/")}>Voltar</button>
      </div>
    </div>
  );
}

export default HardPage;
