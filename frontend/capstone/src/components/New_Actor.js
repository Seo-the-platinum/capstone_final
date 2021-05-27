import React, { useState } from 'react'
import { useAuth0 } from '@auth0/auth0-react'

const New_Actor = ()=> {
  const [newActor, setActor]= useState({
    age: 0,
    gender: '',
    name: '',
    })

  const { getAccessTokenSilently } = useAuth0();

  const handleName = (e)=> {
    let n = e.target.value
    setActor({
      age: newActor.age,
      gender: newActor.gender,
      name: n,
    })
  }

  const handleAge = (e)=> {
    let a = e.target.value
    setActor({
      age: a,
      gender: newActor.gender,
      name: newActor.name,
    })
  }

  const handleGender = (e)=> {
    let g = e.target.value
    setActor({
      age: newActor.age,
      gender: g,
      name: newActor.name,
    })
  }

  const handleSubmit = async (e)=> {
    e.preventDefault()
    const actor = {
      age: newActor.age,
      gender: newActor.gender,
      name: newActor.name
    }

    const audience = process.env.REACT_APP_API_AUDIENCE

    try {
      const accessToken = await getAccessTokenSilently({
        audience: audience,
      })

      fetch('http://localhost:5000/actors', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(actor),
      })
      .then(res => console.log(res.json()))
    }

    catch {
      console.log('couldnt get token')
    }

  }


  return(
    <div>
      <form onSubmit={handleSubmit}>
        <label>name</label>
        <input
          value={newActor.name || ''}
          type='text'
          name='name'
          onChange={handleName}/>
          <label>Age</label>
          <input
            value={newActor.age}
            type='number'
            name='age'
            onChange={handleAge}/>
          <label>Gender</label>
          <select
            id='gender'
            name='gender'
            onChange={handleGender}>
            <option value='Female'>
              Female
            </option>
            <option value='Male'>
              Male
            </option>
            >
          </select>
        <input
          type='submit'
          value='submit'/>
      </form>
    </div>
  )
}

export default New_Actor
