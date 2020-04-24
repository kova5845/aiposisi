import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


function PlatformEdit(props) {

  let index = Number(window.location.href.split("").splice(44, 10).join(""));
  let id = 0;
  let idCompany = 0;
  for (let i = 0; i < props.platform.length; i++) {
    if (props.platform[i].id == index) id = i
  }
  for (let i = 0; i < props.company.length; i++) {
    if (props.company[i].id == props.platform[id].company) idCompany = i
  }

  let PlatformsData = props.company.map(p => (
    <option selected="selected">{p.name}</option>
  ))

  let newPlatformNameEl = React.createRef();
  let newPlatformDateEl = React.createRef();
  let newPlatformCompanyEl = React.createRef();



  let editPlatform = () => {
    let newPlatformName = newPlatformNameEl.current.value;
    let newPlatformDate = newPlatformDateEl.current.value;
    let newPlatformCompany = newPlatformCompanyEl.current.value;
    for (let i = 0; i < props.company.length; i++) {
      if (props.company[i].name == newPlatformCompany) newPlatformCompany = props.company[i].id
    }

    axios.put(`http://localhost:5000/catalog/platform/${index}`, {
      "platform": {
        "name": newPlatformName,
        "date": newPlatformDate,
        "company": newPlatformCompany
      }
    })
  }

  return (
    <div>
      <section className="games-base">
        <div className="container">
          <h2 className="games-base-title">Editing game</h2>
          <NavLink to="/catalog/view/platform" className="games-base-button">Back</NavLink>
          <div className="wrapper">
            <div>
              <input ref={newPlatformNameEl} defaultValue={props.platform[id].name} type="text" name="contact-name" placeholder="Name (Required)" minLength={1} required />
              <input ref={newPlatformDateEl} defaultValue={props.platform[id].date} type="date" name="subject" required />
              <div>
                <select ref={newPlatformCompanyEl} defaultValue={props.company[idCompany].name} className="selectors" name="platform">
                  {PlatformsData}
                </select>
              </div>
              <input className="games-base-button" onClick={editPlatform} type="submit" Value="Submit" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}


export default PlatformEdit;