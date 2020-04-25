import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


function EngineEdit(props) {

  let index = Number(window.location.href.split("").splice(42, 10).join(""));
  let id = 0;
  let idCompany = 0;
  for (let i = 0; i < props.engine.length; i++) {
    if (props.engine[i].id == index) id = i
  }
  for (let i = 0; i < props.company.length; i++) {
    if (props.company[i].id == props.engine[id].company) idCompany = i
  }

  let EnginesData = props.company.map(p => (
    <option selected="selected">{p.name}</option>
  ))

  let newEngineNameEl = React.createRef();
  let newEngineLanguageEl = React.createRef();
  let newEngineDateEl = React.createRef();
  let newEngineCompanyEl = React.createRef();



  let editEngine = () => {
    let newEngineName = newEngineNameEl.current.value;
    let newEngineLanguage = newEngineLanguageEl.current.value;
    let newEngineDate = newEngineDateEl.current.value;
    let newEngineCompany = newEngineCompanyEl.current.value;
    for (let i = 0; i < props.company.length; i++) {
      if (props.company[i].name == newEngineCompany) newEngineCompany = props.company[i].id
    }

    axios.put(`http://localhost:5000/catalog/engine/${index}`, {
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
          <h2 className="games-base-title">Editing game</h2>
          <NavLink to="/catalog/view/engine" className="games-base-button">Back</NavLink>
          <div className="wrapper">
            <div>
              <input ref={newEngineNameEl} defaultValue={props.engine[id].name} type="text" name="contact-name" placeholder="Name (Required)" minLength={1} required />
              <input ref={newEngineLanguageEl} defaultValue={props.engine[id].language} type="text" name="contact-language" placeholder="Language (Required)" minLength={1} required />
              <input ref={newEngineDateEl} defaultValue={props.engine[id].date} type="date" name="subject" required />
              <div>
                <select ref={newEngineCompanyEl} defaultValue={props.company[idCompany].name} className="selectors" name="engine">
                  {EnginesData}
                </select>
              </div>
              <input className="games-base-button" onClick={editEngine} type="submit" Value="Submit" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}


export default EngineEdit;