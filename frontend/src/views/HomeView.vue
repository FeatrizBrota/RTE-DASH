<template>
	<section class="principal">
	
		<div>
	
			<div>
				<canvas id="grafico_cenario"></canvas>
			</div>
		
			<div>
				<canvas id="grafico_empresas"></canvas>
			</div>
		</div>
		<section class="space">
		
		</section>
		<div>
	
			<div>
				<canvas id="grafico_acessos"></canvas>
			</div>
	
			<div>
				<canvas id="grafico_monitoria"></canvas>
			</div>
		</div>
	</section>
</template>

<script>
	export default {
		name: "HomeView",
		components: {},
		props: ["dadosRequisicao", "createChart", "createChartMonitoria"],
		mounted() {
			this.createChart(this.dadosRequisicao.cenarios_prod, "grafico_cenario", 'Total de Cenarios');
			this.createChart(this.dadosRequisicao.acessos_prod, "grafico_acessos", 'Total de acessos');
			this.createChart(this.dadosRequisicao.empresas_prod, "grafico_empresas", 'Total de Empresas Criadas');
			this.createChartMonitoria(this.dadosRequisicao.monitoria_prod);
		},
		methods: {},
	};
</script>

<style scoped>
	/* Estilos personalizados aqui */
	h1 {
		font-size: 24px;
	}
	h3 {
		text-align: center;
		font-size: 20px;
		margin: 20px;
	}
	div {
		text-align: center;
		width: 100%;
		height: 200px;
	}
	.principal {
		text-align: center;
		padding: 30px 100px;
		/* border: 1px solid #000; */
		display: flex;
		justify-content: center;
		align-items: center;
		align-content: center;
	}
	.space {
		margin: 20px;
	}
</style>