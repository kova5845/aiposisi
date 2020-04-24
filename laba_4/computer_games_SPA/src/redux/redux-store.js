import { createStore, combineReducers } from "redux";
import gameReducer from "./game-reducer"
import engineReducer from "./engine-reducer"
import companyReducer from "./company-reducer"
import platformReducer from "./platform-reducer"



let reducers = combineReducers({
  gamePage: gameReducer,
  enginePage: engineReducer,
  companyPage: companyReducer,
  platformPage: platformReducer
});

let store = createStore(reducers);

window.store = store

export default store;