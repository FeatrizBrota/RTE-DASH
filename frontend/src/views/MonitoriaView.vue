<template>
    <div class="container">
      <h1>Monitoria</h1>
      <div class="box">
						<canvas id="grafico_monitoria"></canvas>
					</div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MonitoriaView',
    props: [ 'dadosRequisicao','createChart','createChartMonitoria'],
    mounted(){
      this.createChartMonitoria(this.dadosRequisicao.monitoria_prod)
    }
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
  