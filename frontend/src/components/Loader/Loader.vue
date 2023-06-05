<template>
	<body>
		<div class="loading"></div>
	</body>
</template>



<script>
	export default {
		name: "Loader",
		// Coloque as opções do componente, se necessário
	};
</script>

<style scoped>
	body {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 100vh;
		background-color: #f2f2f2;
	}

	.loading {
		width: 50px;
		height: 50px;
		border: 5px solid #ccc;
		border-top-color: #046392;
		border-radius: 50%;
		animation: spin 1s infinite linear;
	}

	@keyframes spin {
		from {
			transform: rotate(0deg);
		}
		to {
			transform: rotate(360deg);
		}
	}
</style>
