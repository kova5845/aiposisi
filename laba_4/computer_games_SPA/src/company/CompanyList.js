import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


class CompanyList extends React.Component {

  componentDidMount() {
    axios.get("http://localhost:5000/catalog/company/").then(response => {
      this.props.setCompany(response.data.company)
    })
  }

  deleteCompany = (x) => {
    let oldCompanyIndex = x.target.id;
    axios.delete(`http://localhost:5000/catalog/company/${oldCompanyIndex}`).then(() => {
      this.componentDidMount()
    })
  }

  render() {
    return (
      <div>
        <section className="games-base">
          <div className="container">
            <h2 className="games-base-title">Company List</h2>
            <NavLink to="/catalog/add/company" className="games-base-button">Add</NavLink>
            <NavLink to="/catalog" className="games-base-button">Back</NavLink>
            <div className="wrapper">
              <div>
                {this.props.company.map(p => (
                  <div className="buttons">
                    <h3 className="games-base-names">
                      <NavLink to={`/catalog/view/company/${p.id}`}>{p.name}</NavLink>
                      <NavLink to={`/catalog/edit/company/${p.id}`} className="btn">Edit</NavLink>
                      <button id={p.id} onClick={this.deleteCompany} className="btn">Delete</button>
                    </h3>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>
      </div>
    )
  }
}


export default CompanyList;