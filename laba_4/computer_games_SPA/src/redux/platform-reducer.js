let initialState = {
  platform: [
  ]
};

const platformReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SET-PLATFORM': {
      return { ...state, platform: action.platform}
    }
    default:
      return state;

  }

}

export const setPlatformAC = (platform) => ({type: 'SET-PLATFORM', platform})

export default platformReducer;
