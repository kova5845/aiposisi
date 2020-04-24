import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


function PlatformAdd(props) {

  let newPlatformNameEl = React.createRef();
  let newPlatformDateEl = React.createRef();
  let newPlatformCompanyEl = React.createRef();

  let PlatformsData = props.company.map(p => (
    <option id={p.id} selected="selected">{p.name}</option>
  ))


  let addPlatform = () => {
    let newPlatformName = newPlatformNameEl.current.value;
    let newPlatformDate = newPlatformDateEl.current.value;
    let newPlatformCompany = newPlatformCompanyEl.current.value;
    for (let i = 0; i < props.company.length; i++) {
      if (props.company[i].name == newPlatformCompany) newPlatformCompany = props.company[i].id
    }

    axios.post("http://localhost:5000/catalog/platform/", {
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
          <h2 className="games-base-title">Adding platform</h2>
          <NavLink to="/catalog/view/platform" className="games-base-button">Back</NavLink>
          <div className="wrapper">
            <div>
              <input ref={newPlatformNameEl} type="text" name="platform_name" placeholder="Name (Required)" minLength={1} required />
              <input ref={newPlatformDateEl} type="date" defaultValue="2018-07-22" name="date_publishing" required />
              <div>
                <select ref={newPlatformCompanyEl} className="selectors" name="platform">
                  {PlatformsData}
                </select>
              </div>
              <input className="games-base-button" onClick={addPlatform} type="submit" Value="Submit" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}


export default PlatformAdd;