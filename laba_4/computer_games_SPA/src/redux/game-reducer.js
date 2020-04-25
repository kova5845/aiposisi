import * as axios from 'axios';

let initialState = {
  game: [
  ]
};

const gameReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SET-GAME': {
      return { ...state, game: action.game}
    }
    default:
      return state;
  }
}



export const setGameAC = (game) => ({type: 'SET-GAME', game})

export default gameReducer;