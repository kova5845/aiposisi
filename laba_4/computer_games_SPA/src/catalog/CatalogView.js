import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';


class CatalogView extends React.Component {

  componentDidMount() {
    axios.get("http://localhost:5000/catalog/game/").then(response => {
      this.props.setGame(response.data.game)
    });
    axios.get("http://localhost:5000/catalog/engine/").then(response => {
      this.props.setEngine(response.data.engine)
    })
    axios.get("http://localhost:5000/catalog/company/").then(response => {
      this.props.setCompany(response.data.company)
    })
    axios.get("http://localhost:5000/catalog/platform/").then(response => {
      this.props.setPlatform(response.data.platform)
    })
  }

  render() {
    return (
      <div>
        <section className="games-base">
          <div className="container">
            <div className="center">
              <h2 className="games-base-title">Game Base</h2>
              <div>
                <NavLink to="/catalog/view/game" className="games-main-base-button">Game</NavLink>
                <NavLink to="/catalog/view/engine" className="games-main-base-button">Engine</NavLink>
                <NavLink to="/catalog/view/company" className="games-main-base-button">Company</NavLink>
                <NavLink to="/catalog/view/platform" className="games-main-base-button">Platform</NavLink>
              </div>
            </div>
          </div>
        </section>
      </div>
    )
  }
}

export default CatalogView;