<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <LoginForm @auth="auth" />
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
      isAuth: false
    }
  },
  methods: {
      getAnimals() {
      axios.get('http://127.0.0.1:8000/api/animals/')
          .then(response => {
              this.animals = response.data
          }).catch(error => console.log(error))
    },
    auth(login, password) {
      console.log(login)
      console.log(password)
      this.isAuth = true
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
