<template>
    <div class="container">
      <h1>Cenários Gerados</h1>
      <div class="box">
						<canvas id="grafico_cenarios"></canvas>
					</div>
    </div>
  </template>
  
  <script>
  import Chart from 'chart.js';
  
  export default {
    name: 'CenariosGeradosView',
    props: [ 'dadosRequisicao','createChart'],
    mounted(){
      this.createChart(this.dadosRequisicao.acessos_prod,'grafico_cenarios')
    }
    // Coloque as opções do componente, se necessário
  }
  </script>
  
  <style scoped>
    	h1 {
		text-align: center;
		font-size: 24px;
		margin: 10px;
    color: #046392;
	}
.box {
  height: 500px; }  </style>
  