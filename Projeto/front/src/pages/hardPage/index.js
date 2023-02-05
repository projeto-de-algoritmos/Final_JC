import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom'
import MapImage from '../../assets/map.jpg';
import './index.css';

function HardPage() {
  const navigate = useNavigate()
  const [answer, setAnswer] = useState('')
  const [showAnswer, setShowAnswer] = useState(false)

  function handleChangeAnswer(value){
    setAnswer(value)
    console.log(answer)
  }

  function handleSubmitAnswer(){
    setShowAnswer(true)
  }

//   useEffect(() => {
//     fetch(`http://localhost:8000/`)
//     .then((response) => response.json())
//     .then((data) => {
//       setLoadingResult(true)
//       setRoute(data)
//       console.log(data)
//     });
//   });

  const data = {
    "Kingdom of Tentes": 20,
    "Gey": -15,
    "Principality of Montih": 15,
    "Republic of Nyirkad": 10,
    "Kingdom of Merland": 5,
    "Principality of Sicocoria": 3,
    "Kingdom of Guileria": -2,
    "Kingdom of Givrairatil": -4,
    "Grand Duchy of Lignia": 45,
    "Douchientian Theocracy": -37,
    "United Provinces of Rouertia": -1,
    "Bishopric of Silgulia": 35,
    "Lharanha": -2
  }

  return (
      <div className='hard-mode'>
        <div className='map'>
            <img className='map-image' src={MapImage}/>
        </div>
        <div className='info'>
            <h2 className='desc'>Valor inicial na carteira: 30</h2>
            <h2 className='desc'>Valor para entrar em cada reino:</h2>
            <div className='info-container'>
                <div className='left-info'>
                    <h2 className='desc'>Kingdom of Tentes: {data['Kingdom of Tentes']}</h2>
                    <h2 className='desc'>Gey: {data['Gey']}</h2>
                    <h2 className='desc'>Principality of Montih: {data['Principality of Montih']}</h2>
                    <h2 className='desc'>Republic of Nyirkad: {data['Republic of Nyirkad']}</h2>
                    <h2 className='desc'>Kingdom of Merland: {data['Kingdom of Merland']}</h2>
                    <h2 className='desc'>Principality of Sicocoria: {data['Principality of Sicocoria']}</h2>
                </div>
                <div className='right-info'>
                    <h2 className='desc'>Kingdom of Guileria: {data['Kingdom of Guileria']}</h2>
                    <h2 className='desc'>United Provinces of Rouertia: {data['United Provinces of Rouertia']}</h2>
                    <h2 className='desc'>Kingdom of Givrairatil: {data['Kingdom of Givrairatil']}</h2>
                    <h2 className='desc'>Douchientian Theocracy: {data['Douchientian Theocracy']}</h2>
                    <h2 className='desc'>Grand Duchy of Lignia: {data['Grand Duchy of Lignia']}</h2>
                    <h2 className='desc'>Lharanha: {data['Lharanha']}</h2>
                    <h2 className='desc'>Bishopric of Silgulia: {data['Bishopric of Silgulia']}</h2>
                </div>
            </div>
            {!showAnswer ? (
                <>
                    <h2 className='desc'>Indo de Kingdom of Tentes para Kingdom of Givrairatil, quanto de ouro você teria no final?</h2>
                    <div className='input-container'>
                        <h2 className='desc'>Valor na carteira: </h2>
                        <input onChange={(e)=> handleChangeAnswer(e.target.value)}
                            type="text"  
                            value={answer} 
                            name="answer" 
                            className="input"/>
                        <button onClick={handleSubmitAnswer} className="button">Enviar</button>
                    </div>
                </>
            ) : (
                <div></div>
            )}
            <button className="button-return" onClick={() => navigate("/")}>Voltar</button>
        </div>
      </div>
  );
}

export default HardPage;
