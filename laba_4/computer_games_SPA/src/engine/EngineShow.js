import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";


function EngineShow(props) {

  let index = Number(window.location.href.split("").splice(42, 10).join(""));
  let id = 0;
  let idCompany = 0;
  for (let i = 0; i < props.engine.length; i++) {
    if (props.engine[i].id == index) id = i
  }
  for (let i = 0; i < props.company.length; i++) {
    if (props.company[i].id == props.engine[id].company) idCompany = i
  }

  return (
    <div>
      <section className="games-base">
        <div className="container">
          <h2 className="games-base-title">Show company</h2>
          <NavLink to="/catalog/view/engine" className="games-base-button">Back</NavLink>
          <div className="wrapper">
            <dl>
              <dt><h3 className="games-base-names">Name:</h3></dt>
              <dd><p className="games-base-description">{props.engine[id].name}</p></dd>
              <dt><h3 className="games-base-names">Language:</h3></dt>
              <dd><p className="games-base-description">{props.engine[id].language}</p></dd>
              <dt><h3 className="games-base-names">Date:<p /></h3></dt>
              <dd><p className="games-base-description">{props.engine[id].date}</p></dd>
              <dt><h3 className="games-base-names">Company:<p /></h3></dt>
              <dd><p className="games-base-description">{props.company[idCompany].name}</p></dd>
            </dl>
          </div>
        </div>
      </section>
    </div>
  );
}


export default EngineShow;