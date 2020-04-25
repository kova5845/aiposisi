import GameList from "./GameList"
import {connect} from "react-redux"
import {setGameAC} from "../redux/game-reducer"
import {setEngineAC} from "../redux/engine-reducer"
import {setCompanyAC} from "../redux/company-reducer"
import {setPlatformAC} from "../redux/platform-reducer"

let mapStateToProps = (state) => {
  return {
    game: state.gamePage.game,
    engine: state.enginePage.engine,
    company: state.companyPage.company,
    platform: state.platformPage.platform
  }
}

let mapDispatchToProps = (dispatch) => {
  return {
    setGame: (game) => {
      dispatch(setGameAC(game))
    },

    setEngine: (engine) => {
      dispatch(setEngineAC(engine))
    },

    setCompany: (company) => {
      dispatch(setCompanyAC(company))
    },

    setPlatform: (platform) => {
      dispatch(setPlatformAC(platform))
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(GameList);