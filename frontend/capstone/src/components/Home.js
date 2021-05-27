import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useAuth0 } from '@auth0/auth0-react'

const Home = ()=> {

  const { user, isLoading, getAccessTokenSilently } = useAuth0()

  const [data, setData] = useState({
    stars:[],
    arrangedMovies: [],
  })

  useEffect(()=> {
    fetch('https://udacap.herokuapp.com/stars')
    .then(res=> res.json())
    .then(res => {
      let stars = res.stars
      setData({
        stars: stars,
        arrangedMovies: [],
      })
    })
  }, [])

  if (isLoading) {
    return <div> Loading...</div>
  }
  const get_token = async ()=> {
    const audience = process.env.REACT_APP_API_AUDIENCE
    const accessToken = await getAccessTokenSilently({
      audience: audience,
    })
    return accessToken
  }
  console.log(get_token())
  const { stars }= data
  return (
    <div>
      <h2>
        {user.name}
      </h2>
      <h2>
        Casting Sheet
      </h2>
      {stars.map(star=> {
        return (
          <div key={star.id}>
            <Link to={{
              pathname:'/delete_movie',
              state: {
                movie:star.movie,
              }
            }}>
              <h2>
                { star.movie.title }
              </h2>
            </Link>
            <Link to={{
              pathname: '/delete_actor',
              state: {
                actor: star.actor,
              }
            }}>
              <p>
                { star.actor.name}
              </p>
            </Link>
          </div>
        )
      })}
    </div>
  )
}

export default Home
