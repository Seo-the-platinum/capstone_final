import React, { useState } from 'react'
import { Redirect } from 'react-router-dom'
import { useAuth0 } from '@auth0/auth0-react'

const container={
  display: 'flex',
  border:'solid',
  borderColor:'black',
  borderRadius: 5,
  padding: 10,
  marginTop: 5,
}

const formStyle={
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'space-around',
}

const Update_Actor= (props)=> {
  const [data, setData]= useState({
    id: props.location.state.actor.id,
    name: props.location.state.actor.name,
    gender: props.location.state.actor.gender,
    age: props.location.state.actor.age,
  })

  const { getAccessTokenSilently } = useAuth0();

  const handleAge = (e)=> {
    let age = e.target.value

    setData({
      ...data,
      age: age,
    })
  }

  const handleName = (e)=> {
    let name = e.target.value

    setData({
      ...data,
      name: name,
    })
  }

  const handleGender= (e)=> {
    let gender = e.target.value

    setData({
      ...data,
      gender: gender,
    })
  }

  const sendUpdate = async (e)=> {
    e.preventDefault()

    const { id, name, gender, age }= data
    const audience = process.env.REACT_APP_API_AUDIENCE
    const accessToken = await getAccessTokenSilently({
      audience: audience,
    })

    const updatedActor = {
      id:id,
      name: name,
      gender: gender,
      age: age,
    }
    try {
      fetch(`https://udacap.herokuapp.com/actors/${id}`, {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedActor)
      })
      .then(()=> <Redirect to = '/'/>)
    }
    catch {
      console.log('update actors failed')
    }
  }

  const { age, name }= data
  return (
    <div style={container}>
      <form
        style={formStyle}
        onSubmit={sendUpdate}>
        <h2>Age</h2>
        <input
          onChange={handleAge}
          type='number'
          value={age}/>
        <h2>Name</h2>
        <input
          onChange={handleName}
          type='text'
          value={name}/>
        <h2> Gender </h2>
        <select
          id='gender'
          name='gender'
          onChange={handleGender}>
          <option value='Female'>
            Female
          </option>
          <option value="Male">
            Male
          </option>
        </select>
        <input type='submit'/>
      </form>
    </div>
  )
}

export default Update_Actor
