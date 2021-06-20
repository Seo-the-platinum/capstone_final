import React from 'react'
import {
  Link,
} from 'react-router-dom'
import Login from './Login'
import Logout from './Logout'
import { useAuth0 } from '@auth0/auth0-react'

const navStyles={
  backgroundColor: 'blue',
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'space-around',
  width: '100%',
  borderColor: 'red',
  borderWidth: 2,
  padding: 5,
}

const linkStyle={
  color: 'black',
  backgroundColor: 'white',
  border: 'solid',
  borderColor: 'black',
  borderWidth: '2px',
  borderRadius: 5,
  fontSize: 24,
  padding: 5,
  textDecoration: 'none'
}

const NavBar = ()=> {
  const { isAuthenticated, isLoading } = useAuth0()

  if (isLoading) {
    return <div> Loading...</div>
  }

  return (
    <div style={navStyles}>
      <Link style={linkStyle} to='/home'> Home</Link>
      <Link style={linkStyle} to='/add_movie'> Add Movie</Link>
      <Link style={linkStyle} to='/add_actor'> Add Actor</Link>
      <Link style={linkStyle} to='/add_star'> Add Star</Link>
      { !isAuthenticated ? <Login/> : <Logout/>
      }
    </div>
  )
}

export default NavBar
