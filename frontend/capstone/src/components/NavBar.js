import React from 'react'
import {
  Link,
} from 'react-router-dom'
import Login from './Login'
import Logout from './Logout'
import { useAuth0 } from '@auth0/auth0-react'

const NavBar = ()=> {
  const { isAuthenticated, isLoading } = useAuth0()

  if (isLoading) {
    return <div> Loading...</div>
  }

  return (
    <div>
      <ul>
        <li>
          <Link to='/home'> Home</Link>
        </li>
        <li>
          <Link to='/add_movie'> Add Movie</Link>
        </li>
        <li>
          <Link to='/add_actor'> Add Actor</Link>
        </li>
        <li>
          <Link to='/add_star'> Add Star</Link>
        </li>
      </ul>
      { !isAuthenticated ? <Login/> : <Logout/>
      }
    </div>
  )
}

export default NavBar
