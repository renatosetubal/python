import { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'

function App() {
  const [jogadorList, setJogadorList] = useState([{}]);
  const [jogadorNome, setJogadorNome] = useState('');
  const [jogadorIdade, setJogadorIdade] = useState('');
  const [jogadorTime, setJogadorTime] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/jogadores')
      .then(resposta => {
        console.log(resposta.data)
      }).catch(
        (erro) => { console.log(erro) }
      )
  })

  return (
    <div className="container">
      <div className='mt-3 justify-content-center align-items-center mx-auto' style={{ "width": "60vw", "backgroundColor": "#ffffff" }}>
        <h2 className='text-center text-white bg-success card mb-1'>Gerenciamento de Jogadores</h2>
        <h6 className='card text-center text-white bg-success mb-2 pb-2'>Informações de Jogadores</h6>
        <div className='card-body text-center'>
          <h5 className='card text-center text-white bg-dark pb-1'>Cadastro do Jogador</h5>
          <span className='card-text'>
            <input className='mb-2 form-control' placeholder='Informe o nome'></input>
            <input className='mb-2 form-control' placeholder='Informe a idade'></input>
            <input className='mb-2 form-control' placeholder='Informe o time'></input>
            <button className='btn btn-outline-success mb-4'>Cadastrar</button>
          </span>
          <h5 className='card text-center text-white bg-dark pb-1 mb-4'>Lista de Jogadores</h5>
        </div>
        <h6 className='card text-center text-light bg-success py-1'>&copy; Iwit - 2025</h6>
      </div>
    </div>
  );
}

export default App;
