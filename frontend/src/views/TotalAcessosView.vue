<template>
    <div class="container">
      <h1>Total de Acessos</h1>
      <div class="box">
						<canvas id="grafico_acessos"></canvas>
					</div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'TotalAcessosView',
    props: [ 'dadosRequisicao','createChart'],
    mounted(){
      this.createChart(this.dadosRequisicao.acessos_prod,'grafico_acessos')
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
  height: 500px; }
  </style>
  