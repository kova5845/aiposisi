import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";


function PlatformShow(props) {

  let index = Number(window.location.href.split("").splice(44, 10).join(""));
  let id = 0;
  let idCompany = 0;
  for (let i = 0; i < props.platform.length; i++) {
    if (props.platform[i].id == index) id = i
  }
  for (let i = 0; i < props.company.length; i++) {
    if (props.company[i].id == props.platform[id].company) idCompany = i
  }

  return (
    <div>
      <section className="games-base">
        <div className="container">
          <h2 className="games-base-title">Show company</h2>
          <NavLink to="/catalog/view/platform" className="games-base-button">Back</NavLink>
          <div className="wrapper">
            <dl>
              <dt><h3 className="games-base-names">Name:</h3></dt>
              <dd><p className="games-base-description">{props.platform[id].name}</p></dd>
              <dt><h3 className="games-base-names">Date:<p /></h3></dt>
              <dd><p className="games-base-description">{props.platform[id].date}</p></dd>
              <dt><h3 className="games-base-names">Company:<p /></h3></dt>
              <dd><p className="games-base-description">{props.company[idCompany].name}</p></dd>
            </dl>
          </div>
        </div>
      </section>
    </div>
  );
}


export default PlatformShow;