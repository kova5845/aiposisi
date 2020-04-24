import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


function CompanyAdd(props) {

  let newCompanyNameEl = React.createRef()
  let newCompanyPlaceEl = React.createRef()
  let newCompanyDateEl = React.createRef()


  let addCompany = () => {
    let newCompanyName = newCompanyNameEl.current.value;
    let newCompanyPlace = newCompanyPlaceEl.current.value;
    let newCompanyDate = newCompanyDateEl.current.value;

    axios.post("http://localhost:5000/catalog/company/", {
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
          <h2 className="games-base-title">Adding company</h2>
          <NavLink to="/catalog/view/company" className="games-base-button">Back</NavLink>
          <div className="wrapper">
            <div>
              <input ref={newCompanyNameEl} type="text" name="company_name" placeholder="Name (Required)" minLength={1} required />
              <input ref={newCompanyPlaceEl} type="text" name="company_place" placeholder="Place (Required)" minLength={1} required />
              <input ref={newCompanyDateEl} type="date" defaultValue="2018-07-22" name="date_publishing" required />
              <input className="games-base-button" onClick={addCompany} type="submit" Value="Submit" />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}


export default CompanyAdd;