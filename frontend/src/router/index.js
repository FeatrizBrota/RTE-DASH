import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TotalAcessosView from '../views/TotalAcessosView.vue'
import CenariosGeradosView from '../views/CenariosGeradosView.vue'
import EmpresasCriadasView from '../views/EmpresasCriadasView.vue'
import MonitoriaView from '../views/MonitoriaView.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  {
    path: '/total-acessos',
    name: 'total-acessos',
    component: TotalAcessosView
  },
  {
    path: '/cenarios-gerados',
    name: 'cenarios-gerados',
    component: CenariosGeradosView
  },
  {
    path: '/empresas-criadas',
    name: 'empresas-criadas',
    component: EmpresasCriadasView
  },
  {
    path: '/monitoria',
    name: 'monitoria',
    component: MonitoriaView
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
