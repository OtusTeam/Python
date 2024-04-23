<template>
  <img alt="Vue logo" src="./assets/logo.png">
  
  <div v-if="isAuth">
    <button v-on:click="logout">Logout</button>
  </div>
  <div v-else>
    <LoginForm @auth="auth" />
  </div>
  <button v-on:click="getAnimals">Получить список животных</button>
  <AnimalsList :items="animals" />
</template>

<script>
import axios from 'axios'
import LoginForm from './components/Auth.vue'
import AnimalsList from './components/Animals.vue'

export default {
  name: 'App',
  components: {
    LoginForm,
    AnimalsList
  },
  data() {
    return {
      animals: [
        //{'name': 'Борис', 'kind': 'Белый', 'family': 'Медведь'},
      ],
      isAuth: false,
      token: ''
    }
  },
  methods: {
      getAnimals() {
        let headers = {
          'Content-Type': 'application/json'
        }
        if (this.isAuth) {
          headers['Authorization'] = 'Token ' + this.token
        }
        axios.get('http://127.0.0.1:8000/api/animals/', {headers})
            .then(response => {
                this.animals = response.data
            }).catch(error => console.log(error))
    },
    auth(login, password) {
      // console.log(login)
      // console.log(password)
      // this.isAuth = true
      axios.post('http://127.0.0.1:8000/api-token-auth/', {username: login, password: password})
      .then(response => {
          const token = response.data['token']
          this.token = token
          this.isAuth = true
      }).catch(error => alert('Неверный логин или пароль' + error))
    },
    logout() {
      this.isAuth = false
      this.token = ''
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
