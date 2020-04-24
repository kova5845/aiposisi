import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


class PlatformList extends React.Component {

  componentDidMount() {
    axios.get("http://localhost:5000/catalog/company/").then(response => {
      this.props.setCompany(response.data.company)
    })
    axios.get("http://localhost:5000/catalog/platform/").then(response => {
      this.props.setPlatform(response.data.platform)
    })
  }

  deletePlatform = (x) => {
    let oldPlatformIndex = x.target.id;
    axios.delete(`http://localhost:5000/catalog/platform/${oldPlatformIndex}`).then(() => {
      this.componentDidMount()
    })
  }

  render() {
    return (
      <div>
        <section className="games-base">
          <div className="container">
            <h2 className="games-base-title">Platform List</h2>
            <NavLink to="/catalog/add/platform" className="games-base-button">Add</NavLink>
            <NavLink to="/catalog" className="games-base-button">Back</NavLink>
            <div className="wrapper">
              <div>
                {this.props.platform.map(p => (
                  <div className="buttons">
                    <h3 className="games-base-names">
                      <NavLink to={`/catalog/view/platform/${p.id}`}>{p.name}</NavLink>
                      <NavLink to={`/catalog/edit/platform/${p.id}`} className="btn">Edit</NavLink>
                      <button id={p.id} onClick={this.deletePlatform} className="btn">Delete</button>
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


export default PlatformList;