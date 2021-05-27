import React from 'react'
import { Link, Redirect } from 'react-router-dom'
import { useAuth0 } from '@auth0/auth0-react'

const Delete_Movie = (props)=> {

  const { getAccessTokenSilently } = useAuth0()

  const deleteMovie = async (e)=> {

      e.preventDefault()

      const { movie }= props.location.state
      const audience = process.env.REACT_APP_API_AUDIENCE
      const accessToken = await getAccessTokenSilently({
        audience: audience,
      })
      try {
        fetch(`https://udacap.herokuapp.com/movies/${movie.id}`, {
          method: 'DELETE',
          headers: {
            'Authorization': `Bearer ${accessToken}`,
            'Content-Type': 'applications/json',
          }
        })
        .then(res => console.log(res.json()))
        .then(()=> <Redirect to='/'/>)
      }
      catch {
        console.log('couldnt delete movie')
      }
  }

  const { movie }= props.location.state
  return (
    <div>
      <h2>
        {movie.title}
      </h2>
      <button onClick = {deleteMovie}>
        <label>Delete</label>
      </button>
        <Link to={{
          pathname: '/update_movie',
          state: {
            movie: movie,
          }
        }}>
        <button>
          <label>
            Update
          </label>
        </button>
      </Link>
    </div>
  )
}

export default Delete_Movie
