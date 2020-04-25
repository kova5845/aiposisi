let initialState = {
  company: [
  ]
};

const companyReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SET-COMPANY': {
      return { ...state, company: action.company}
    }
    default:
      return state;

  }

}

export const setCompanyAC = (company) => ({type: 'SET-COMPANY', company})

export default companyReducer;
