import React from "react";
import axios from "axios";

function Jogador(props){
    const excluiJogador = (jogadorId) => {
        axios.delete(`http://localhost:8000/jogadores/${jogadorId}`)
        .then(
            resposta=> {
                alert("Jogador removido com sucesso!" + resposta.data)
            }
        )
    }
    const editarJogador = (jogador) => {
        props.setJogadorId(jogador.id);
        props.setJogadorNome(jogador.nome);
        props.setJogadorIdade(jogador.idade);
        props.setJogadorTime(jogador.time);
        props.setTextoBotao("Atualizar")


    }
    return (
        <div>
            <p>
                <span className="fw-bold">
                    {props.jogador.nome} - {props.jogador.idade} - {props.jogador.time}
                </span>
                <button 
                    onClick={() => editarJogador(props.jogador)}
                    className="btn btn-info">
                <span className="badge rouded-pill bg-info">Editar</span>
                </button>
                <button className="btn btn-danger">
                    <span onClick={() => excluiJogador(props.jogador.id)} className="badge rouded-pill bg-danger">X</span>
                </button>
            </p>
        </div>
    )
}

export default Jogador;