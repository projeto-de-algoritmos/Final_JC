import React from 'react';
import { Route, Routes } from "react-router-dom";
import MapImage from '../src/assets/map.jpg';
import HomePage from './pages/homePage';
import EasyPage from './pages/easyPage';
import HardPage from './pages/hardPage';
import InstructionPage from './pages/instructionPage';
import './App.css';

function App() {

  return (
    <div className='App' style={{ backgroundImage: `url(${MapImage})` }}>
      <div className='content-instructions'>
        <h1 className='title'>Map Game</h1>
        <Routes>
          <Route path="/" element={<HomePage/>} exact />
          <Route path="/easy" element={<EasyPage/>} />
          <Route path="/hard" element={<HardPage/>} />
          <Route path="/instructions" element={<InstructionPage/>} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
