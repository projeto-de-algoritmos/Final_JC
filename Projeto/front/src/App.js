import React from 'react';
import { Route, Routes } from "react-router-dom";
import MapImage from '../src/assets/Gises 2023-02-05-14-59.png';
import HomePage from './pages/homePage';
import './App.css';

function App() {

  return (
    <div className='App' style={{ backgroundImage: `url(${MapImage})` }}>
      <div className='content-instructions'>
        <h1 className='title'>Map Game</h1>
        <Routes>
          <Route path="/" element={<HomePage/>} exact />
        </Routes>
      </div>
    </div>
  );
}

export default App;
