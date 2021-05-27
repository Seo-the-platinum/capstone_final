import React, { useState, useEffect } from 'react'
import { useAuth0 } from '@auth0/auth0-react'

const New_Star = ()=> {
  const [ data, setData] = useState({
    movies: [],
    actors: [],
    stars: [],
    unavailActors: [],
    selectedMovie: null,
    selectedActor: null,
    selectedTitle: null,
  })

  const { getAccessTokenSilently } = useAuth0()

  useEffect(()=> {
    const moviesUrl = fetch('http://localhost:5000/movies')
    const actorsUrl = fetch('http://localhost:5000/actors')
    const starsUrl = fetch('http://localhost:5000/stars')

    Promise.all([moviesUrl, actorsUrl, starsUrl])
    .then(values => Promise.all(values.map(value => value.json())))
    .then(finalVals => {
      setData({
        movies: finalVals[0].movies,
        actors: finalVals[1].actors,
        stars: finalVals[2].stars,
        unavailActors: [],
        selectedActor: false,
        selectedMovie: false,
        selectedTitle: null,

      })
    })
  }, [])

  const handleMovieSelection = (e)=> {
    let selected = e.target.value
    let selectedIndex = e.target.options['selectedIndex']
    let movie = e.target.options[selectedIndex].id
    setData({
      ...data,
      selectedMovie: movie,
      selected: selected,
    })

  }

  useEffect(()=> {

    buildList()
}, [data.selected])

  const buildList = ()=> {
    let list=[]
    const { selected } = data
    const { stars }= data
    stars.map(star => {
      if (star.movie.title === selected ) {
        list.push(star.actor.id)
        }
      return null
    })
    setData({
      ...data,
      unavailActors: list,
    })
  }

  const handleActorSelection = (e)=> {
      let actorIndex = e.target.options['selectedIndex']
      let actor = e.target.options[actorIndex].id
      setData({
        ...data,
        selectedActor: actor,
      })
  }

  const handleSubmit = async (e)=> {
    e.preventDefault()
    const { selectedActor, selectedMovie }= data

    let newStar = {
      actor_id: selectedActor,
      movie_id:selectedMovie,
    }

    const audience = process.env.REACT_APP_API_AUDIENCE

    try {

      const accessToken = await getAccessTokenSilently({
        audience: audience
      })

      fetch('http://localhost:5000/stars', {
        method: 'POST',
        headers: {
          'Authorization':`Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newStar),
      })
      .then(res=> console.log(res.json()))
    }
    catch {
      console.log('tried to add star')
    }
  }

  const { movies, actors, unavailActors, selectedMovie } = data
  console.log('before render', selectedMovie)
  return(
    <div>
      <form onSubmit={handleSubmit}>
        <label> Movie </label>
        <select defaultValue = 'choose here' onChange= {handleMovieSelection}>
          <option value="choose here" disabled hidden>Choose here</option>
          {movies.map((movie)=> {
            return (
              <option key = {movie.title} value={movie.title} id={movie.id}>
                {movie.title}
              </option>
            )
          })}
        </select>
        <label> Actor </label>
        <select defaultValue='choose here' onChange={handleActorSelection}>
          <option value="choose here" disabled hidden>Choose here</option>
          {
            actors.map((actor)=> {
              if (unavailActors.includes(actor.id)) {
            return null}
              else {
                return (
                  <option key = {actor.name} value={actor.name} id={actor.id}>
                    {actor.name}
                  </option>
                )
              }
          })}
        </select>
        <input type='submit'/>
      </form>
    </div>
  )
}

export default New_Star
