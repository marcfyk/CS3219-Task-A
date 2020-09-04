<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div>
        <hr />
        <b>X: </b>{{x}}
        <br />
        <b>Y: </b>{{y}}
        <hr />
        <b>X + Y: </b>{{sum}}
        <br />
        <b>| X - Y |: </b>{{difference}}
        <br />
        <b>X * Y: </b>{{product}}
        <br />
        <b>X / Y: </b>{{division}}
        <br />
        <b>X ^ Y: </b>{{exponent}}
        <hr />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'HelloWorld',
    props: {
        msg: String
    },
    data() {
        return {
            x: 0,
            y: 0,
            sum: 0,
            difference: 0,
            product: 0,
            division: 0,
            exponent: 0,
        };
    },
    async mounted() {
        const { x, y } = (await axios.get('http://localhost/rng')).data;
        this.x = x;
        this.y = y;
        const { sum, difference, product, division, exponent } = (await axios.get(`http://localhost/calculator?x=${x}&y=${y}`)).data;
        this.sum = sum;
        this.difference = difference;
        this.product = product;
        this.division = division;
        this.exponent = exponent;
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
