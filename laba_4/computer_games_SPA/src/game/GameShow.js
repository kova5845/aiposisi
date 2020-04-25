import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";


function GameShow(props) {

  let index = Number(window.location.href.split("").splice(40, 10).join(""));
  let id = 0;
  let idCompany = 0;
  let idEngine = 0;
  let idPlatform = [];
  for (let i = 0; i < props.game.length; i++) {
    if (props.game[i].id == index) id = i
  }

  for (let i = 0; i < props.company.length; i++) {
    if (props.company[i].id == props.game[id].company) idCompany = i
  }

  for (let i = 0; i < props.engine.length; i++) {
    if (props.engine[i].id == props.game[id].engine) idEngine = i
  }

  for (let i = 0; i < props.platform.length; i++) {
    for (let j = 0; j < props.game[id].platform.length; j++) {
      if (props.platform[i].id == props.game[id].platform[j]) idPlatform.push(props.platform[i].name)
    }
  }

  let platformsList = idPlatform.map(p => (
    <p className="games-base-description">{p}</p>
  ))

  return (
    <div>
      <section className="games-base">
        <div className="container">
          <h2 className="games-base-title">Show game</h2>
          <NavLink to="/catalog/view/game" className="games-base-button">Back</NavLink>
          <div className="wrapper">
              <dl>
                <dt><h3 className="games-base-names">Name:</h3></dt>
                <dd><p className="games-base-description">{props.game[id].name}</p></dd>
                <dt><h3 className="games-base-names">Genre:<p /></h3></dt>
                <dd><p className="games-base-description">{props.game[id].genre}</p></dd>
                <dt><h3 className="games-base-names">Setting:<p /></h3></dt>
                <dd><p className="games-base-description">{props.game[id].setting}</p></dd>
                <dt><h3 className="games-base-names">Date:<p /></h3></dt>
                <dd><p className="games-base-description">{props.game[id].date}</p></dd>
                <dt><h3 className="games-base-names">Company:<p /></h3></dt>
                <dd><p className="games-base-description">{props.company[idCompany].name}</p></dd>
                <dt><h3 className="games-base-names">Engine:<p /></h3></dt>
                <dd><p className="games-base-description">{props.engine[idEngine].name}</p></dd>
                <dt><h3 className="games-base-names">Platforms:<p /></h3></dt>
                <dd>{platformsList}</dd>
              </dl>
          </div>
        </div>
      </section>
    </div>
  );
}


export default GameShow;