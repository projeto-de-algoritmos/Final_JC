import React from 'react';
import { useNavigate } from 'react-router-dom'
import './index.css';

function HomePage() {
  const navigate = useNavigate()
  return (
    <div className='home-page'>
        <div className='button-customize'>
            <button className="button" onClick={() => navigate("/easy")}>Fácil</button>
            <button className="button" onClick={() => navigate("/hard")}>Difícil</button>
            <button className="button" onClick={() => navigate("/instructions")}>Instruções</button>
        </div>
    </div>
  );
}

export default HomePage;
