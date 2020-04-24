let initialState = {
  engine: [
  ]
};

const engineReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SET-ENGINE': {
      return { ...state, engine: action.engine}
    }
    default:
      return state;

  }

}

export const setEngineAC = (engine) => ({type: 'SET-ENGINE', engine})

export default engineReducer;
