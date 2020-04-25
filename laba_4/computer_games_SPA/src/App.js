import React from 'react';
import './css/style.css';
import './css/lato-font.css';
import AppContainer from './catalog/CatalogContainer'
import GameAddContainer from './game/GameAddContainer'
import GameEditContainer from './game/GameEditContainer'
import GameContainer from './game/GameContainer'
import GameShowContainer from './game/GameShowContainer'
import EngineAddContainer from './engine/EngineAddContainer'
import EngineEditContainer from './engine/EngineEditContainer'
import EngineContainer from './engine/EngineContainer'
import EngineShowContainer from './engine/EngineShowContainer'
import CompanyAddContainer from './company/CompanyAddContainer'
import CompanyEditContainer from './company/CompanyEditContainer'
import CompanyContainer from './company/CompanyContainer'
import CompanyShowContainer from './company/CompanyShowContainer'
import PlatformAddContainer from './platform/PlatformAddContainer'
import PlatformEditContainer from './platform/PlatformEditContainer'
import PlatformContainer from './platform/PlatformContainer'
import PlatformShowContainer from './platform/PlatformShowContainer'
import { Route, Switch} from "react-router-dom";


const App = (props) => (
  <div>
    <Switch>
      <Route exact path='/catalog' render={() => <AppContainer />} />

      <Route exact path='/catalog/view/game' render={() => <GameContainer />} />
      <Route path='/catalog/add/game' render={() => <GameAddContainer />} />
      <Route path='/catalog/edit/game/:id' render={() => <GameEditContainer />} />
      <Route path='/catalog/view/game/:id' render={() => <GameShowContainer />} />

      <Route exact path='/catalog/view/engine' render={() => <EngineContainer />} />
      <Route path='/catalog/add/engine' render={() => <EngineAddContainer />} />
      <Route path='/catalog/edit/engine/:id' render={() => <EngineEditContainer />} />
      <Route path='/catalog/view/engine/:id' render={() => <EngineShowContainer />} />

      <Route exact path='/catalog/view/company' render={() => <CompanyContainer />} />
      <Route path='/catalog/add/company' render={() => <CompanyAddContainer />} />
      <Route path='/catalog/edit/company/:id' render={() => <CompanyEditContainer />} />
      <Route path='/catalog/view/company/:id' render={() => <CompanyShowContainer />} />

      <Route exact path='/catalog/view/platform' render={() => <PlatformContainer />} />
      <Route path='/catalog/add/platform' render={() => <PlatformAddContainer />} />
      <Route path='/catalog/edit/platform/:id' render={() => <PlatformEditContainer />} />
      <Route path='/catalog/view/platform/:id' render={() => <PlatformShowContainer />} />
    </Switch>
  </div>
)


export default App;