<template>
  <div class="hello">
  <ul v-if="movies && movies.length">
    <table class="card-panel bordered highlight purple lighten-2" >
        <thead>
          <tr>
              <th>发布时间</th>
              <th>电影名称</th>
          </tr>
        </thead>
      <tbody v-for="movie of movies">
        <tr>
      <td>{{movie.create_date}}</td>
      <td>{{movie.name}}</td>
        </tr>
      </tbody>
    </table>
  </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default{
  name: 'HelloWorld',
  data () {
    return {
      movies: [],
      errors: []
    }
  },
  created () {
    axios.get(`http://127.0.0.1:8000/api/movieslist`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.movies = response.data.results
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

a {
  color: #42b983;
}
</style>
