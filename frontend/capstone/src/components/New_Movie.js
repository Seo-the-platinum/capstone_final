import React, { useState } from 'react'
import { useAuth0 } from '@auth0/auth0-react'

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

      fetch('http://localhost:5000/movies', {
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
    <div>
      <form onSubmit={handleSubmit}>
        <label>Title</label>
        <input
          value={newMovie.title || ''}
          type='text'
          name='title'
          onChange={handleTitle}/>
          <label>Release Date (mm/dd/yy)</label>
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
