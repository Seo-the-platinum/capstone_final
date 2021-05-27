import './App.css';
import Home from './components/Home'
import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom'
import NavBar from './components/NavBar'
import Login from './components/Login'
import New_Actor from './components/New_Actor'
import New_Movie from './components/New_Movie'
import New_Star from './components/New_Star'
import Delete_Movie from './components/Delete_Movie'
import Delete_Actor from './components/Delete_Actor'
import Update_Actor from './components/Update_Actor'
import Update_Movie from './components/Update_Movie'

function App() {
  return (
    <Router>
      <div className="App">
        <Route path='/' component={ NavBar }/>
        <Route path='/home' component={ Home }/>
        <Route path='/login' component={ Login }/>
        <Route path='/add_actor' component={ New_Actor }/>
        <Route path='/add_movie' component={ New_Movie }/>
        <Route path='/add_star' component={ New_Star }/>
        <Route path='/delete_movie' component={ Delete_Movie }/>
        <Route path='/delete_actor' component={ Delete_Actor }/>
        <Route path='/update_actor' component={ Update_Actor }/>
        <Route path='/update_movie' component={ Update_Movie }/>
      </div>
    </Router>
  );
}

export default App;
