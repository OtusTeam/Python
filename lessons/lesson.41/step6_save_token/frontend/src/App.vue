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
import Cookies from 'universal-cookie';
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
    }
  },
  methods: {
      getAnimals() {
        let headers = {
          'Content-Type': 'application/json'
        }
        if (this.isAuth) {
          const token = this.getToken()
          headers['Authorization'] = 'Token ' + token
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
          this.saveToken(token)
          this.isAuth = true
      }).catch(error => alert('Неверный логин или пароль' + error))
    },
    logout() {
      this.isAuth = false
      this.removeToken()
    },
    saveToken(token) {
      localStorage.setItem('token', token)
      const cookies = new Cookies()
      cookies.set('token', token)
      //cookies.set('token', token, {'httpOnly': true})
    },
    getToken() {
      // локалстораж
      const token_localstorage = localStorage.getItem('token')
      // куки
      //const cookies = new Cookies()
      //const token_cookie = cookies.get('token')
      return token_localstorage
      //return token_cookie
    },
    removeToken() {
      //локалстораж
      localStorage.setItem('token', '')
      //куки
      const cookies = new Cookies()
      cookies.set('token', '')
    }
  },
  mounted() {
    const token = this.getToken()
    console.log(token)
    if (token != null) {
      if (token !== '') {
        this.isAuth = true
      }
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
