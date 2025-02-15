import { createRouter, createWebHistory } from 'vue-router'
import RegisterUser from '@/components/registerUser.vue'
import LoginView from '@/components/login.vue'
import DashboardView from '@/components/dashboard.vue'
import PersonasView from '@/components/personas.vue'
import UsuarioView from '@/components/usuario.vue'
import ResultadosEstudioView from '@/components/resultadosEstudio.vue'
import EstudioView from '@/components/estudio.vue'
import TablaResutadoEstudioView from '@/components/tablaResultadoEstudio.vue'
import TablaEstudiosView from '@/components/tablaEstudios.vue'
import PiePaginaView from '@/components/pie-pagina.vue'

// Seccion de Solicitudes
import RegistroSolicitudes from '@/components/Comite-Transplantes/RegistroSolicitudes.vue'
import TablaSolicitudes from '@/components/Comite-Transplantes/Tabla-Solicitudes.vue'
import UpdateSolucitud from '@/components/Comite-Transplantes/Update-Solucitud.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUser
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      children: [{
        path: '/personas',
        name: 'personas',
        component: PersonasView
      },
      {
        path: '/usuario',
        name: 'usuario',
        component: UsuarioView
      },
      {
        path: '/resultadosEstudio',
        name: 'resultadosEstudio',
        component: ResultadosEstudioView
      },
      {
        path: '/tablaResultadoEstudio',
        name: 'tablaResultadoEstudio',
        component: TablaResutadoEstudioView
      },
      {
        path: '/estudio',
        name: 'estudio',
        component: EstudioView
      },
      {
        path: '/tablaEstudios',
        name: 'tablaEstudios',
        component: TablaEstudiosView
      },
      // Seccion de Solicitudes
      {
        path: '/RegistroSolicitudes',
        name: 'RegistroSolicitudes',
        component: RegistroSolicitudes
      },
      {
        path: '/TablaSolicitudes',
        name: 'TablaSolicitudes',
        component: TablaSolicitudes
      },
      {
        path: '/UpdateSolicitudes',
        name: 'UpdateSolicitudes',
        component: UpdateSolucitud
      },
      {
        path: '/pie-pagina',
        name: 'piePagina',
        component: PiePaginaView
      }]
    }



  ]
})

export default router
