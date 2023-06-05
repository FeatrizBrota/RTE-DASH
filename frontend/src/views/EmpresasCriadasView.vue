<template>
    <div class="container">
      <h1>Total de Empresas</h1>
      <div class="box">
						<canvas id="grafico_empresas"></canvas>
					</div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'EmpresasCriadasView',
    props: [ 'dadosRequisicao','createChart'],
    mounted(){
      this.createChart(this.dadosRequisicao.acessos_prod,'grafico_empresas')
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
  height: 500px; }  </style>
  