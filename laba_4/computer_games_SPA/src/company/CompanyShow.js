import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";


function CompanyShow(props) {

  let index = Number(window.location.href.split("").splice(43, 10).join(""))
  let id = 0
  for (let i = 0; i < props.company.length; i++) {
    if (props.company[i].id == index) id = i
  }

  return (
    <div>
      <section className="games-base">
        <div className="container">
          <h2 className="games-base-title">Show company</h2>
          <NavLink to="/catalog/view/company" className="games-base-button">Back</NavLink>
          <div className="wrapper">
            <dl>
              <dt><h3 className="games-base-names">Name:</h3></dt>
              <dd><p className="games-base-description">{props.company[id].name}</p></dd>
              <dt><h3 className="games-base-names">Place:<p /></h3></dt>
              <dd><p className="games-base-description">{props.company[id].place}</p></dd>
              <dt><h3 className="games-base-names">Date:<p /></h3></dt>
              <dd><p className="games-base-description">{props.company[id].date}</p></dd>
            </dl>
          </div>
        </div>
      </section>
    </div>
  );
}


export default CompanyShow;