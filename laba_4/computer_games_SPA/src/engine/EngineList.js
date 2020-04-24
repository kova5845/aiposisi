import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


class EngineList extends React.Component {

  componentDidMount() {
    axios.get("http://localhost:5000/catalog/engine/").then(response => {
      this.props.setEngine(response.data.engine)
    })
    axios.get("http://localhost:5000/catalog/company/").then(response => {
      this.props.setCompany(response.data.company)
    })
  }

  deleteEngine = (x) => {
    let oldEngineIndex = x.target.id;
    axios.delete(`http://localhost:5000/catalog/engine/${oldEngineIndex}`).then(() => {
      this.componentDidMount()
    })
  }

  render() {
    return (
      <div>
        <section className="games-base">
          <div className="container">
            <h2 className="games-base-title">Engine List</h2>
            <NavLink to="/catalog/add/engine" className="games-base-button">Add</NavLink>
            <NavLink to="/catalog" className="games-base-button">Back</NavLink>
            <div className="wrapper">
              <div>
                {this.props.engine.map(p => (
                  <div className="buttons">
                    <h3 className="games-base-names">
                      <NavLink to={`/catalog/view/engine/${p.id}`}>{p.name}</NavLink>
                      <NavLink to={`/catalog/edit/engine/${p.id}`} className="btn">Edit</NavLink>
                      <button id={p.id} onClick={this.deleteEngine} className="btn">Delete</button>
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


export default EngineList;