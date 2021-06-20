import React, { useState } from 'react'
import { useAuth0 } from '@auth0/auth0-react'

const container={
  display: 'flex',
  flexDirection: 'column',
  border: 'solid',
  borderColor: 'black',
  borderWidth: 2,
  borderRadius: 5,
  padding: 10,
  marginTop: 5,
}

const formStyle={
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'space-around',
  height: '100%'
}

const New_Movie = ()=> {
  const [newMovie, setMovie]= useState({
    title: '',
    releaseDate: '',
    })

  const { getAccessTokenSilently } = useAuth0()

  const handleTitle = (e)=> {
    let t = e.target.value
    setMovie({
      title: t,
      releaseDate: newMovie.releaseDate
    })
  }

  const handleDate = (e)=> {
    let date = e.target.value
    setMovie({
      releaseDate: date,
      title: newMovie.title,
    })
  }

  const handleSubmit = async (e)=> {
    e.preventDefault()

    const movie = {
      title: newMovie.title,
      release_date: newMovie.releaseDate,
    }

    const audience = process.env.REACT_APP_API_AUDIENCE

    try {

      const accessToken = await getAccessTokenSilently({
        audience: audience,
      })

      fetch('https://udacap.herokuapp.com/movies', {
        method: 'POST',
        headers: {
          'Authorization':`Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(movie),
      })
      .then(res => console.log(res.json()))
    }
    catch {
      console.log('unable to add movie')
    }
  }

  return(
    <div style={container}>
      <form
        style={formStyle}
        onSubmit={handleSubmit}>
        <h2>Title</h2>
        <input
          value={newMovie.title || ''}
          type='text'
          name='title'
          onChange={handleTitle}/>
          <h2>Release Date (mm/dd/yy 00:00:00)</h2>
          <input
            value={newMovie.releaseDate || ''}
            type='text'
            name='realeaseDate'
            onChange={handleDate}/>
        <input
          type='submit'
          value='submit'/>
      </form>
    </div>
  )
}

export default New_Movie
