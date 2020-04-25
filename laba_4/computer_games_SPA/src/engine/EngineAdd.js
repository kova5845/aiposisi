import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


function EngineAdd(props) {

  let newEngineNameEl = React.createRef();
  let newEngineLanguageEl = React.createRef();
  let newEngineDateEl = React.createRef();
  let newEngineCompanyEl = React.createRef();

  let EnginesData = props.company.map(p => (
    <option id={p.id} selected="selected">{p.name}</option>
  ))


  let addEngine = () => {
    let newEngineName = newEngineNameEl.current.value;
    let newEngineLanguage = newEngineLanguageEl.current.value;
    let newEngineDate = newEngineDateEl.current.value;
    let newEngineCompany = newEngineCompanyEl.current.value;
    for (let i = 0; i < props.company.length; i++) {
      if (props.company[i].name == newEngineCompany) newEngineCompany = props.company[i].id
    }

    axios.post("http://localhost:5000/catalog/engine/", {
      "engine": {
        "name": newEngineName,
        "language": newEngineLanguage,
        "date": newEngineDate,
        "company": newEngineCompany
      }
    })
  }

  return (
    <div>
      <section className="games-base">
        <div className="container">
          <h2 className="games-base-title">Adding engine</h2>
          <NavLink to="/catalog/view/engine" className="games-base-button">Back</NavLink>
          <div className="wrapper">
            <div>
              <input ref={newEngineNameEl} type="text" name="engine_name" placeholder="Name (Required)" minLength={1} required />
              <input ref={newEngineLanguageEl} type="text" name="engine_language" placeholder="Language (Required)" minLength={1} required />
              <input ref={newEngineDateEl} type="date" defaultValue="2018-07-22" name="date_publishing" required />
              <div>
                <select ref={newEngineCompanyEl} className="selectors" name="engine">
                  {EnginesData}
                </select>
              </div>
              <input className="games-base-button" onClick={addEngine} type="submit" Value="Submit" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}


export default EngineAdd;