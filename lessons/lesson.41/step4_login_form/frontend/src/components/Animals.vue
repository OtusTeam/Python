<template>
<table>
    <tr>
        <th>NAME</th>
        <th>FAMILY</th>
        <th>KIND</th>
    </tr>
     <tr v-for="item in items" :key="item.name">
            <td>{{item.name}}</td>
            <td>{{item.family}}</td>
            <td>{{item.kind}}</td>
        </tr>
</table>
</template>

<script>
export default {
  name: 'AnimalsList',
  props: ['items']
}
</script>