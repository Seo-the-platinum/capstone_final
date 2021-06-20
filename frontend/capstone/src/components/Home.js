import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useAuth0 } from '@auth0/auth0-react'

const container={
  alignItems: 'center',
  border: 'solid',
  borderColor: 'black',
  borderWidth: 2,
  borderRadius: 5,
  backgroundColor: 'white',
  display: 'flex',
  flexDirection: 'column',
  marginTop: 10,
  width: '50%'
}

const casting={
  borderBottom: '2px solid black',
  width: '50%',
}

const link={
  textDecoration: 'none',
  color: 'black'
}

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
    return null
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
    <div style={container}>
      <h2>
        {`Hello, ${user.name}`}
      </h2>
      <h2 style={casting}>
        Casting Sheet
      </h2>
      {stars.map(star=> {
        return (
          <div key={star.id}>
            <Link
              style={link}
              to={{
              pathname:'/delete_movie',
              state: {
                movie:star.movie,
              }
            }}>
              <h2>
                { star.movie.title }
              </h2>
            </Link>
            <Link
              style={link}
              to={{
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
