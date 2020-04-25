import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


function GameEdit(props) {

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

  let GamesData = props.company.map(p => (
    <option id={p.id} selected="selected">{p.name}</option>
  ))

  let GamesData2 = props.engine.map(p => (
    <option id={p.id} selected="selected">{p.name}</option>
  ))

  let GamesData3 = props.platform.map(p => (
    <option id={p.id} selected="selected">{p.name}</option>
  ))

  let newGameNameEl = React.createRef()
  let newGameGenreEl = React.createRef()
  let newGameSettingEl = React.createRef()
  let newGameDateEl = React.createRef()
  let newGameCompanyEl = React.createRef()
  let newGameEngineEl = React.createRef()
  let newGamePlatformEl = React.createRef()


  let editGame = () => {

    let newGamePlatformNames = []

    for (let i = 0; i < newGamePlatformEl.current.selectedOptions.length; i++) {
      newGamePlatformNames.push(newGamePlatformEl.current.selectedOptions[i].value)
    }

    let newGameName = newGameNameEl.current.value;
    let newGameGenre = newGameGenreEl.current.value;
    let newGameSetting = newGameSettingEl.current.value;
    let newGameDate = newGameDateEl.current.value;
    let newGameCompany = newGameCompanyEl.current.value;
    let newGameEngine = newGameEngineEl.current.value;
    let newGamePlatform = [];

    for (let i = 0; i < props.company.length; i++) {
      if (props.company[i].name == newGameCompany) newGameCompany = props.company[i].id
    }

    for (let i = 0; i < props.engine.length; i++) {
      if (props.engine[i].name == newGameEngine) newGameEngine = props.engine[i].id
    }

    for (let i = 0; i < newGamePlatformNames.length; i++) {
      for (let j = 0; j < props.platform.length; j++) {
        if (newGamePlatformNames[i] == props.platform[j].name) newGamePlatform.push(props.platform[j].id)
      }
    }

    axios.put(`http://localhost:5000/catalog/game/${index}`, {
      "game": {
        "name": newGameName,
        "genre": newGameGenre,
        "setting": newGameSetting,
        "date": newGameDate,
        "company": newGameCompany,
        "engine": newGameEngine,
        "platform": newGamePlatform
      }
    })
  }

  return (
    <div>
      <section className="games-base">
        <div className="container">
          <h2 className="games-base-title">Editing game</h2>
          <NavLink to="/catalog/view/game" className="games-base-button">Back</NavLink>
          <div className="wrapper">
            <div>
              <input ref={newGameNameEl} defaultValue={props.game[id].name} type="text" name="contact-name" placeholder="Name (Required)" minLength={1} required />
              <input ref={newGameGenreEl} defaultValue={props.game[id].genre} type="text" name="contact-email" placeholder="Genre (Required)" minLength={1} required />
              <input ref={newGameSettingEl} defaultValue={props.game[id].setting} type="text" name="setting" placeholder="Setting (Required)" minLength={1} required />
              <input ref={newGameDateEl} defaultValue={props.game[id].date} type="date" name="subject" required />
              <div>
                <select ref={newGameCompanyEl} defaultValue={props.company[idCompany].name} className="selectors" name="engine">
                  {GamesData}
                </select>
              </div>
              <div>
                <select ref={newGameEngineEl} defaultValue={props.engine[idEngine].name} className="selectors" name="engine">
                  {GamesData2}
                </select>
              </div>
              <div>
                <select ref={newGamePlatformEl} defaultValue={idPlatform} className="selectors" name="platform" multiple>
                  {GamesData3}
                </select>
              </div>
              <input className="games-base-button" onClick={editGame} type="submit" Value="Submit" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}


export default GameEdit;