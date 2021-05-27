import React, { useState } from 'react'
import { Redirect } from 'react-router-dom'
import { useAuth0 } from '@auth0/auth0-react'

const Update_Movie = (props)=> {
  const [data, setData]= useState({
    id: props.location.state.movie.id,
    title:props.location.state.movie.title,
    release_date:props.location.state.movie.release_date,
  })

  const { getAccessTokenSilently } = useAuth0();

  const sendUpdate = async (e)=> {
    e.preventDefault()

    const { title, release_date, id }= data
    const audience = process.env.REACT_APP_API_AUDIENCE
    const accessToken = await getAccessTokenSilently({
      audience: audience,
    })

    let updatedMovie = {
      release_date: release_date,
      title: title,
    }

    try {
      fetch(`https://udacap.herokuapp.com/movies/${id}`, {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedMovie)
      })
      .then(res=> console.log(res.json()))
      .then(()=> <Redirect to='/'/>)
    }
    catch {
      console.log('failed to update movie')
    }
  }

  const handleTitle = (e)=> {
    let title = e.target.value
    setData({
      ...data,
      title: title,
    })
  }

  const handleDate = (e)=> {
    let date = e.target.value
    setData({
      ...data,
      release_date: date,
    })
  }

  const { release_date, title }= data
  console.log(title)
  return (
    <div>
      <form onSubmit={sendUpdate}>
        <input
          onChange={handleTitle}
          type='text'
          value={title}/>
        <input
          onChange={handleDate}
          type='text'
          value={release_date}/>
        <input type='submit'/>
      </form>
    </div>
  )
}

export default Update_Movie
