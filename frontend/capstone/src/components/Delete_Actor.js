import React from 'react'
import { Link, Redirect } from 'react-router-dom'
import { useAuth0 } from '@auth0/auth0-react'

const Delete_Actor= (props)=> {

  const { getAccessTokenSilently } = useAuth0()

  const deleteActor = async (e)=> {

    e.preventDefault()
    const audience = process.env.REACT_APP_API_AUDIENCE

    const accessToken = await getAccessTokenSilently({
      audience: audience,
    })

    try {

      const { actor }= props.location.state

      fetch(`https://udacap.herokuapp.com/actors/${actor.id}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'applications/json',
        }
      }).then(res=> console.log(res.json()))
      .then(()=> <Redirect to='/'/>)
    }
   catch {
     console.log('unable to delete actor')
   }
  }


  const { actor }= props.location.state
  return (
    <div>
      <h2>
        { actor.name }
      </h2>
      <button onClick={deleteActor}>
        <label> Delete </label>
      </button>
      <Link to={{
        pathname: '/update_actor',
        state: {
          actor: actor,
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

export default Delete_Actor
