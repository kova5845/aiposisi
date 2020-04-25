import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


function CompanyEdit(props) {

  let index = Number(window.location.href.split("").splice(43, 3).join(""))
  let id = 0
  for (let i = 0; i < props.company.length; i++) {
    if (props.company[i].id == index) id = i
  }

  let newCompanyNameEl = React.createRef()
  let newCompanyPlaceEl = React.createRef()
  let newCompanyDateEl = React.createRef()


  let editCompany = () => {
    let newCompanyName = newCompanyNameEl.current.value;
    let newCompanyPlace = newCompanyPlaceEl.current.value;
    let newCompanyDate = newCompanyDateEl.current.value;

    axios.put(`http://localhost:5000/catalog/company/${index}`, {
      "company": {
        "name": newCompanyName,
        "place": newCompanyPlace,
        "date": newCompanyDate
      }
    })
  }

  return (
    <div>
      <section className="games-base">
        <div className="container">
          <h2 className="games-base-title">Editing game</h2>
          <NavLink to="/catalog/view/company" className="games-base-button">Back</NavLink>
          <div className="wrapper">
            <div>
              <input ref={newCompanyNameEl} defaultValue={props.company[id].name} type="text" name="contact-name" placeholder="Name (Required)" minLength={1} required />
              <input ref={newCompanyPlaceEl} defaultValue={props.company[id].place} type="text" name="contact-email" placeholder="Place (Required)" minLength={1} required />
              <input ref={newCompanyDateEl} defaultValue={props.company[id].date} type="date" name="subject" required />
              <input className="games-base-button" onClick={editCompany} type="submit" Value="Submit" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}


export default CompanyEdit;