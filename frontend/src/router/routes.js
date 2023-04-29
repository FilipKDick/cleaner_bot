
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: 'chore/', component: () => import('pages/ChoreAddPage.vue'), name: 'addChore' },
      { path: 'group/', component: () => import('pages/ChoreGroupAddPage.vue'), name: 'addGroup' },
      { path: 'all/', component: () => import('pages/IndexPage.vue'), name: 'allChores' }
    ]
  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
