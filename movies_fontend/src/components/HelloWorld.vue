<template>
  <div class="hello">
    <el-input v-model="input" placeholder="输入想搜索的关键字"></el-input>
    <button class="btn btn-default cyan darken-3" type="button" @click="search(input)">搜索</button>
  <ul v-if="movies && movies.length">
     <el-table
    :data="movies"
    border
    style="width: 100%">
     <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left">
          <el-form-item label="下载链接">
            <span style="word-wrap: break-word;">{{ props.row.link }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      prop="create_date"
      label="日期"
      width="94%">
    </el-table-column>
    <el-table-column
      prop="name"
      label="名称">
    </el-table-column>
    <el-table-column
      label="操作"
      width="100">
      <template slot-scope="scope">
        <a size="small" :href="scope.row.link" target="_blank">下载</a>
      </template>
        </el-table-column>
  </el-table>
  </ul>
<template>
  <paginate
    :page-count="total"
    :page-range="3"
    :margin-pages="2"
    :click-handler="clickCallback"
    :prev-text="'Prev'"
    :next-text="'Next'"
    :container-class="'pagination'"
    :page-class="'page-item'">
  </paginate>
</template>
  </div>
</template>

<script>
import axios from 'axios'
var baseurl = 'http://127.0.0.1:8000/api/'

export default{
  name: 'HelloWorld',
  data () {
    return {
      total: 1,
      input: '',
      movies: [],
      errors: []
    }
  },
  methods: {
    clickCallback (pageNum) {
      axios.get(baseurl + `movieslist?page=` + pageNum)
      .then(response => {
      // JSON responses are automatically parsed.
        this.movies = response.data.results
      })
      .catch(e => {
        this.errors.push(e)
      })
    },
    search (input) {
      axios.get(baseurl + `searchlist?name=` + input)
      .then(response => {
        this.movies = response.data.results
        this.total = 1
      })
      .catch(e => {
        this.errors.push(e)
      })
    }
  },
  // created () {
  beforeCreate () {
    axios.get(baseurl + `movieslist`)
    .then(response => {
      this.movies = response.data.results
      this.total = Math.round(response.data.count / 20)
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: #00838f;
}
</style>
