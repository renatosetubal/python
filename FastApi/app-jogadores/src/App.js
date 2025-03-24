import { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'
import JogadorList from './components/JogadorList';

function App() {
  const [jogadorList, setJogadorList] = useState([{}]);
  const [jogadorNome, setJogadorNome] = useState('');
  const [jogadorIdade, setJogadorIdade] = useState('');
  const [jogadorTime, setJogadorTime] = useState('');
  const [jogadorId, setJogadorId] = useState('');
  const [textoBotao, setTextoBotao] = useState('Cadastrar');

  useEffect(() => {
    axios.get('http://localhost:8000/jogadores')
      .then(resposta => {
        console.log(resposta.data)
        setJogadorList(resposta.data)
      }).catch(
        (error) => { console.log(error) }
      )
  })

  const atualizaJogador = (jogador) => {
    axios.put(`http://127.0.0.1:8000/jogadores/${jogadorId}`, jogador)
      .then(resposta => {
        alert("Jogador utilizado com sucesso!")
      })
      .catch((error) => {
        console.log(error);
      })
  }

  const adicionaJogador = (jogador) => {
    axios.post('http://localhost:8000/jogadores', jogador)
      .then(resposta => {
        // limparCampos();
        alert("Jogador cadastrado com sucesso!");
      })
      .catch((error) => {
        console.log(error);
      })
  }



  // const limparCampos = () => {
  //   setJogadorNome('');
  //   setJogadorIdade('');
  //   setJogadorTime('');
  // };
  const adicionaAtualizaJogador = () => {
    const jogador = {
      'jogador_nome': jogadorNome,
      'jogador_idade': jogadorIdade,
      'jogador_time': jogadorTime
    }
    if(jogadorId !== ''){
      atualizaJogador(jogador);
    }else{
      adicionaJogador(jogador);
    }

  }

  return (
    <div className="container">
      <div className='mt-3 justify-content-center align-items-center mx-auto' style={{ "width": "60vw", "backgroundColor": "#ffffff" }}>
        <h2 className='text-center text-white bg-success card mb-1'>Gerenciamento de Jogadores</h2>
        <h6 className='card text-center text-white bg-success mb-2 pb-2'>Informações de Jogadores</h6>
        <div className='card-body text-center'>
          <h5 className='card text-center text-white bg-dark pb-1'>Cadastro do Jogador</h5>
          <span className='card-text'>
            <input value={jogadorNome} onChange={evento => setJogadorNome(evento.target.value)} className='mb-2 form-control' placeholder='Informe o nome'></input>
            <input value={jogadorIdade} onChange={evento => setJogadorIdade(evento.target.value)} className='mb-2 form-control' placeholder='Informe a idade'></input>
            <input value={jogadorTime} onChange={evento => setJogadorTime(evento.target.value)} className='mb-2 form-control' placeholder='Informe o time'></input>
            <button onClick={adicionaAtualizaJogador} className='btn btn-outline-success mb-4'>
              {textoBotao}
            </button>
          </span>
        </div>
        <div>
          <h5 className='card text-center text-white bg-dark pb-1 mb-4'>Lista de Jogadores</h5>
        </div>
        <div className='text-center'>
          <JogadorList
            jogadorList={jogadorList}
            setJogadorId={setJogadorId}
            setJogadorNome={setJogadorNome}
            setJogadorIdade={setJogadorIdade}
            setJogadorTime={setJogadorTime}
            setTextoBotao={setTextoBotao}

          />
        </div>

        <h6 className='card text-center text-light bg-success py-1'>&copy; Iwit - 2025</h6>
      </div>
    </div>
  );
}

export default App;
