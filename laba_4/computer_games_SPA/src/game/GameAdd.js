import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


function GameAdd(props) {


  let newGameNameEl = React.createRef()
  let newGameGenreEl = React.createRef()
  let newGameSettingEl = React.createRef()
  let newGameDateEl = React.createRef()
  let newGameCompanyEl = React.createRef()
  let newGameEngineEl = React.createRef()
  let newGamePlatformEl = React.createRef()


  let GamesData = props.company.map(p => (
    <option id={p.id} selected="selected">{p.name}</option>
  ))

  let GamesData2 = props.engine.map(p => (
    <option id={p.id} selected="selected">{p.name}</option>
  ))

  let GamesData3 = props.platform.map(p => (
    <option id={p.id} selected="selected">{p.name}</option>
  ))

  let addGame = () => {
    let newGamePlatform = []

    for (let i = 0; i < newGamePlatformEl.current.selectedOptions.length; i++) {
      newGamePlatform.push(newGamePlatformEl.current.selectedOptions[i].value)
    }


    let newGameName = newGameNameEl.current.value;
    let newGameGenre = newGameGenreEl.current.value;
    let newGameSetting = newGameSettingEl.current.value;
    let newGameDate = newGameDateEl.current.value;
    let newGameCompany = newGameCompanyEl.current.value;
    let newGameEngine = newGameEngineEl.current.value;

    for (let i = 0; i < props.company.length; i++) {
      if (props.company[i].name == newGameCompany) newGameCompany = props.company[i].id
    }

    for (let i = 0; i < props.engine.length; i++) {
      if (props.engine[i].name == newGameEngine) newGameEngine = props.engine[i].id
    }

    for (let i = 0; i < props.platform.length; i++) {
      if (props.platform[i].name == newGamePlatform[i]) newGamePlatform[i] = props.platform[i].id
    }

    axios.post("http://localhost:5000/catalog/game/", {
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
          <h2 className="games-base-title">Adding game</h2>
          <NavLink to="/catalog/view/game" className="games-base-button">Back</NavLink>
          <div className="wrapper">
            <div>
              <input ref={newGameNameEl} type="text" name="game_name" placeholder="Name (Required)" minLength={1} required />
              <input ref={newGameGenreEl} type="text" name="game_genre" placeholder="Genre (Required)" minLength={1} required />
              <input ref={newGameSettingEl} type="text" name="game_setting" placeholder="Setting (Required)" minLength={1} required />
              <input ref={newGameDateEl} type="date" defaultValue="2018-07-22" defaultMin="1900-01-01" defaultMax="2020-12-31" name="date_publishing" required />
              <div>
                <select ref={newGameCompanyEl} className="selectors" name="company">
                  {GamesData}
                </select>
              </div>
              <div>
                <select ref={newGameEngineEl} className="selectors" name="engine">
                  {GamesData2}
                </select>
              </div>
              <div>
                <select ref={newGamePlatformEl} className="selectors" name="platform" multiple>
                  {GamesData3}
                </select>
              </div>
              <input className="games-base-button" onClick={addGame} type="submit" Value="Submit" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}



export default GameAdd;