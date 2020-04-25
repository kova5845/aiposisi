import React from 'react';
import '../css/style.css';
import '../css/lato-font.css';
import { NavLink } from "react-router-dom";
import * as axios from 'axios';

class GameList extends React.Component {

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

  deleteGame = (x) => {
    let oldGameIndex = x.target.id;
    axios.delete(`http://localhost:5000/catalog/game/${oldGameIndex}`).then( () => {
      this.componentDidMount()
    })
  }
  render() {
    return (
      <div>
        <section className="games-base">
          <div className="container">
            <h2 className="games-base-title">Game List</h2>
            <NavLink to="/catalog/add/game" className="games-base-button">Add</NavLink>
            <NavLink to="/catalog" className="games-base-button">Back</NavLink>
            <div className="wrapper">
              <div>
                {this.props.game.map(p => (
                  <div className="buttons">
                    <h3 className="games-base-names">
                      <NavLink to={`/catalog/view/game/${p.id}`}>{p.name}</NavLink>
                      <NavLink to={`/catalog/edit/game/${p.id}`} className="btn">Edit</NavLink>
                      <button to="/catalog/view/game/" id={p.id} onClick={this.deleteGame} className="btn">Delete</button>
                    </h3>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>
      </div>
    );
  }
}

export default GameList;