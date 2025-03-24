import React from "react";
import Jogador from './Jogador';

function JogadorList(props){
    return(
        <div>
            <ul>
                {
                    props.jogadorList.map(
                        (jogador, indice) => {
                            return (< Jogador 
                                jogador={jogador} 
                                key={indice}
                                setJogadorId={props.setJogadorId}
                                setJogadorNome={props.setJogadorNome}
                                setJogadorIdade={props.setJogadorIdade}
                                setJogadorTime={props.setJogadorTime}
                                setTextoBotao={props.setTextoBotao}
                                />
                        )}
                    )
                }
            </ul>
        </div>
    )

}
export default JogadorList
