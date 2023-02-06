import React from 'react';
import { useNavigate } from 'react-router-dom'
import './index.css';

function InstructionPage() {
  const navigate = useNavigate()
  return (
      <div className='instruction'>
          <h2 className='instruction-text'>
            Num mundo de fantasia você é um viajante e quer ir de uma cidade inicial à outra. 
          </h2>
          <h2 className='instruction-text'>
            Você pode viajar a pé ou via teletransporte. Indo a pé você consome 
            sua energia (representadas com o valor positivo)
            e utilizando os teletransportes você passa por um processo de recuperação 
            e restaura sua energia (representadas com o valor negativo). 
            Esse processo depende de quão avançado é o teletransporte em cada cidade, 
            e também não são todas as cidade que tem.
          </h2>
          <h2 className='instruction-text'>
            Além disso cada cidade tem um pedágio para entrada (representadas com o valor positivo), 
            algumas estão incentivando o turismo
            e pagando para os viajantes visitarem (representadas com o valor negativo). 
          </h2>
          <h2 className='instruction-text'>
            No inicio desse jogo você tem uma carteira com 30 moedas e 30 de energia (modo fácil) 
            ou 40 moedas e 40 de energia (modo difícil).
            Tendo isso em mente você tem que calcular qual seria o caminho mais rentável ou o que gasta menos energia 
            e o valor final na sua carteira.
            Lembrando que valores negativos relativo a energia seriam somados (pois restauram) 
            e valores negativos relativos a moedas seriam subtraidos (pois foi gasto).
          </h2>
          <button className="button" onClick={() => navigate("/")}>Voltar</button>
      </div>
  );
}

export default InstructionPage;
