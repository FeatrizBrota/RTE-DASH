<template>
	<div id="app">
		<head>
			<link
				rel="stylesheet"
				href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
			/>
			<link
				rel="stylesheet"
				href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/css/bulma.min.css"
			/>
		</head>
		<nav class="navbar" role="navigation" aria-label="main navigation">
			<div class="navbar-brand">
				<a class="navbar-item logo" href="/">
					<i class="fas fa-heart"></i>
					RTE DASH
				</a>

				<a
					role="button"
					class="navbar-burger burger"
					aria-label="menu"
					aria-expanded="false"
					data-target="navbarBasicExample"
				>
					<span aria-hidden="true"></span>
					<span aria-hidden="true"></span>
					<span aria-hidden="true"></span>
				</a>
			</div>

			<div id="navbarBasicExample" class="navbar-menu">
				<div class="navbar-start">
					<router-link to="/" class="navbar-item"> Home </router-link>

					<router-link to="/total-acessos" class="navbar-item">
						Total Acessos
					</router-link>

					<router-link to="/cenarios-gerados" class="navbar-item">
						Cenários Gerados
					</router-link>

					<router-link to="/empresas-criadas" class="navbar-item">
						Empresas Criadas
					</router-link>

					<router-link to="/monitoria" class="navbar-item">
						Monitoria
					</router-link>
				</div>
			</div>
		</nav>
		<Loader v-if="blLoading"></Loader>
		<router-view
			v-else
			:dadosRequisicao="dadosRequisicao"
			:createChartMonitoria="createChartMonitoria"
			:createChart="createChart"
		/>
	</div>
</template>
<script>
	import axios from "axios";
	import Chart from "chart.js/auto";
	import Loader from "./components/Loader/Loader.vue";

	export default {
		name: "App",
		data() {
			return {
				dadosRequisicao: null,
				blLoading: true,
			};
		},
		components: { Loader },
		mounted() {
			this.fetchData();
		},
		methods: {
			fetchData() {
				axios
					.get("/dados")
					.then((response) => {
						console.log(response.data);
						this.dadosRequisicao = response.data;
						this.blLoading = false;
					})
					.catch((error) => {
						console.error(error);
						this.blLoading = false;
					});
			},
			createChart(resultados, id, titulo) {
				var ctx = document.getElementById(id).getContext("2d");
				var chart = new Chart(ctx, {
					type: "bar",
					data: {
						labels: resultados.map((item) => item[0]),
						datasets: [
							{
								label: "Quantidade",
								data: resultados.map((item) => item[1]),
								backgroundColor: "#04639271",
								borderColor: "rgba(4, 99, 146, 1)",
								borderWidth: 1,
								borderRadius: 10, // Define o raio do arredondamento das bordas
							},
						],
					},
					options: {
						maintainAspectRatio: false,
						responsive: true,
						scales: {
							y: {
								beginAtZero: true,
							},
						},
						plugins: {
							title: {
								display: true,
								text: titulo,
								font: {
									size: 18,
									weight: "bold",
								},
							},
						},
					},
				});
			},

			createChartMonitoria(dados) {
				const separatedData = {};

				dados.forEach(([name, month, value]) => {
					if (!separatedData[name]) {
						separatedData[name] = [];
					}

					separatedData[name].push([month, value]);
				});

				const pisCofinsData = separatedData["PIS/COFINS"];
				const cideCombustiveisData = separatedData["CIDE COMBUSTÍVEIS"];
				const ipiData = separatedData["IPI"];
				const icmsData = separatedData["ICMS"];

				const pisCofinsLabels = pisCofinsData.map(([month, _]) => month);
				const pisCofinsValues = pisCofinsData.map(([_, value]) => value);

				const cideCombustiveisLabels = cideCombustiveisData.map(
					([month, _]) => month
				);
				const cideCombustiveisValues = cideCombustiveisData.map(
					([_, value]) => value
				);

				const ipiLabels = ipiData.map(([month, _]) => month);
				const ipiValues = ipiData.map(([_, value]) => value);

				const icmsLabels = icmsData.map(([month, _]) => month);
				const icmsValues = icmsData.map(([_, value]) => value);

				const ctx = document
					.getElementById("grafico_monitoria")
					.getContext("2d");
				new Chart(ctx, {
					type: "bar",
					data: {
						labels: pisCofinsLabels,
						datasets: [
							{
								label: "PIS/COFINS",
								data: pisCofinsValues,
								backgroundColor: "rgba(4, 99, 146, 0.5)",
								borderRadius: 10,
							},
							{
								label: "CIDE Combustíveis",
								data: cideCombustiveisValues,
								backgroundColor: "rgba(79, 185, 238, 0.5)",
								borderRadius: 10,
							},
							{
								label: "IPI",
								data: ipiValues,
								backgroundColor: "rgba(6, 124, 184, 1)",
								borderRadius: 10,
							},
						],
					},
					options: {
						maintainAspectRatio: false,
						responsive: true,
						scales: {
							y: {
								beginAtZero: true,
							},
						},
						plugins: {
							title: {
								display: true,
								text: "Total de Produtos Monitorados por Imposto",
								font: {
									size: 18,
									weight: "bold",
								},
							},
						},
					},
				});
			},
		},
	};
</script>

<style lang="scss" scoped>
	#app {
		font-family: Avenir, Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
	}

	.navbar {
		background-color: #f5f5f5;
	}

	.logo {
		font-size: 24px;
		font-weight: bold;
		color: #2c3e50;
		display: flex;
		align-items: center;

		i {
			margin-right: 5px;
		}
	}
	.navbar {
		background-color: #046392;
	}
	.navbar-item {
		font-weight: bold;
		color: #fff;

		&.is-active {
			color: #133d2a;
		}
	}

	.navbar-burger {
		border: none;
		background-color: transparent;

		span {
			background-color: #2c3e50;
		}
	}
	.navbar-brand {
		color: #16262e;
	}
	.navbar-link.is-active,
	.navbar-link:focus,
	.navbar-link:focus-within,
	.navbar-link:hover,
	a.navbar-item.is-active,
	a.navbar-item:focus,
	a.navbar-item:focus-within,
	a.navbar-item:hover {
		background-color: #fff;
		color: #046392;
	}
</style>
