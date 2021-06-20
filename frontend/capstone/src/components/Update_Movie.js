import React, { useState } from 'react'
import { Redirect } from 'react-router-dom'
import { useAuth0 } from '@auth0/auth0-react'

const container={
  border: 'solid',
  borderColor: 'black',
  borderWidth: 2,
  borderRadius: 5,
  display: 'flex',
  flexDirection: 'column',
  padding: 10,
  marginTop: 5,
}

const formStyle={
  display: 'flex',
  flexDirection:'column',
  alignItems: 'space-around',
  justifyContent: 'space-around',
  height: '100%',
}

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
    <div style={container}>
      <h2> Update title or release data and time below</h2>
      <form
        style={formStyle}
        onSubmit={sendUpdate}>
        <h2>Title</h2>
        <input
          onChange={handleTitle}
          type='text'
          value={title}/>
        <h2> Date and Time (mm/dd/yyyy 00:00:00)</h2>
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
